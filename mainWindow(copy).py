import json

from PIL import Image

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt, QObject, QThread, QEvent)
from PySide6.QtGui import (QPixmap, QRegion)
from PySide6.QtWidgets import (QLabel, QWidget, QSlider, QDialog, QMainWindow)
from parametersConfig import Ui_Dialog

from domColor import sqrt_algorithm


class Ui_MainWindow(object):
    def __init__(self):
        self.newWindow = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.newWindow)

    def initializteUi(self, MainWindow):
        self.operator_to_func = {
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '==': lambda a, b: a == b
        }
        with open(r"config.json") as configFile:
            self.config = json.load(configFile)
        self.backgroungColorFixed = self.config["backgroundColorFixed"]
        self.backgroundColor = self.config["backgroundColor"]
        self.albumImageSize = self.config["albumImageSize"]
        self.albumImageRadius = self.config["albumImageRadius"]
        self.albumImageMarginLeft = self.config["albumImageMarginLeft"]
        self.albumImageMarginUp = self.config["albumImageMarginUp"]
        self.trackNameMode = self.config["trackNameMode"]
        self.trackNameSize = self.config["trackNameSize"]
        self.trackNameColor1 = self.config["trackNameColor1"]
        self.trackNameColorFixed = self.config["trackNameColorFixed"]
        self.trackNameColorThreshold = self.config["trackNameColorThreshold"]
        self.trackNameColorThresholdMode = self.config["trackNameColorThresholdMode"]
        self.trackNameColor2 = self.config["trackNameColor2"]
        self.trackNamePosition = self.config["trackNamePosition"]
        self.nameArtistsMode = self.config["nameArtistsMode"]
        self.nameArtistsSize = self.config["nameArtistsSize"]
        nameArtistMargin = self.config["nameArtistsMargin"]
        self.nameArtistsColor1 = self.config["nameArtistsColor1"]
        self.nameArtistsColorFixed = self.config["nameArtistsColorFixed"]
        self.nameArtistsColorThreshold = self.config["nameArtistsColorThreshold"]
        self.nameArtistsColorThresholdMode = self.config["nameArtistsColorThresholdMode"]
        self.nameArtistsColor2 = self.config["nameArtistsColor2"]
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
        self.trackProgressSize = self.config["trackProgressSize"]
        self.trackProgressMarginX = self.config["trackProgressMarginX"]
        self.trackProgressMarginY = self.config["trackProgressMarginY"]
        self.trackProgressColor1 = self.config["trackProgressColor1"]
        self.trackProgressColorFixed = self.config["trackProgressColorFixed"]
        self.trackProgressColorThreshold = self.config["trackProgressColorThreshold"]
        self.trackProgressColorThresholdMode = self.config["trackProgressColorThresholdMode"]
        self.trackProgressColor2 = self.config["trackProgressColor2"]
        self.trackDurationSize = self.config["trackDurationSize"]
        self.trackDurationMarginX = self.config["trackDurationMarginX"]
        self.trackDurationMarginY = self.config["trackDurationMarginY"]
        self.trackDurationColor1 = self.config["trackDurationColor1"]
        self.trackDurationColorFixed = self.config["trackDurationColorFixed"]
        self.trackDurationColorThreshold = self.config["trackDurationColorThreshold"]
        self.trackDurationColorThresholdMode = self.config["trackDurationColorThresholdMode"]
        self.trackDurationColor2 = self.config["trackDurationColor2"]

        if self.trackNameMode == "right":
            self.trackNamePosition = *(self.albumImageMarginLeft + self.albumImageSize + self.trackNamePosition[0],
                                       self.albumImageMarginUp + self.albumImageSize - self.trackNameSize -
                                       self.trackNamePosition[1]),
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] - int(
                                                 self.nameArtistsSize * 1.35) - nameArtistMargin),
            elif self.nameArtistsMode == "down":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] + int(
                                                 1.35 * self.trackNameSize) + nameArtistMargin),
        elif self.config['trackNameMode'] == "left":
            self.trackNamePosition = *(
            self.albumImageMarginUp + self.albumImageSize - self.trackNameSize - self.trackNamePosition[1],
            self.albumImageMarginLeft - self.trackNamePosition[0]),
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
            self.trackNamePosition = *(self.albumImageMarginLeft - self.trackNamePosition[0],
                                       self.albumImageMarginUp + self.albumImageSize + self.trackNamePosition[1]),
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] - int(
                                                 self.nameArtistsSize * 1.35) - nameArtistMargin),
            elif self.nameArtistsMode == "down":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] + int(
                                                 1.35 * self.trackNameSize) + nameArtistMargin),
        elif self.trackNameMode == "up":
            self.trackNamePosition = *(self.albumImageMarginLeft + self.trackNamePosition[0],
                                       self.albumImageMarginUp - self.trackNamePosition[1]),
            if self.nameArtistsMode == "up":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] - int(
                                                 self.nameArtistsSize * 1.35) - nameArtistMargin),
            elif self.nameArtistsMode == "down":
                self.nameArtistsPosition = *(self.trackNamePosition[0],
                                             self.trackNamePosition[1] + int(
                                                 1.35 * self.trackNameSize) + nameArtistMargin),

        if self.backgroungColorFixed:
            backgroundColor = self.backgroundColor
            MainWindow.setStyleSheet(f"background-color: rgb{str(tuple(self.backgroundColor))};")
        else:
            backgroundColor = str(sqrt_algorithm(Image.open(r'albumImg.jpg')))
            MainWindow.setStyleSheet(f"background-color: rgb{backgroundColor};")
            backgroundColor = list(sqrt_algorithm(Image.open(r'albumImg.jpg')))
        print(backgroundColor)

        if self.operator_to_func[self.trackNameColorThresholdMode](sorted(backgroundColor), sorted(self.trackNameColorThreshold)) and not self.trackNameColorFixed:
            self.trackName.setStyleSheet(f"color: rgb{str(tuple(self.trackNameColor2))}; font-size: {self.trackNameSize}px")
        else:
            self.trackName.setStyleSheet(f"color: rgb{str(tuple(self.trackNameColor1))}; font-size: {self.trackNameSize}px")
        if self.operator_to_func[self.nameArtistsColorThresholdMode](sorted(backgroundColor), sorted(self.nameArtistsColorThreshold)) and not self.nameArtistsColorFixed:
            self.artists.setStyleSheet(f"color: rgba{str(tuple(self.nameArtistsColor2))}; font-size: {self.nameArtistsSize}px")
        else:
            self.artists.setStyleSheet(f"color: rgba{str(tuple(self.nameArtistsColor1))}; font-size: {self.nameArtistsSize}px")
        if self.operator_to_func[self.trackProgressColorThresholdMode](sorted(backgroundColor), sorted(self.trackProgressColorThreshold)) and not self.trackProgressColorFixed:
            self.progressTime.setStyleSheet(f"color: rgba{str(tuple(self.trackProgressColor2))}; font-size: {self.trackProgressSize}px")
        else:
            self.progressTime.setStyleSheet(f"color: rgba{str(tuple(self.trackProgressColor1))}; font-size: {self.trackProgressSize}px")
        if self.operator_to_func[self.trackDurationColorThresholdMode](sorted(backgroundColor), sorted(self.trackDurationColorThreshold)) and not self.trackDurationColorFixed:
            self.durationTime.setStyleSheet(f"color: rgba{str(tuple(self.trackDurationColor2))}; font-size: {self.trackDurationSize}px")
        else:
            self.durationTime.setStyleSheet(f"color: rgba{str(tuple(self.trackDurationColor1))}; font-size: {self.trackDurationSize}px")
        if self.operator_to_func[self.trackSliderAdd_pageColorThresholdMode](sorted(backgroundColor), sorted(self.trackSliderAdd_pageColorThreshold)) and not self.trackSliderAdd_pageColorFixed:
            sliderAdd_pageColor = self.trackSliderAdd_pageColor2
        else:
            sliderAdd_pageColor = self.trackSliderAdd_pageColor1
        if self.operator_to_func[self.trackSliderSub_pageColorThresholdMode](sorted(backgroundColor), sorted(self.trackSliderSub_pageColorThreshold)) and not self.trackSliderSub_pageColorFixed:
            sliderSub_pageColor = self.trackSliderSub_pageColor2
        else:
            sliderSub_pageColor = self.trackSliderSub_pageColor1
        if self.operator_to_func[self.trackSliderHandleColorThresholdMode](sorted(backgroundColor), sorted(self.trackSliderHandleColorThreshold)) and not self.trackSliderHandleColorFixed:
            sliderHandleColor = self.trackSliderHandleColor2
        else:
            sliderHandleColor = self.trackSliderHandleColor1


        self.trackSlider.setStyleSheet(f"""
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


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.albumImage = QLabel(self.centralwidget)
        self.trackName = QLabel(self.centralwidget)
        self.artists = QLabel(self.centralwidget)
        self.trackSlider = QSlider(Qt.Horizontal, self.centralwidget)
        self.progressTime = QLabel(self.centralwidget)
        self.durationTime = QLabel(self.centralwidget)
        self.initializteUi(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

        self.updateUi(MainWindow)

    def updateUi(self, MainWindow):
        self.initializteUi(MainWindow)
        self.albumImage.setObjectName(u"albumImage")
        self.albumImage.setGeometry(QRect(self.albumImageMarginLeft, self.albumImageMarginUp, self.albumImageSize, self.albumImageSize))
        self.borderRadiusAlbumImage(self.albumImageRadius)

        self.trackName.setObjectName(u"trackName")
        self.artists.setObjectName(u"artists")
        self.trackSlider.setObjectName(u"trackSlider")
        self.progressTime.setObjectName(u"progressTime")
        self.durationTime.setObjectName(u"durationTime")

        if self.trackNameMode == "left":
            self.trackName.setGeometry(QRect(0, *self.trackNamePosition, 1000))

            self.artists.setGeometry(QRect(QRect(0, *self.nameArtistsPosition, int(1.35 * self.nameArtistsSize))))
        else:
            self.trackName.setGeometry(QRect(*self.trackNamePosition, 1000, int(1.35 * self.trackNameSize)))

            self.artists.setGeometry(QRect(*self.nameArtistsPosition, 1000, int(1.35 * self.nameArtistsSize)))
        self.trackSlider.setGeometry(QRect(self.trackSliderMarginLeft, self.trackSliderMarginUp, self.trackSliderSizeX, self.trackSliderHandleSizeY + 15))
        self.progressTime.setGeometry(
            QRect(self.trackSliderMarginLeft - int(self.trackProgressSize * 1.8) - self.trackProgressMarginX,
                  self.trackSliderMarginUp - self.trackProgressMarginY,
                  int(self.trackProgressSize * 1.8), self.trackProgressSize * 0.9))
        self.durationTime.setGeometry(
            QRect(self.trackSliderMarginLeft + self.trackSliderSizeX + self.trackDurationMarginX,
                  self.trackSliderMarginUp - self.trackDurationMarginY,
                  int(self.trackDurationSize * 1.8), self.trackDurationSize * 0.9))

        self.progressTime.setStyleSheet(f"font-size: {self.trackProgressSize}px")
        self.durationTime.setStyleSheet(f"font-size: {self.trackDurationSize}px")

        if self.config["trackNameMode"] == 'left':
            self.trackName.setAlignment(Qt.AlignRight)
            self.artists.setAlignment(Qt.AlignRight)
        else:
            self.trackName.setAlignment(Qt.AlignLeft)
            self.artists.setAlignment(Qt.AlignLeft)

        self.albumImage.setText("")
        self.albumImage.setPixmap(QPixmap(r'albumImg.jpg'))


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

        self.albumImage.setMask(circle1Region + circle2Region + circle3Region + circle4Region + rect1Region + rect2Region)

    def updateProgressBar(self, progress, duration):
        if type(progress) == int:
            self.trackSlider.setMaximum(duration)
            self.trackSlider.setValue(progress)

            self.progressTime.setText(str(progress // 60) + ':' +
                                      ('0' if len(str(int(progress % 60))) == 1 else '') +
                                      str(progress % 60))
            self.durationTime.setText(str(duration // 60) + ':' +
                                  ('0' if len(str(duration % 60)) == 1 else '') +
                                  str(duration % 60))
        else:
            self.trackSlider.setValue(0)
            self.progressTime.setText(progress)
            self.durationTime.setText(duration)

    def retranslateUi(self, MainWindow, trackName, artists):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        if self.backgroungColorFixed:
            backgroundColor = self.backgroundColor
            MainWindow.setStyleSheet(f"background-color: rgb{str(tuple(self.backgroundColor))};")
        else:
            backgroundColor = str(sqrt_algorithm(Image.open(r'albumImg.jpg')))
            MainWindow.setStyleSheet(f"background-color: rgb{backgroundColor};")
            backgroundColor = list(sqrt_algorithm(Image.open(r'albumImg.jpg')))

        if self.operator_to_func[self.trackNameColorThresholdMode](sorted(backgroundColor), sorted(self.trackNameColorThreshold)) and not self.trackNameColorFixed:
            self.trackName.setStyleSheet(f"color: rgb{str(tuple(self.trackNameColor2))}; font-size: {self.trackNameSize}px")
        else:
            self.trackName.setStyleSheet(f"color: rgb{str(tuple(self.trackNameColor1))}; font-size: {self.trackNameSize}px")
        if self.operator_to_func[self.nameArtistsColorThresholdMode](sorted(backgroundColor), sorted(self.nameArtistsColorThreshold)) and not self.nameArtistsColorFixed:
            self.artists.setStyleSheet(f"color: rgba{str(tuple(self.nameArtistsColor2))}; font-size: {self.nameArtistsSize}px")
        else:
            self.artists.setStyleSheet(f"color: rgba{str(tuple(self.nameArtistsColor1))}; font-size: {self.nameArtistsSize}px")
        if self.operator_to_func[self.trackProgressColorThresholdMode](sorted(backgroundColor), sorted(self.trackProgressColorThreshold)) and not self.trackProgressColorFixed:
            self.progressTime.setStyleSheet(f"color: rgba{str(tuple(self.trackProgressColor2))}; font-size: {self.trackProgressSize}px")
        else:
            self.progressTime.setStyleSheet(f"color: rgba{str(tuple(self.trackProgressColor1))}; font-size: {self.trackProgressSize}px")
        if self.operator_to_func[self.trackDurationColorThresholdMode](sorted(backgroundColor), sorted(self.trackDurationColorThreshold)) and not self.trackDurationColorFixed:
            self.durationTime.setStyleSheet(f"color: rgba{str(tuple(self.trackDurationColor2))}; font-size: {self.trackDurationSize}px")
        else:
            self.durationTime.setStyleSheet(f"color: rgba{str(tuple(self.trackDurationColor1))}; font-size: {self.trackDurationSize}px")
        if self.operator_to_func[self.trackSliderAdd_pageColorThresholdMode](sorted(backgroundColor), sorted(self.trackSliderAdd_pageColorThreshold)) and not self.trackSliderAdd_pageColorFixed:
            sliderAdd_pageColor = self.trackSliderAdd_pageColor2
        else:
            sliderAdd_pageColor = self.trackSliderAdd_pageColor1
        if self.operator_to_func[self.trackSliderSub_pageColorThresholdMode](sorted(backgroundColor), sorted(self.trackSliderSub_pageColorThreshold)) and not self.trackSliderSub_pageColorFixed:
            sliderSub_pageColor = self.trackSliderSub_pageColor2
        else:
            sliderSub_pageColor = self.trackSliderSub_pageColor1
        if self.operator_to_func[self.trackSliderHandleColorThresholdMode](sorted(backgroundColor), sorted(self.trackSliderHandleColorThreshold)) and not self.trackSliderHandleColorFixed:
            sliderHandleColor = self.trackSliderHandleColor2
        else:
            sliderHandleColor = self.trackSliderHandleColor1


        self.trackSlider.setStyleSheet(f"""
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

        self.trackName.setText(trackName)
        self.artists.setText(artists)

        if self.config['trackNameMode'] == 'left':
            self.trackName.setAlignment(Qt.AlignRight)
            self.artists.setAlignment(Qt.AlignRight)
        else:
            self.trackName.setAlignment(Qt.AlignLeft)
            self.artists.setAlignment(Qt.AlignLeft)

        self.albumImage.setPixmap(QPixmap(r'albumImg.jpg'))
