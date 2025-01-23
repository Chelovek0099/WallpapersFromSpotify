import json
import threading

from PySide6.QtWidgets import QWidget

from PIL import Image
from spotipyHandler import SpCaller
from domColor import sqrt_algorithm


with open('widgets.json') as widgets_config:
    widgets = json.load(widgets_config)

updateTrack = []
updatePlayback = []
updateWidget = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        with open('backgroundConfig.json', 'r') as backgroundConfig:
            self.backgroundConfig = json.load(backgroundConfig)
            self.backgroundColorFixed = self.backgroundConfig['backgroundColorFixed']
            self.backgroundColor = self.backgroundConfig['backgroundColor']

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(0, 0, 10000, 10000)

        self.sp_caller = SpCaller()
        playback = self.sp_caller.getTrackInfo()

        for widget in widgets:
            exec('from addons.' + widget + '.widget import Widget')

            exec('self.' + widget + ' = Widget(self.centralwidget)')
            exec('self.' + widget + f'.init({playback}, (255, 255, 255))')

            if hasattr(eval('Widget'), 'updateTrack'):
                updateTrack.append(widget)
            if hasattr(eval('Widget'), 'updatePlayback'):
                updatePlayback.append(widget)
            if hasattr(eval('Widget'), 'updateWidget'):
                updateWidget.append(widget)

        self.changeBackground()

        track_update = threading.Thread(target=self.trackUpdate)
        track_update.start()

    def trackUpdate(self):
        playback = self.sp_caller.getTrackInfo()
        last_id = playback['item']['id']
        while 1:
            playback = self.sp_caller.getTrackInfo()
            track_id = playback['item']['id']

            if track_id != last_id:
                last_id = track_id

                for widget in updateTrack:
                    exec('self.' + widget + f'.updateTrack({playback}, (255, 255, 255))')

                self.changeBackground()

            for widget in updatePlayback:
                exec('self.' + widget + f'.updatePlayback({playback})')

    def widgetsUpdate(self):
        for widget in updateWidget:
            exec('self.' + widget + f'.updateWidget((255, 255, 255))')

    def changeBackground(self):
        if self.backgroundColorFixed:
            backgroundColor = str(tuple(self.backgroundColor))
        else:
            backgroundColor = str(sqrt_algorithm(Image.open('albumImg.jpg')))
        print(f'background-color: {backgroundColor}')
        self.centralwidget.setStyleSheet(f'background-color: rgb{backgroundColor}')
