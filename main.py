import os
import sys
import json

from spotipyHandler import SpCaller

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

        self.ui_new_window.apply.clicked.connect(lambda: self.apply_button())
        self.ui_new_window.cancel.clicked.connect(lambda: self.cancel_button())
        self.ui_new_window.ok.clicked.connect(lambda: self.ok_button())

        self.ui_new_window.addons_button.clicked.connect(lambda: self.ui_new_window.changeEnableWidgets())

    def keyPressEvent(self, event):
        if event.modifiers().name == 'ControlModifier|AltModifier' and event.text() == 'P':
            self.new_window.show()

            self.ui_new_window.get_configs()
            self.old_enavled_widgets = self.ui_new_window.enabled_widgets.copy()
            self.old_widgets = self.ui.widgets.copy()
            self.last_widgets = self.old_widgets.copy()
            self.enabledWidgets = self.ui_new_window.enabled_widgets

    def apply_button(self):
        self.ui_new_window.apply_func()
        self.setEnabledWidgets(self.enabledWidgets)
        self.changeEnableWidgets(self.last_widgets, self.enabledWidgets)
        self.last_widgets = self.enabledWidgets.copy()
        self.ui.widgetsUpdate()

    def cancel_button(self):
        self.ui_new_window.cancel_func()
        self.setEnabledWidgets(self.old_enavled_widgets)
        self.changeEnableWidgets(self.last_widgets, self.old_widgets)
        self.new_window.close()
        self.ui.widgetsUpdate()

    def ok_button(self):
        self.ui_new_window.ok_func()
        enabledWidgets = self.ui_new_window.enabled_widgets.copy()
        self.setEnabledWidgets(enabledWidgets)
        self.changeEnableWidgets(self.last_widgets, enabledWidgets)
        self.old_widgets = self.ui.widgets.copy()
        self.last_widgets = self.old_widgets.copy()
        self.new_window.close()
        self.ui.widgetsUpdate()

    def changeEnableWidgets(self, old_widgets, new_widgets):
        print(old_widgets, new_widgets)
        old_widgets, new_widgets = set(old_widgets), set(new_widgets)
        unification = old_widgets & new_widgets
        old_widgets = old_widgets - unification
        new_widgets = new_widgets - unification
        for widget in old_widgets:
            self.ui.deleteWidget(widget)
            self.ui_new_window.deleteLayoutIntoSrollByName(widget)
            print(f"{widget} enabled")
        for widget in new_widgets:
            self.ui.addWidget(widget)
            self.ui_new_window.addWidgetParameters(widget)
            print(f"{widget} deleted")

    def setEnabledWidgets(self, enabled_widgets):
        with open('enabledWidgets.json', 'w') as enabledWidgetsFile:
            json.dump(enabled_widgets, enabledWidgetsFile, indent=4)


if __name__ == "__main__":
    if os.path.exists(".cache"):
        app = QApplication(sys.argv)
        window = MainWindow()
        window.showFullScreen()

        app.exec()
    else:
        spCaller = SpCaller()
        spCaller.initCache()
