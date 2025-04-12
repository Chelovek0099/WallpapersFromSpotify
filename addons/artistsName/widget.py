from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect, Qt

import json


class ArtistsName(QLabel):
    def init(self, playback):
        self.operator_to_func = {
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '==': lambda a, b: a == b
        }
        self.configInit()

        self.setObjectName(u"artists")
        if self.trackNameMode == "left":
            self.setGeometry(QRect(QRect(0, *self.nameArtistsPosition, int(1.35 * self.nameArtistsSize))))
            self.setAlignment(Qt.AlignRight)
        else:
            self.setGeometry(QRect(*self.nameArtistsPosition, 1000, int(1.35 * self.nameArtistsSize)))
            self.setAlignment(Qt.AlignLeft)


    def updateTrack(self, playback, background):
        artists_name = ", ".join(artist["name"] for artist in playback["item"]["artists"])

        if self.operator_to_func[self.nameArtistsColorThresholdMode](
                sorted(background), sorted(self.nameArtistsColorThreshold)) and not self.nameArtistsColorFixed:
            self.setStyleSheet(f"color: rgba{str(tuple(self.nameArtistsColor2))}; font-size: {self.nameArtistsSize}px")
        else:
            self.setStyleSheet(f"color: rgba{str(tuple(self.nameArtistsColor1))}; font-size: {self.nameArtistsSize}px")

        self.setText(artists_name)

        if self.config['trackNameMode'] == 'left':
            self.setAlignment(Qt.AlignRight)
        else:
            self.setAlignment(Qt.AlignLeft)

    def updateWidget(self, background):
        self.configInit()

        if self.operator_to_func[self.nameArtistsColorThresholdMode](
                sorted(background), sorted(self.nameArtistsColorThreshold)) and not self.nameArtistsColorFixed:
            self.setStyleSheet(f"color: rgba{str(tuple(self.nameArtistsColor2))}; font-size: {self.nameArtistsSize}px")
        else:
            self.setStyleSheet(f"color: rgba{str(tuple(self.nameArtistsColor1))}; font-size: {self.nameArtistsSize}px")

        if self.trackNameMode == "left":
            self.setGeometry(QRect(QRect(0, *self.nameArtistsPosition, int(1.35 * self.nameArtistsSize))))
            self.setAlignment(Qt.AlignRight)
        else:
            self.setGeometry(QRect(*self.nameArtistsPosition, 1000, int(1.35 * self.nameArtistsSize)))
            self.setAlignment(Qt.AlignLeft)

    def configInit(self):
        with open(r"addons/artistsName/config.json") as configFile:
            self.config = json.load(configFile)
        self.nameArtistsMode = self.config["nameArtistsMode"]
        self.nameArtistsSize = self.config["nameArtistsSize"]
        self.nameArtistMargin = self.config["nameArtistsMargin"]
        self.nameArtistsColor1 = self.config["nameArtistsColor1"]
        self.nameArtistsColorFixed = self.config["nameArtistsColorFixed"]
        self.nameArtistsColorThreshold = self.config["nameArtistsColorThreshold"]
        self.nameArtistsColorThresholdMode = self.config["nameArtistsColorThresholdMode"]
        self.nameArtistsColor2 = self.config["nameArtistsColor2"]
        with open(r"addons/albumImage/config.json") as configFile:
            self.config = json.load(configFile)
        self.albumImageSize = self.config["albumImageSize"]
        self.albumImagePosition = self.config["albumImagePosition"]
        with open(r"addons/trackName/config.json") as configFile:
            self.config = json.load(configFile)
        self.trackNameMode = self.config["trackNameMode"]
        self.trackNameSize = self.config["trackNameSize"]
        self.trackNamePosition = self.config["trackNamePosition"]

        if self.trackNameMode == "right":
            self.trackNamePosition = *(
                self.albumImagePosition[0] + self.albumImageSize + self.trackNamePosition[0],self.albumImagePosition[1] +
                self.albumImageSize - self.trackNameSize -self.trackNamePosition[1]),
        elif self.config['trackNameMode'] == "left":
            self.trackNamePosition = *(
                self.albumImagePosition[1] + self.albumImageSize - self.trackNameSize - self.trackNamePosition[1],
                self.albumImagePosition[0] - self.trackNamePosition[0]),
        elif self.trackNameMode == "down":
            self.trackNamePosition = *(self.albumImagePosition[0] - self.trackNamePosition[0],
                                       self.albumImagePosition[1] + self.albumImageSize + self.trackNamePosition[1]),
        elif self.trackNameMode == "up":
            self.trackNamePosition = *(self.albumImagePosition[0] + self.trackNamePosition[0],
                                       self.albumImagePosition[1] - self.trackNamePosition[1]),

        if self.trackNameMode == "right":
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] - int(
                                                 self.nameArtistsSize * 1.35) - self.nameArtistMargin),
            elif self.nameArtistsMode == "down":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] + int(
                                                 1.35 * self.trackNameSize) + self.nameArtistMargin),
        elif self.config['trackNameMode'] == "left":
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0] - int(
                                                 self.nameArtistsSize * 1.35) - self.nameArtistMargin,
                                             self.trackNamePosition[1]),
            elif self.nameArtistsMode == "down":
                print(self.trackNamePosition)
                self.nameArtistsPosition = *(self.trackNamePosition[0] + int(
                                                 1.35 * self.trackNameSize) + self.nameArtistMargin,
                                             self.trackNamePosition[1]),
        elif self.trackNameMode == "down":
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] - int(
                                                 self.nameArtistsSize * 1.35) - self.nameArtistMargin),
            elif self.nameArtistsMode == "down":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] + int(
                                                 1.35 * self.trackNameSize) + self.nameArtistMargin),
        elif self.trackNameMode == "up":
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] - int(
                                                 self.nameArtistsSize * 1.35) - self.nameArtistMargin),
            elif self.nameArtistsMode == "down":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] + int(
                                                 1.35 * self.trackNameSize) + self.nameArtistMargin),
