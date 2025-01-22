import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from mainWindow import Ui_MainWindow
from parametersConfig import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.new_window = QDialog()
        self.ui_new_window = Ui_Dialog()
        self.ui_new_window.setupUi(self.new_window)

    def keyPressEvent(self, event):
        if event.modifiers().name == 'ControlModifier|AltModifier' and event.text() == 'P':
            self.new_window.show()

            self.ui_new_window.apply.clicked.connect(lambda: self.apply_button())
            self.ui_new_window.cancel.clicked.connect(lambda: self.cancel_button())
            self.ui_new_window.ok.clicked.connect(lambda: self.ok_button())

            self.ui_new_window.get_configs()

    def apply_button(self):
        self.ui_new_window.apply_func()
        self.ui.widgetsUpdate()

    def cancel_button(self):
        self.ui_new_window.cancel_func()
        self.new_window.close()
        self.ui.widgetsUpdate()

    def ok_button(self):
        self.ui_new_window.ok_func()
        self.new_window.close()
        self.ui.widgetsUpdate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()

    app.exec()
