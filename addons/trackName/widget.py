from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect, Qt

import json


class Widget(QLabel):
    def init(self, playback, background):
        self.operator_to_func = {
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '==': lambda a, b: a == b
        }
        self.configInit()

        track_name = playback["item"]["name"]

        self.setObjectName(u"trackName")
        if self.trackNameMode == "left":
            self.setGeometry(QRect(0, *self.trackNamePosition, 1000))
        else:
            self.setGeometry(QRect(*self.trackNamePosition, 1000, int(1.35 * self.trackNameSize)))

        if self.operator_to_func[self.trackNameColorThresholdMode](
                sorted(background), sorted(self.trackNameColorThreshold)) and not self.trackNameColorFixed:
            self.setStyleSheet(f"color: rgba{str(tuple(self.trackNameColor2))}; font-size: {self.trackNameSize}px")
        else:
            self.setStyleSheet(f"color: rgba{str(tuple(self.trackNameColor1))}; font-size: {self.trackNameSize}px")

        self.setText(track_name)

        if self.trackNameMode == 'left':
            self.setAlignment(Qt.AlignRight)
        else:
            self.setAlignment(Qt.AlignLeft)

    def updateTrack(self, playback, background):
        track_name = playback["item"]["name"]

        self.setText(track_name)

        if self.trackNameMode == 'left':
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

        if self.operator_to_func[self.trackNameColorThresholdMode](
                sorted(background), sorted(self.trackNameColorThreshold)) and not self.trackNameColorFixed:
            self.setStyleSheet(f"color: rgba{str(tuple(self.trackNameColor2))}; font-size: {self.trackNameSize}px")
        else:
            self.setStyleSheet(f"color: rgba{str(tuple(self.trackNameColor1))}; font-size: {self.trackNameSize}px")

    def configInit(self):
        with open(r"addons/trackName/config.json", 'r', encoding='utf-8') as configFile:
            self.config = json.load(configFile)
        self.trackNameMode = self.config["trackNameMode"]
        self.trackNameSize = self.config["trackNameSize"]
        self.trackNameColor1 = self.config["trackNameColor1"]
        self.trackNameColorFixed = self.config["trackNameColorFixed"]
        self.trackNameColorThreshold = self.config["trackNameColorThreshold"]
        self.trackNameColorThresholdMode = self.config["trackNameColorThresholdMode"]
        self.trackNameColor2 = self.config["trackNameColor2"]
        self.trackNamePosition = self.config["trackNamePosition"]
        with open(r"addons/albumImage/config.json", 'r', encoding='utf-8') as configFile:
            self.config = json.load(configFile)
        self.albumImageSize = self.config["albumImageSize"]
        self.albumImagePosition = self.config["albumImagePosition"]

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
