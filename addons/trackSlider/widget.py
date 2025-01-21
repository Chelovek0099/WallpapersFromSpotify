import time

from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt
from PySide6.QtCore import QRect

import json


class Widget(QSlider):
    def __init__(self, parent):
        super().__init__(Qt.Horizontal, parent)

    def init(self, playback, background):
        self.operator_to_func = {
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '==': lambda a, b: a == b
        }
        self.configInit()

        self.setObjectName(u"trackSlider")
        self.setGeometry(QRect(self.trackSliderMarginLeft, self.trackSliderMarginUp, self.trackSliderSizeX,
                                           self.trackSliderHandleSizeY + 15))

        if self.operator_to_func[self.trackSliderAdd_pageColorThresholdMode](sorted(background), sorted(self.trackSliderAdd_pageColorThreshold)) and not self.trackSliderAdd_pageColorFixed:
            sliderAdd_pageColor = self.trackSliderAdd_pageColor2
        else:
            sliderAdd_pageColor = self.trackSliderAdd_pageColor1
        if self.operator_to_func[self.trackSliderSub_pageColorThresholdMode](sorted(background), sorted(self.trackSliderSub_pageColorThreshold)) and not self.trackSliderSub_pageColorFixed:
            sliderSub_pageColor = self.trackSliderSub_pageColor2
        else:
            sliderSub_pageColor = self.trackSliderSub_pageColor1
        if self.operator_to_func[self.trackSliderHandleColorThresholdMode](sorted(background), sorted(self.trackSliderHandleColorThreshold)) and not self.trackSliderHandleColorFixed:
            sliderHandleColor = self.trackSliderHandleColor2
        else:
            sliderHandleColor = self.trackSliderHandleColor1

        self.setStyleSheet(f"""
                QSlider::groove:horizontal {"{"}
                    border-radius: 1px; 
                    height: 7px;              
                    margin: -1px 0;           
                {"}"}
                QSlider::handle:horizontal {"{"}
                    background-color: rgba{str(tuple(sliderHandleColor))};
                    border: 1px solid rgba{str(tuple(sliderHandleColor))};    
                    width: {self.trackSliderHandleSizeX + 10}px;
                    margin: -2px 0;     
                    border-radius: {self.trackSliderHandleRadius}px;
                    padding: 0 {self.trackSliderHandleSizeY * (-1) + 1}px;
                {"}"}
                QSlider::add-page:horizontal {"{"}
                    border-radius: {self.trackSliderRadius}px;
                    background: rgba{str(tuple(sliderAdd_pageColor))};
                {"}"}
                QSlider::sub-page:horizontal {"{"}
                    border-radius: {self.trackSliderRadius}px;
                    background: rgba{str(tuple(sliderSub_pageColor))};
                {"}"}
        """)

    def updateTrack(self, playback, background):
        self.setMaximum(playback['item']['duration_ms']/1000)

        if self.operator_to_func[self.trackSliderAdd_pageColorThresholdMode](sorted(background), sorted(self.trackSliderAdd_pageColorThreshold)) and not self.trackSliderAdd_pageColorFixed:
            sliderAdd_pageColor = self.trackSliderAdd_pageColor2
        else:
            sliderAdd_pageColor = self.trackSliderAdd_pageColor1
        if self.operator_to_func[self.trackSliderSub_pageColorThresholdMode](sorted(background), sorted(self.trackSliderSub_pageColorThreshold)) and not self.trackSliderSub_pageColorFixed:
            sliderSub_pageColor = self.trackSliderSub_pageColor2
        else:
            sliderSub_pageColor = self.trackSliderSub_pageColor1
        if self.operator_to_func[self.trackSliderHandleColorThresholdMode](sorted(background), sorted(self.trackSliderHandleColorThreshold)) and not self.trackSliderHandleColorFixed:
            sliderHandleColor = self.trackSliderHandleColor2
        else:
            sliderHandleColor = self.trackSliderHandleColor1

        self.setStyleSheet(f"""
                        QSlider::groove:horizontal {"{"}
                            border-radius: 1px; 
                            height: 7px;              
                            margin: -1px 0;           
                        {"}"}
                        QSlider::handle:horizontal {"{"}
                            background-color: rgba{str(tuple(sliderHandleColor))};
                            border: 1px solid rgba{str(tuple(sliderHandleColor))};    
                            width: {self.trackSliderHandleSizeX + 10}px;
                            margin: -2px 0;     
                            border-radius: {self.trackSliderHandleRadius}px;
                            padding: 0 {self.trackSliderHandleSizeY * (-1) + 1}px;
                        {"}"}
                        QSlider::add-page:horizontal {"{"}
                            border-radius: {self.trackSliderRadius}px;
                            background: rgba{str(tuple(sliderAdd_pageColor))};
                        {"}"}
                        QSlider::sub-page:horizontal {"{"}
                            border-radius: {self.trackSliderRadius}px;
                            background: rgba{str(tuple(sliderSub_pageColor))};
                        {"}"}
                """)

    def updatePlayback(self, playback):
        self.setValue(playback["progress_ms"]/1000)

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

