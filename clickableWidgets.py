from PySide6.QtWidgets import QLabel, QLineEdit, QComboBox
from PySide6.QtCore import Signal


class ClickableLabel(QLabel):
    clicked = Signal()

    def mouseReleaseEvent(self, e):
        self.clicked.emit()


class ClickableLineEdit(QLineEdit):
    clicked = Signal()

    def mouseReleaseEvent(self, e):
        self.clicked.emit()


class ClickableComboBox(QComboBox):
    clicked = Signal()

    def mouseReleaseEvent(self, e):
        self.clicked.emit()
