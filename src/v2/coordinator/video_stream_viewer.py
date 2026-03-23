import requests
from PySide6.QtCore import QObject, Qt, QThread, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QMessageBox, QVBoxLayout, QWidget


class MjpegStreamWorker(QObject):
    frame_ready = Signal(QImage)
    error = Signal(str)
    finished = Signal()

    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self._running = True

    @Slot()
    def run(self):
        try:
            with requests.get(self.url, stream=True, timeout=10) as response:
                response.raise_for_status()
                buffer = b""

                for chunk in response.iter_content(chunk_size=4096):
                    if not self._running:
                        break

                    if not chunk:
                        continue

                    buffer += chunk

                    while True:
                        start = buffer.find(b"\xff\xd8")
                        end = buffer.find(b"\xff\xd9", start + 2)

                        if start != -1 and end != -1:
                            jpg = buffer[start : end + 2]
                            buffer = buffer[end + 2 :]

                            image = QImage.fromData(jpg, "JPEG")
                            if not image.isNull():
                                self.frame_ready.emit(image)
                        else:
                            break

        except requests.RequestException as e:
            if self._running:
                self.error.emit(f"Errore di rete: {e}")
        except Exception as e:
            if self._running:
                self.error.emit(f"Errore nello stream: {e}")
        finally:
            self.finished.emit()

    def stop(self):
        self._running = False


class MjpegViewerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._last_pixmap = QPixmap()
        self._current_url = ""
        self.thread = None
        self.worker = None

        self.image_label = QLabel("No active stream")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background-color: black; color: white;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.image_label)

    def start_stream(self, url: str):
        if not url:
            self.show_error("URL for stream not valid")
            return

        self.stop_stream(clear_image=False)

        self._current_url = url
        self.image_label.setText("Connection to video stream...")
        self.image_label.setPixmap(QPixmap())
        self._last_pixmap = QPixmap()

        self.thread = QThread(self)
        self.worker = MjpegStreamWorker(url)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.frame_ready.connect(self.update_frame)
        self.worker.error.connect(self.show_error)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self._on_thread_finished)

        self.thread.start()

    def stop_stream(self, clear_image=True):
        if self.worker is not None:
            self.worker.stop()

        if self.thread is not None and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait(2000)

        self.worker = None
        self.thread = None
        self._current_url = ""

        if clear_image:
            self._last_pixmap = QPixmap()
            self.image_label.setPixmap(QPixmap())
            self.image_label.setText("Stream stopped")

    @Slot()
    def _on_thread_finished(self):
        if self.thread is not None:
            self.thread.deleteLater()
        self.thread = None
        self.worker = None

    @Slot(QImage)
    def update_frame(self, image: QImage):
        pixmap = QPixmap.fromImage(image)
        self._last_pixmap = pixmap
        self._refresh_pixmap()

    def _refresh_pixmap(self):
        if self._last_pixmap.isNull():
            return

        scaled = self._last_pixmap.scaled(
            self.image_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )
        self.image_label.setPixmap(scaled)

    @Slot(str)
    def show_error(self, message: str):
        self.image_label.setPixmap(QPixmap())
        self.image_label.setText("Video stream error")
        QMessageBox.critical(self, "Error", message)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._refresh_pixmap()

    def closeEvent(self, event):
        self.stop_stream()
        super().closeEvent(event)
