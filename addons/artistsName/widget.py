from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect, Qt

import json


class Widget(QLabel):
    def init(self, playback, background):
        self.configInit()

        artists_name = ", ".join(artist["name"] for artist in playback["item"]["artists"])

        self.setObjectName(u"artists")
        if self.trackNameMode == "left":
            self.setGeometry(QRect(QRect(0, *self.nameArtistsPosition, int(1.35 * self.nameArtistsSize))))
        else:
            self.setGeometry(QRect(*self.nameArtistsPosition, 1000, int(1.35 * self.nameArtistsSize)))

        self.setText(artists_name)

        if self.config['trackNameMode'] == 'left':
            self.setAlignment(Qt.AlignRight)
        else:
            self.setAlignment(Qt.AlignLeft)

    def updateTrack(self, playback, background):
        artists_name = ", ".join(artist["name"] for artist in playback["item"]["artists"])

        self.setText(artists_name)

        if self.config['trackNameMode'] == 'left':
            self.setAlignment(Qt.AlignRight)
        else:
            self.setAlignment(Qt.AlignLeft)

    def updateWidget(self, background):
        self.configInit()

        self.setObjectName(u"artists")
        if self.trackNameMode == "left":
            self.setGeometry(QRect(QRect(0, *self.nameArtistsPosition, int(1.35 * self.nameArtistsSize))))
        else:
            self.setGeometry(QRect(*self.nameArtistsPosition, 1000, int(1.35 * self.nameArtistsSize)))

    def configInit(self):
        with open(r"config.json") as configFile:
            self.config = json.load(configFile)
        self.albumImageSize = self.config["albumImageSize"]
        self.albumImageMarginLeft = self.config["albumImageMarginLeft"]
        self.albumImageMarginUp = self.config["albumImageMarginUp"]
        self.trackNameMode = self.config["trackNameMode"]
        self.trackNameSize = self.config["trackNameSize"]
        self.trackNamePosition = self.config["trackNamePosition"]
        self.nameArtistsMode = self.config["nameArtistsMode"]
        self.nameArtistsSize = self.config["nameArtistsSize"]
        nameArtistMargin = self.config["nameArtistsMargin"]
        self.nameArtistsColor1 = self.config["nameArtistsColor1"]
        self.nameArtistsColorFixed = self.config["nameArtistsColorFixed"]
        self.nameArtistsColorThreshold = self.config["nameArtistsColorThreshold"]
        self.nameArtistsColorThresholdMode = self.config["nameArtistsColorThresholdMode"]
        self.nameArtistsColor2 = self.config["nameArtistsColor2"]

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

        if self.trackNameMode == "right":
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] - int(
                                                 self.nameArtistsSize * 1.35) - nameArtistMargin),
            elif self.nameArtistsMode == "down":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] + int(
                                                 1.35 * self.trackNameSize) + nameArtistMargin),
        elif self.config['trackNameMode'] == "left":
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0] - int(
                                                 self.nameArtistsSize * 1.35) - nameArtistMargin,
                                             self.trackNamePosition[1]),
            elif self.nameArtistsMode == "down":
                print(self.trackNamePosition)
                self.nameArtistsPosition = *(self.trackNamePosition[0] + int(
                                                 1.35 * self.trackNameSize) + nameArtistMargin,
                                             self.trackNamePosition[1]),
        elif self.trackNameMode == "down":
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] - int(
                                                 self.nameArtistsSize * 1.35) - nameArtistMargin),
            elif self.nameArtistsMode == "down":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] + int(
                                                 1.35 * self.trackNameSize) + nameArtistMargin),
        elif self.trackNameMode == "up":
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] - int(
                                                 self.nameArtistsSize * 1.35) - nameArtistMargin),
            elif self.nameArtistsMode == "down":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] + int(
                                                 1.35 * self.trackNameSize) + nameArtistMargin),
