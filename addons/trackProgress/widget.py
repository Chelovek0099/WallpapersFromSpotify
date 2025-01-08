from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect

import json


class Widget(QLabel):
    def init(self, playback, background):
        self.confiInit()

        self.setObjectName(u"progressTime")
        self.setGeometry(
            QRect(self.trackSliderMarginLeft - int(self.trackProgressSize * 1.8) - self.trackProgressMarginX,
                  self.trackSliderMarginUp - self.trackProgressMarginY,
                  int(self.trackProgressSize * 1.8), self.trackProgressSize * 0.9))
        self.setStyleSheet(f"font-size: {self.trackProgressSize}px")

    def updateTrack(self, playback, background):
        pass

    def updatePlayback(self, playback):
        pass

    def updateWidget(self, background):
        self.setGeometry(
            QRect(self.trackSliderMarginLeft - int(self.trackProgressSize * 1.8) - self.trackProgressMarginX,
                  self.trackSliderMarginUp - self.trackProgressMarginY,
                  int(self.trackProgressSize * 1.8), self.trackProgressSize * 0.9))
        self.setStyleSheet(f"font-size: {self.trackProgressSize}px")

    def confiInit(self):
        with open(r"config.json") as configFile:
            self.config = json.load(configFile)
        self.trackProgressSize = self.config["trackProgressSize"]
        self.trackProgressMarginX = self.config["trackProgressMarginX"]
        self.trackProgressMarginY = self.config["trackProgressMarginY"]
        self.trackProgressColor1 = self.config["trackProgressColor1"]
        self.trackProgressColorFixed = self.config["trackProgressColorFixed"]
        self.trackProgressColorThreshold = self.config["trackProgressColorThreshold"]
        self.trackProgressColorThresholdMode = self.config["trackProgressColorThresholdMode"]
        self.trackProgressColor2 = self.config["trackProgressColor2"]
        self.trackSliderMarginLeft = self.config["trackSliderMarginLeft"]
        self.trackSliderMarginUp = self.config["trackSliderMarginUp"]
