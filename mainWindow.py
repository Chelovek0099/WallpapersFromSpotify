import json
import requests
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
nonePlayback = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        with open('backgroundConfig.json', 'r') as backgroundConfig:
            self.backgroundConfig = json.load(backgroundConfig)
            self.backgroundColorFixed = self.backgroundConfig['backgroundColorFixed']
            self.backgroundColor = self.backgroundConfig['backgroundColor']
            self.backgroundColor_noneTrack = self.backgroundConfig['backgroundColor-NoneTrack']

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(0, 0, 10000, 10000)

        self.sp_caller = SpCaller()
        playback = self.sp_caller.getTrackInfo()

        for widget in widgets:
            exec('from addons.' + widget + '.widget import Widget')

            exec('self.' + widget + ' = Widget(self.centralwidget)')
            exec('self.' + widget + f'.init({playback})')

            if hasattr(eval('Widget'), 'updateTrack'):
                updateTrack.append(widget)
            if hasattr(eval('Widget'), 'updatePlayback'):
                updatePlayback.append(widget)
            if hasattr(eval('Widget'), 'updateWidget'):
                updateWidget.append(widget)
            if hasattr(eval('Widget'), 'nonePlayback'):
                nonePlayback.append(widget)

        track_update = threading.Thread(target=self.trackUpdate)
        track_update.start()
        self.none_track = threading.Thread(target = self.noneTrackThread)

    def trackUpdate(self):
        playback = self.sp_caller.getTrackInfo()
        none = False

        if playback == None:
            self.none_track.start()
            none = True
        else:
            last_id = playback['item']['id']

            background_update = threading.Thread(target=self.updateTrackThread, args=(playback, ))
            background_update.start()
        while 1:
            playback = self.sp_caller.getTrackInfo()

            if playback == None and not none:
                self.none_track.start()
                none = True
            elif not none:
                track_id = playback['item']['id']

                for widget in updatePlayback:
                    exec('self.' + widget + f'.updatePlayback({playback})')

                if track_id != last_id:
                    last_id = track_id

                    background_update = threading.Thread(target = self.updateTrackThread, args = (playback,))
                    background_update.start()
            else:
                none = False

    def widgetsUpdate(self):
        for widget in updateWidget:
            exec('self.' + widget + f'.updateWidget({self.currentBackgroundColor})')

    def changeBackground(self):
        if self.backgroundColorFixed:
            backgroundColor = str(tuple(self.backgroundColor))
        else:
            backgroundColor = str(sqrt_algorithm(Image.open('callback_resources/albumImg.jpg')))
        self.centralwidget.setStyleSheet(f'background-color: rgb{backgroundColor}')
        self.currentBackgroundColor = backgroundColor

    def updateTrackThread(self, playback):
        self.loadAlbumImage(playback)
        self.changeBackground()
        for widget in updateTrack:
            exec('self.' + widget + f'.updateTrack({playback}, {self.currentBackgroundColor})')

    def noneTrackThread(self):
        currentBackgroundColor = str(tuple(self.backgroundColor_noneTrack))
        self.centralwidget.setStyleSheet(f'background-color: rgb{currentBackgroundColor}')
        for widget in nonePlayback:
            exec('self.' + widget + f'.nonePlayback({currentBackgroundColor})')

    def loadAlbumImage(self, playback):
        self.opened = True
        try:
            resource = requests.get(playback["item"]["album"]["images"][1]["url"])
            with open('callback_resources/albumImg.jpg', 'wb') as img:
                img.write(resource.content)
        finally:
            pass
        self.opened = False
