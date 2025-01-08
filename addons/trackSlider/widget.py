from PySide6.QtWidgets import QProgressBar
from PySide6.QtCore import QRect

import json


class Widget(QProgressBar):
    def init(self, playback, background):
        self.configInit()

        self.setObjectName(u"trackSlider")
        self.setGeometry(QRect(self.trackSliderMarginLeft, self.trackSliderMarginUp, self.trackSliderSizeX,
                                           self.trackSliderHandleSizeY + 15))

    def updateTrack(self, playback, background):
        pass

    def updatePlayback(self, playback):
        pass

    def updateWidget(self, background):
        self.setGeometry(QRect(self.trackSliderMarginLeft, self.trackSliderMarginUp, self.trackSliderSizeX,
                               self.trackSliderHandleSizeY + 15))

    def configInit(self):
        with open(r"config.json") as configFile:
            self.config = json.load(configFile)
        self.trackSliderSizeX = self.config["trackSliderSizeX"]
        self.trackSliderSizeY = self.config["trackSliderSizeY"]
        self.trackSliderRadius = self.config["trackSliderRadius"]
        self.trackSliderAdd_pageColor1 = self.config["trackSliderAdd-pageColor1"]
        self.trackSliderAdd_pageColorFixed = self.config["trackSliderAdd-pageColorFixed"]
        self.trackSliderAdd_pageColorThreshold = self.config["trackSliderAdd-pageColorThreshold"]
        self.trackSliderAdd_pageColorThresholdMode = self.config["trackSliderAdd-pageColorThresholdMode"]
        self.trackSliderAdd_pageColor2 = self.config["trackSliderAdd-pageColor2"]
        self.trackSliderSub_pageColor1 = self.config["trackSliderSub-pageColor1"]
        self.trackSliderSub_pageColorFixed = self.config["trackSliderSub-pageColorFixed"]
        self.trackSliderSub_pageColorThreshold = self.config["trackSliderSub-pageColorThreshold"]
        self.trackSliderSub_pageColorThresholdMode = self.config["trackSliderSub-pageColorThresholdMode"]
        self.trackSliderSub_pageColor2 = self.config["trackSliderSub-pageColor2"]
        self.trackSliderMarginLeft = self.config["trackSliderMarginLeft"]
        self.trackSliderMarginUp = self.config["trackSliderMarginUp"]
        self.trackSliderHandleSizeX = self.config["trackSliderHandleSizeX"]
        self.trackSliderHandleSizeY = self.config["trackSliderHandleSizeY"]
        self.trackSliderHandleRadius = self.config["trackSliderHandleRadius"]
        self.trackSliderHandleColor1 = self.config["trackSliderHandleColor1"]
        self.trackSliderHandleColorFixed = self.config["trackSliderHandleColorFixed"]
        self.trackSliderHandleColorThreshold = self.config["trackSliderHandleColorThreshold"]
        self.trackSliderHandleColorThresholdMode = self.config["trackSliderHandleColorThresholdMode"]
        self.trackSliderHandleColor2 = self.config["trackSliderHandleColor2"]

