"""
Raspberry Pi coordinator

"""

from pathlib import Path

from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class ResultsWidget(QWidget):
    """
    widget for visualizing text output
    """

    def __init__(self):
        super().__init__()

        self.parameters = False

        self.setWindowTitle("")

        hbox = QVBoxLayout()

        self.lb = QLabel("")
        hbox.addWidget(self.lb)

        self.ptText = QPlainTextEdit()
        self.ptText.setFont(
            QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        )

        hbox.addWidget(self.ptText)

        hbox2 = QHBoxLayout()
        hbox2.addItem(QSpacerItem(241, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.pbSave = QPushButton("Save output", clicked=self.save_results)
        hbox2.addWidget(self.pbSave)

        self.pbOK = QPushButton("OK", clicked=self.close)
        hbox2.addWidget(self.pbOK)

        hbox.addLayout(hbox2)

        self.setLayout(hbox)

        self.resize(540, 640)

    def save_results(self):
        """
        save content of self.ptText
        """

        if self.parameters:
            file_name = str(Path(__file__).parent / "config_coordinator.py")
        else:
            fn = QFileDialog().getSaveFileName(
                self, "Save output", "", "Text files (*.txt *.tsv);;All files (*)"
            )
            file_name = fn[0] if type(fn) is tuple else fn

        if file_name:
            try:
                with open(file_name, "w") as f:
                    f.write(self.ptText.toPlainText())
            except Exception:
                QMessageBox.critical(self, "", f"The file {file_name} can not be saved")
