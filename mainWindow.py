import json
import sys

from PIL import Image

from PySide6.QtWidgets import QWidget

from parametersConfig import Ui_Dialog

from spotipyHandler import SpCaller

with open('widgets.json') as widgets_config:
    widgets = json.load(widgets_config)

all_widgets = []
updateTrack = []
updatePlayback = []
updateWidget = []

for widget in widgets:
    exec('from addons.' + widget + '.widget import Widget')

    all_widgets.append(widget)
    if hasattr(eval('Widget'), 'updateTrack'):
        updateTrack.append(widget)
    if hasattr(eval('Widget'), 'updatePlayback'):
        updatePlayback.append(widget)
    if hasattr(eval('Widget'), 'updateWidget'):
        updateWidget.append(widget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(0, 0, 10000, 10000)

        self.sp_caller = SpCaller()
        playback = self.sp_caller.getTarckInfo()

        for widget in all_widgets:
            exec('from addons.' + widget + '.widget import Widget')

            exec('self.' + widget + ' = Widget(self.centralwidget)')
            exec('self.' + widget + f'.init({playback}, {(255, 255, 255)})')
