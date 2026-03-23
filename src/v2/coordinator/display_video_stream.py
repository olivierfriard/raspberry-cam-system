import sys
import re

from PySide6.QtCore import QObject, QThread, Qt, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
    QWidget,
)

import requests


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

                content_type = response.headers.get("Content-Type", "")
                boundary = None

                match = re.search(r'boundary="?([^";]+)"?', content_type, re.IGNORECASE)
                if match:
                    boundary = match.group(1).encode()

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
                            jpg = buffer[start:end + 2]
                            buffer = buffer[end + 2:]

                            image = QImage.fromData(jpg, "JPEG")
                            if not image.isNull():
                                self.frame_ready.emit(image)
                        else:
                            break

        except requests.RequestException as e:
            self.error.emit(f"Errore di rete: {e}")
        except Exception as e:
            self.error.emit(f"Errore nello stream: {e}")
        finally:
            self.finished.emit()

    def stop(self):
        self._running = False


class MjpegViewerWidget(QWidget):
    def __init__(self, url: str, parent=None):
        super().__init__(parent)
        self.url = url
        self._last_pixmap = QPixmap()

        self.image_label = QLabel("Connessione allo stream...")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(640, 480)
        self.image_label.setStyleSheet("background-color: black; color: white;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)

        self.thread = QThread(self)
        self.worker = MjpegStreamWorker(self.url)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.frame_ready.connect(self.update_frame)
        self.worker.error.connect(self.show_error)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    @Slot(QImage)
    def update_frame(self, image: QImage):
        pixmap = QPixmap.fromImage(image)
        self._last_pixmap = pixmap

        scaled = pixmap.scaled(
            self.image_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )
        self.image_label.setPixmap(scaled)

    @Slot(str)
    def show_error(self, message: str):
        self.image_label.setText("Errore stream")
        QMessageBox.critical(self, "Errore", message)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if not self._last_pixmap.isNull():
            scaled = self._last_pixmap.scaled(
                self.image_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.image_label.setPixmap(scaled)

    def closeEvent(self, event):
        self.worker.stop()
        if self.thread.isRunning():
            self.thread.quit()
            self.thread.wait(2000)
        super().closeEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MJPEG Viewer")

        url = "http://130.192.101.53:8000/stream.mjpg"
        self.viewer = MjpegViewerWidget(url)
        self.setCentralWidget(self.viewer)
        self.resize(900, 700)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())