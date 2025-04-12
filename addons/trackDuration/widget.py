from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect

import json


class TrackDuration(QLabel):
    def init(self, playback, background):
        self.configInit()

        self.setObjectName(u'durationTime')
        self.setGeometry(
            QRect(self.trackSliderMarginLeft + self.trackSliderSizeX + self.trackDurationMarginX,
                  self.trackSliderMarginUp - self.trackDurationMarginY,
                  int(self.trackDurationSize * 1.8), self.trackDurationSize * 0.9))
        self.setStyleSheet(f"font-size: {self.trackDurationSize}px")


    def updateTrack(self, playback, background):
        pass

    def updateWidget(self, background):
        self.setObjectName(u'durationTime')
        self.setGeometry(
            QRect(self.trackSliderMarginLeft + self.trackSliderSizeX + self.trackDurationMarginX,
                  self.trackSliderMarginUp - self.trackDurationMarginY,
                  int(self.trackDurationSize * 1.8), self.trackDurationSize * 0.9))
        self.setStyleSheet(f"font-size: {self.trackDurationSize}px")

    def configInit(self):
        with open(r"config.json") as configFile:
            self.config = json.load(configFile)

        self.trackDurationSize = self.config["trackDurationSize"]
        self.trackDurationMarginX = self.config["trackDurationMarginX"]
        self.trackDurationMarginY = self.config["trackDurationMarginY"]
        self.trackDurationColor1 = self.config["trackDurationColor1"]
        self.trackDurationColorFixed = self.config["trackDurationColorFixed"]
        self.trackDurationColorThreshold = self.config["trackDurationColorThreshold"]
        self.trackDurationColorThresholdMode = self.config["trackDurationColorThresholdMode"]
        self.trackDurationColor2 = self.config["trackDurationColor2"]
        self.trackSliderSizeX = self.config["trackSliderSizeX"]
        self.trackSliderMarginLeft = self.config["trackSliderMarginLeft"]
        self.trackSliderMarginUp = self.config["trackSliderMarginUp"]
