from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect

import json


class Widget(QLabel):
    def init(self, playback, background):
        self.confiInit()

        self.setObjectName(u"progressTime")
        self.setGeometry(
            QRect(self.trackSliderPosition[0] - int(self.trackProgressSize * 1.8) - self.trackProgressPosition[0],
                  self.trackSliderPosition[1] - self.trackProgressPosition[1],
                  int(self.trackProgressSize * 1.8), self.trackProgressSize * 0.9))
        self.setStyleSheet(f"font-size: {self.trackProgressSize}px")

    def updateTrack(self, playback, background):
        pass

    def updatePlayback(self, playback):
        pass

    def updateWidget(self, background):
        self.setGeometry(
            QRect(self.trackSliderPosition[0] - int(self.trackProgressSize * 1.8) - self.trackProgressPosition[0],
                  self.trackSliderPosition[1] - self.trackProgressPosition[1],
                  int(self.trackProgressSize * 1.8), self.trackProgressSize * 0.9))
        self.setStyleSheet(f"font-size: {self.trackProgressSize}px")

    def confiInit(self):
        with open(r"addons/trackProgress/config.json") as configFile:
            self.config = json.load(configFile)
        self.trackProgressSize = self.config["trackProgressSize"]
        self.trackProgressPosition = self.config["trackProgressPosition"]
        self.trackProgressColor1 = self.config["trackProgressColor1"]
        self.trackProgressColorFixed = self.config["trackProgressColorFixed"]
        self.trackProgressColorThreshold = self.config["trackProgressColorThreshold"]
        self.trackProgressColorThresholdMode = self.config["trackProgressColorThresholdMode"]
        self.trackProgressColor2 = self.config["trackProgressColor2"]
        with open(r"addons/trackSlider/config.json") as configFile:
            self.config = json.load(configFile)
        self.trackSliderPosition = self.config["trackSliderPosition"]
