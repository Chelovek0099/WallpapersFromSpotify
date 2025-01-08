from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap, QRegion

import json


class Widget(QLabel):
    def init(self, playback, background):
        self.configInit()

        self.setObjectName(u"albumImage")
        self.setGeometry(QRect(self.albumImageMarginLeft, self.albumImageMarginUp, self.albumImageSize, self.albumImageSize))
        self.borderRadiusAlbumImage(self.albumImageRadius)

        self.setText("")
        self.setPixmap(QPixmap(r'albumImg.jpg'))

    def updateTarck(self, playback, background):
        self.setPixmap(QPixmap(r'albumImg.jpg'))

    def updateWidget(self, background):
        self.configInit()

        self.setGeometry(QRect(self.albumImageMarginLeft, self.albumImageMarginUp, self.albumImageSize, self.albumImageSize))
        self.borderRadiusAlbumImage(self.albumImageRadius)

    def configInit(self):
        with open(r"config.json") as configFile:
            self.config = json.load(configFile)
        self.albumImageSize = self.config["albumImageSize"]
        self.albumImageRadius = self.config["albumImageRadius"]
        self.albumImageMarginLeft = self.config["albumImageMarginLeft"]
        self.albumImageMarginUp = self.config["albumImageMarginUp"]

    def borderRadiusAlbumImage(self, radius):
        circle1 = QRect(0, 0, radius, radius)
        circle2 = QRect(self.albumImageSize - radius, 0, radius, radius)
        circle3 = QRect(0, self.albumImageSize - radius, radius, radius)
        circle4 = QRect(self.albumImageSize - radius, self.albumImageSize - radius, radius, radius)

        circle1Region = QRegion(circle1, QRegion.Ellipse)
        circle2Region = QRegion(circle2, QRegion.Ellipse)
        circle3Region = QRegion(circle3, QRegion.Ellipse)
        circle4Region = QRegion(circle4, QRegion.Ellipse)
        rect1Region = QRegion(QRect(radius / 2, 0, self.albumImageSize - radius, self.albumImageSize))
        rect2Region = QRegion(QRect(0, radius / 2, self.albumImageSize, self.albumImageSize - radius))

        self.setMask(circle1Region + circle2Region + circle3Region + circle4Region + rect1Region + rect2Region)

    def hello(self):
        print("Hello from AlbumImage")
