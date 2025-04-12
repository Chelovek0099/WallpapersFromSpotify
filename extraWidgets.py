from PySide6.QtWidgets import QLabel, QLineEdit, QComboBox, QFrame, QHBoxLayout, QCheckBox
from PySide6.QtCore import Signal, QSize


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


class LineEdits(QFrame):
    def __init__(self, left_margin, *names: str, parent=None):
        super().__init__(parent)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(left_margin, 0, 0, 0)

        self.setMinimumSize(0, 24)
        self.setMaximumSize(16777215, 24)

        self.line_edits = []
        for name in names:
            line_edit = ClickableLineEdit(self)
            line_edit.setPlaceholderText(name)
            line_edit.setStyleSheet(u"color: white;\n"
                                    "border:1px solid rgb(18, 18, 18);\n"
                                    "border-radius: 5px;\n"
                                    "background-color: rgb(18, 18, 18);")
            line_edit.setMaximumSize(90 - len(names) * 12, 24)
            line_edit.setMinimumSize(70 - len(names) * 12, 24)
            self.horizontalLayout.addWidget(line_edit)
            self.line_edits.append(line_edit)

        frame = Frame(self)
        self.horizontalLayout.addWidget(frame)

    def setActive(self, active):
        for line_edit in self.line_edits:
            line_edit.setEnabled(active)

    def getLineEdits(self):
        return self.line_edits

    def setTexts(self, texts):
        length = len(self.line_edits)
        for i in range(length):
            self.line_edits[i].setText(str(texts[i] if length != 1 else texts))


class NamedCheckBox(QFrame):
    def __init__(self, left_margin, name, parent=None):
        super().__init__(parent)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(left_margin, 0, 0, 0)

        self.setMinimumSize(0, 24)
        self.setMaximumSize(16777215, 24)

        self.label = ClickableLabel(self)
        self.label.setText(name)
        self.label.setMinimumSize(195, 24)
        self.label.setMaximumSize(195, 24)
        self.horizontalLayout.addWidget(self.label)

        self.checkbox = QCheckBox(self)
        self.checkbox.setStyleSheet("QCheckBox::indicator {"
                                    "width: 15px;"
                                    "height: 15px;"
                                    "background-color: rgb(18, 18, 18);"
                                    "border: 1px solid;"
                                    "border-radius: 5px;"
                                    "} QCheckBox::indicator::checked {"
                                    "background-color: white;"
                                    "}")
        self.checkbox.setMinimumSize(0, 24)
        self.checkbox.setMaximumSize(16777215, 24)
        self.horizontalLayout.addWidget(self.checkbox)

    def setActive(self, active):
        self.checkbox.setEnabled(active)

    def setChecked(self, checked):
        self.checkbox.setChecked(bool(checked))


class ComboBox(QFrame):
    def __init__(self, left_margin, *options, parent=None):
        super().__init__(parent)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(left_margin, 0, 0, 0)

        self.setMinimumSize(0, 24)
        self.setMaximumSize(16777215, 24)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems(options)
        self.comboBox.setStyleSheet("color: white;"
                                    "border:1px solid rgb(18, 18, 18);"
                                    "border-radius: 5px;"
                                    "background-color: rgb(18, 18, 18);")
        self.comboBox.setMinimumSize(70, 24)
        self.comboBox.setMaximumSize(70, 24)

        frame = Frame(self)

        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout.addWidget(frame)

    def setActive(self, active):
        self.comboBox.setEnabled(active)

    def setText(self, text):
        mode = self.comboBox.findText(str(text))
        self.comboBox.setCurrentIndex(mode)


class Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(0, 24)
        self.setMaximumSize(16777215, 24)


class H1(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setStyleSheet("font-size: 24px")
        self.setMinimumSize(0, 40)
        self.setMaximumSize(16777215, 40)
        self.setText(text)


class H2(QFrame):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(16, 0, 0, 0)

        label = ClickableLabel()
        label.setStyleSheet("font-size: 20px")
        label.setMinimumSize(0, 40)
        label.setMaximumSize(16777215, 40)
        label.setText(text)

        self.horizontalLayout.addWidget(label)


class H3(QFrame):
    def __init__(self, left_margin, text, parent=None):
        super().__init__(parent)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(left_margin, 0, 0, 0)

        self.setMinimumSize(0, 24)
        self.setMaximumSize(16777215, 24)

        self.label = ClickableLabel()
        self.label.setMinimumSize(0, 24)
        self.label.setMaximumSize(16777215, 24)
        self.label.setText(text)

        self.horizontalLayout.addWidget(self.label)

    def setClickedEvent(self, clicked):
        self.label.clicked.connect(lambda: clicked)


class AddonLabel(ClickableLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setMinimumSize(0, 34)
        self.setMaximumSize(16777215, 34)
        self.setText(text)
        self.text = text

    def getText(self):
        return self.text
