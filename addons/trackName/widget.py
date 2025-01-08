from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect, Qt

import json


class Widget(QLabel):
    def init(self, playback, background):
        self.configInit()

        track_name = playback["item"]["name"]

        self.setObjectName(u"trackName")
        if self.trackNameMode == "left":
            self.setGeometry(QRect(0, *self.trackNamePosition, 1000))
        else:
            self.setGeometry(QRect(*self.trackNamePosition, 1000, int(1.35 * self.trackNameSize)))


        self.setText(track_name)

        if self.trackNameMode == 'left':
            self.setAlignment(Qt.AlignRight)
        else:
            self.setAlignment(Qt.AlignLeft)

    def updateTrack(self, playback, background):
        track_name = playback["item"]["name"]

        self.setText(track_name)

        if self.config['trackNameMode'] == 'left':
            self.setAlignment(Qt.AlignRight)
        else:
            self.setAlignment(Qt.AlignLeft)

    def updateWidget(self, background):
        self.configInit()

        self.setObjectName(u"trackName")
        if self.trackNameMode == "left":
            self.setGeometry(QRect(0, *self.trackNamePosition, 1000))
        else:
            self.setGeometry(QRect(*self.trackNamePosition, 1000, int(1.35 * self.trackNameSize)))

    def configInit(self):
        with open(r"config.json") as configFile:
            self.config = json.load(configFile)
        self.trackNameMode = self.config["trackNameMode"]
        self.trackNameSize = self.config["trackNameSize"]
        self.trackNameColor1 = self.config["trackNameColor1"]
        self.trackNameColorFixed = self.config["trackNameColorFixed"]
        self.trackNameColorThreshold = self.config["trackNameColorThreshold"]
        self.trackNameColorThresholdMode = self.config["trackNameColorThresholdMode"]
        self.trackNameColor2 = self.config["trackNameColor2"]
        self.trackNamePosition = self.config["trackNamePosition"]
        self.albumImageSize = self.config["albumImageSize"]
        self.albumImageMarginLeft = self.config["albumImageMarginLeft"]
        self.albumImageMarginUp = self.config["albumImageMarginUp"]

        if self.trackNameMode == "right":
            self.trackNamePosition = *(
                self.albumImageMarginLeft + self.albumImageSize + self.trackNamePosition[0],self.albumImageMarginUp +
                self.albumImageSize - self.trackNameSize -self.trackNamePosition[1]),
        elif self.config['trackNameMode'] == "left":
            self.trackNamePosition = *(
                self.albumImageMarginUp + self.albumImageSize - self.trackNameSize - self.trackNamePosition[1],
                self.albumImageMarginLeft - self.trackNamePosition[0]),
        elif self.trackNameMode == "down":
            self.trackNamePosition = *(self.albumImageMarginLeft - self.trackNamePosition[0],
                                       self.albumImageMarginUp + self.albumImageSize + self.trackNamePosition[1]),
        elif self.trackNameMode == "up":
            self.trackNamePosition = *(self.albumImageMarginLeft + self.trackNamePosition[0],
                                       self.albumImageMarginUp - self.trackNamePosition[1]),
