import threading
import json
import time
import os

import callToSpotifyAPI
from markdownToHtml import markdownToHtml

from PySide6.QtGui import Qt

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QObject, QEvent
from mainWindow import Ui_MainWindow
from parametersConfig import Ui_Dialog

class MainWindow(QMainWindow):
    def setDocumentation(self, file):
        self.uiNewWindow.element_documentation.setHtml(markdownToHtml(file))

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.newWindow = QDialog()
        self.uiNewWindow = Ui_Dialog()
        self.uiNewWindow.setupUi(self.newWindow)

        self.initializeConfigWindow()

        self.uiNewWindow.fixedColorBackgroundCheckBox.clicked.connect(lambda: self.enableChangeBackgroundColor())
        self.uiNewWindow.fixedColorTrackNameCheckBox.clicked.connect(lambda: self.enableChangeTrackNameColor2())
        self.uiNewWindow.fixedColorArtistsCheckBox.clicked.connect(lambda: self.enableChangeNameArtistsColor2())
        self.uiNewWindow.fixedColorProgrsbarAddCheckBox.clicked.connect(lambda: self.enableChangeProgressbarAddColor2())
        self.uiNewWindow.fixedColorProgresbarSubCheckBox.clicked.connect(lambda: self.enableChangeProgressbarSubColor2())
        self.uiNewWindow.fixedColorProgresbarHandlerCheckBox.clicked.connect(lambda: self.enableChangeProgressbarHandlerColor2())
        self.uiNewWindow.fixedColorProgressCheckBox.clicked.connect(lambda: self.enableChangeProgressColor2())
        self.uiNewWindow.fixedColorDurationCheckBox.clicked.connect(lambda: self.enableChangeDurationColor2())

        self.uiNewWindow.background.clicked.connect(lambda: self.setDocumentation('documentation\\background.md'))
        self.uiNewWindow.fixedColorBackground.clicked.connect(lambda: self.setDocumentation('documentation\\backgroundFixed_Parameter.md'))
        self.uiNewWindow.fixedColorBackgroundCheckBox.clicked.connect(lambda: self.setDocumentation('documentation\\backgroundFixed_Parameter.md'))
        self.uiNewWindow.backgroundColor.clicked.connect(lambda: self.setDocumentation('documentation\\backgroundColor_Parameter.md'))
        self.uiNewWindow.backgroundR.clicked.connect(lambda: self.setDocumentation('documentation\\backgroundColor_Parameter.md'))
        self.uiNewWindow.backgroundG.clicked.connect(lambda: self.setDocumentation('documentation\\backgroundColor_Parameter.md'))
        self.uiNewWindow.backgroundB.clicked.connect(lambda: self.setDocumentation('documentation\\backgroundColor_Parameter.md'))
        self.uiNewWindow.albumImg.clicked.connect(lambda: self.setDocumentation('documentation\\albumImg.md'))
        self.uiNewWindow.albumImgSize.clicked.connect(lambda: self.setDocumentation('documentation\\albumImgSize_Parameter.md'))
        self.uiNewWindow.albumImgSizePx.clicked.connect(lambda: self.setDocumentation('documentation\\albumImgSize_Parameter.md'))
        self.uiNewWindow.albumImgRadius.clicked.connect(lambda: self.setDocumentation('documentation\\albumImgRadius_Parameter.md'))
        self.uiNewWindow.albumImgRadiusPx.clicked.connect(lambda: self.setDocumentation('documentation\\albumImgRadius_Parameter.md'))
        self.uiNewWindow.albumImgPosition.clicked.connect(lambda: self.setDocumentation('documentation\\albumImgPosition_Parameter.md'))
        self.uiNewWindow.albumImgPositionX.clicked.connect(lambda: self.setDocumentation('documentation\\albumImgPosition_Parameter.md'))
        self.uiNewWindow.albumImgPositionY.clicked.connect(lambda: self.setDocumentation('documentation\\albumImgPosition_Parameter.md'))
        self.uiNewWindow.trackName.clicked.connect(lambda: self.setDocumentation('documentation\\trackName.md'))
        self.uiNewWindow.trackNameMode.clicked.connect(lambda: self.setDocumentation('documentation\\trackNameMode_Parameter.md'))
        self.uiNewWindow.trackNameModeComboBox.textActivated.connect(lambda: self.setDocumentation('documentation\\trackNameMode_Parameter.md'))
        self.uiNewWindow.trackNameSize.clicked.connect(lambda: self.setDocumentation('documentation\\trackNameSize_Parameter.md'))
        self.uiNewWindow.trackNameSizePx.clicked.connect(lambda: self.setDocumentation('documentation\\trackNameSize_Parameter.md'))
        self.uiNewWindow.trackNamePosition.clicked.connect(lambda: self.setDocumentation('documentation\\trackNamePosition_Parameter.md'))
        self.uiNewWindow.trackNamePositionX.clicked.connect(lambda: self.setDocumentation('documentation\\trackNamePosition_Parameter.md'))
        self.uiNewWindow.trackNameColor.clicked.connect(lambda: self.setDocumentation('documentation\\color.md'))
        self.uiNewWindow.trackNameColor1.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1R.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1G.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1B.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1A.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.fixedColorTrackName.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.fixedColorTrackNameCheckBox.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.trackNameThreshold.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.trackNameThresholdR.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.trackNameThresholdG.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.trackNameThresholdB.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.trackNameThresholdMode.clicked.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.trackNameThresholdModeComboBox.textActivated.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.trackNameColor2.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.trackNameColor2R.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.trackNameColor2G.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.trackNameColor2B.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.trackNameColor2A.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.artists.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.artistsMode.clicked.connect(lambda: self.setDocumentation('documentation/artistsMode_Parameter.md'))
        self.uiNewWindow.artistsModeComboBox.activated.connect(lambda: self.setDocumentation('documentation/artistsMode_Parameter.md'))
        self.uiNewWindow.artistsSize.clicked.connect(lambda: self.setDocumentation('documentation/artistsSize_Parameter.md'))
        self.uiNewWindow.artistsSizePx.clicked.connect(lambda: self.setDocumentation('documentation/artistsSize_Parameter.md'))
        self.uiNewWindow.artistsPosition.clicked.connect(lambda: self.setDocumentation('documentation/artistsMargin_Parameter.md'))
        self.uiNewWindow.artistsPositionPx.clicked.connect(lambda: self.setDocumentation('documentation/artistsMargin_Parameter.md'))
        self.uiNewWindow.artistsColor.clicked.connect(lambda: self.setDocumentation('documentation\\color.md'))
        self.uiNewWindow.trackNameColor1.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1R.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1G.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1B.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1A.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.fixedColorTrackName.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.fixedColorTrackNameCheckBox.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.artistsThreshold.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.artistsThresholdR.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.artistsThresholdG.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.artistsThresholdB.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.artistsThresholdMode.clicked.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.artistsThresholdModeComboBox.textActivated.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.artistsColor2.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.artistsColor2R.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.artistsColor2G.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.artistsColor2B.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.artistsColor2A.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progressbar.clicked.connect(lambda: self.setDocumentation('documentation/progressbar.md'))
        self.uiNewWindow.progressbarSize.clicked.connect(lambda: self.setDocumentation('documentation/progressbarSize_Parameter.md'))
        self.uiNewWindow.progressbarSizeX.clicked.connect(lambda: self.setDocumentation('documentation/progressbarSize_Parameter.md'))
        self.uiNewWindow.progressbarSizeY.clicked.connect(lambda: self.setDocumentation('documentation/progressbarSize_Parameter.md'))
        self.uiNewWindow.progresbarRadius.clicked.connect(lambda: self.setDocumentation('documentation/progressbarRadius_Parameter.md'))
        self.uiNewWindow.progresbarRadiusPx.clicked.connect(lambda: self.setDocumentation('documentation/progressbarRadius_Parameter.md'))
        self.uiNewWindow.progresbarPosition.clicked.connect(lambda: self.setDocumentation('documentation/progressbarPosition_Parameter.md'))
        self.uiNewWindow.progresbarPositionX.clicked.connect(lambda: self.setDocumentation('documentation/progressbarPosition_Parameter.md'))
        self.uiNewWindow.progresbarPositionY.clicked.connect(lambda: self.setDocumentation('documentation/progressbarPosition_Parameter.md'))
        self.uiNewWindow.progresbarAddColor.clicked.connect(lambda: self.setDocumentation('documentation\\color.md'))
        self.uiNewWindow.progresbarAddColor1.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progressbarAddColor1R.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progressbarAddColor1G.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progressbarAddColor1B.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1A.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.fixedColorProgrsbarAdd.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.fixedColorProgrsbarAddCheckBox.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.progressbarAddThreshold.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarAddThresholdR.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarAddThresholdG.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarAddThresholdB.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarAddThresholdMode.clicked.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.progresbarAddThresholdModeComboBox.textActivated.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.progresbarAddColor2.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarAddColor2R.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarAddColor2G.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarAddColor2B.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarAddColor2A.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarSubColor.clicked.connect(lambda: self.setDocumentation('documentation\\color.md'))
        self.uiNewWindow.progresbarSubColor1.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progressbarSubColor1R.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progressbarSubColor1G.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progressbarSubColor1B.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1A.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.fixedColorProgresbarSub.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.fixedColorProgresbarSubCheckBox.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.progresbarSubThreshold.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarSubThresholdR.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarSubThresholdG.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarSubThresholdB.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarSubThresholdMode.clicked.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.progresbarSubThresholdModeComboBox.textActivated.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.progresbarSubColor2.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarSubColor2R.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarSubColor2G.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarSubColor2B.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarSubColor2A.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarHandlerLabel.clicked.connect(lambda: self.setDocumentation('documentation\\progressbarHandler.md'))
        self.uiNewWindow.progresbarHandlerSize.clicked.connect(lambda: self.setDocumentation('documentation\\progressbarHandlerSize_Parameter.md'))
        self.uiNewWindow.progresbarHandlerSizeX.clicked.connect(lambda: self.setDocumentation('documentation\\progressbarHandlerSize_Parameter.md'))
        self.uiNewWindow.progresbarHandlerSizeY.clicked.connect(lambda: self.setDocumentation('documentation\\progressbarHandlerSize_Parameter.md'))
        self.uiNewWindow.progresbarHandlerRadius.clicked.connect(lambda: self.setDocumentation('documentation\\progressbarHandlerRadius_Parameter.md'))
        self.uiNewWindow.progresbarHandlerRadiusPx.clicked.connect(lambda: self.setDocumentation('documentation\\progressbarHandlerRadius_Parameter.md'))
        self.uiNewWindow.progresbarHandlerColor.clicked.connect(lambda: self.setDocumentation('documentation\\color.md'))
        self.uiNewWindow.progresbarHandlerColor1.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progresbarHandlerColor1R.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progresbarHandlerColor1G.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progresbarHandlerColor1B.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1A.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.fixedColorProgresbarHandler.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.fixedColorProgresbarHandlerCheckBox.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.progresbarHandlerThreshold.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarHandlerThresholdR.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarHandlerThresholdG.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarHandlerThresholdB.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progresbarHandlerThresholdMode.clicked.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.progresbarHandlerThresholdModeComboBox.textActivated.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.progresbarHandlerColor2.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarHandlerColor2R.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarHandlerColor2G.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarHandlerColor2B.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progresbarHandlerColor2A.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progress.clicked.connect(lambda: self.setDocumentation('documentation\\trackProgress.md'))
        self.uiNewWindow.progressSze.clicked.connect(lambda: self.setDocumentation('documentation\\trackProgressSize_Parameter.md'))
        self.uiNewWindow.progressSizePx.clicked.connect(lambda: self.setDocumentation('documentation\\trackProgressSize_Parameter.md'))
        self.uiNewWindow.progressPosition.clicked.connect(lambda: self.setDocumentation('documentation\\trackProgressPosition_Parameter.md'))
        self.uiNewWindow.progressPositionX.clicked.connect(lambda: self.setDocumentation('documentation\\trackProgressPosition_Parameter.md'))
        self.uiNewWindow.progressPositionY.clicked.connect(lambda: self.setDocumentation('documentation\\trackProgressPosition_Parameter.md'))
        self.uiNewWindow.progressColor.clicked.connect(lambda: self.setDocumentation('documentation\\color.md'))
        self.uiNewWindow.progressColor1.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progressColor1R.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progressColor1G.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.progressColor1B.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1A.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.fixedColorProgress.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.fixedColorProgressCheckBox.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.progressThreshold.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progressThresholdR.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progressThresholdG.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progressThresholdB.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.progressThresholdMode.clicked.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.progressThresholdModeComboBox.textActivated.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.progressColor2.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progressColor2R.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progressColor2G.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progressColor2B.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.progressColor2A.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.duration.clicked.connect(lambda: self.setDocumentation('documentation\\trackDuration.md'))
        self.uiNewWindow.durationSize.clicked.connect(lambda: self.setDocumentation('documentation\\trackDurationSize_Parameter.md'))
        self.uiNewWindow.durationSizePx.clicked.connect(lambda: self.setDocumentation('documentation\\trackDurationSize_Parameter.md'))
        self.uiNewWindow.durationPosition.clicked.connect(lambda: self.setDocumentation('documentation\\trackDurationPosition_Parameter.md'))
        self.uiNewWindow.durationPositionX.clicked.connect(lambda: self.setDocumentation('documentation\\trackDurationPosition_Parameter.md'))
        self.uiNewWindow.durationPositionY.clicked.connect(lambda: self.setDocumentation('documentation\\trackDurationPosition_Parameter.md'))
        self.uiNewWindow.durationColor.clicked.connect(lambda: self.setDocumentation('documentation\\color.md'))
        self.uiNewWindow.durationColor1.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.durationColor1R.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.durationColor1G.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.durationColor1B.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.trackNameColor1A.clicked.connect(lambda: self.setDocumentation('documentation\\color1_Parameter.md'))
        self.uiNewWindow.fixedColorDuration.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.fixedColorDurationCheckBox.clicked.connect(lambda: self.setDocumentation('documentation\\fixedColor_Parameter.md'))
        self.uiNewWindow.durationThreshold.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.durationThresholdR.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.durationThresholdG.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.durationThresholdB.clicked.connect(lambda: self.setDocumentation('documentation\\colorThreshold_Parameter.md'))
        self.uiNewWindow.durationThresholdMode.clicked.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.durationThresholdModeComboBox.textActivated.connect(lambda: self.setDocumentation('documentation\\colorThresholdMode_Parameter.md'))
        self.uiNewWindow.durationColor2.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.durationColor2R.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.durationColor2G.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.durationColor2B.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))
        self.uiNewWindow.durationColor2A.clicked.connect(lambda: self.setDocumentation('documentation\\color2_Parameter.md'))


        self.uiNewWindow.apply.clicked.connect(lambda: self.applyButton())
        self.uiNewWindow.ok.clicked.connect(lambda: self.okButton())
        self.uiNewWindow.cancel.clicked.connect(lambda: self.cancelButton())

    def readConfig(self):
        with open(r"config.json") as configFile:
            self.config = json.load(configFile)
        self.backgroundColorFixed = self.config["backgroundColorFixed"]
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
        self.nameArtistsMargin = self.config["nameArtistsMargin"]
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

    def initializeConfigWindow(self):
        self.readConfig()

        self.uiNewWindow.fixedColorBackgroundCheckBox.setChecked(self.backgroundColorFixed)
        if self.backgroundColorFixed:
            self.uiNewWindow.backgroundR.setEnabled(False)
            self.uiNewWindow.backgroundG.setEnabled(False)
            self.uiNewWindow.backgroundB.setEnabled(False)
        self.uiNewWindow.backgroundR.setText(str(self.backgroundColor[0]))
        self.uiNewWindow.backgroundG.setText(str(self.backgroundColor[1]))
        self.uiNewWindow.backgroundB.setText(str(self.backgroundColor[2]))

        self.uiNewWindow.albumImgSizePx.setText(str(self.albumImageSize))
        self.uiNewWindow.albumImgRadiusPx.setText(str(self.albumImageRadius))
        self.uiNewWindow.albumImgPositionX.setText(str(self.albumImageMarginLeft))
        self.uiNewWindow.albumImgPositionY.setText(str(self.albumImageMarginUp))

        mode = self.uiNewWindow.trackNameModeComboBox.findText(self.trackNameMode)
        self.uiNewWindow.trackNameModeComboBox.setCurrentIndex(mode)
        self.uiNewWindow.trackNameSizePx.setText(str(self.trackNameSize))
        self.uiNewWindow.trackNamePositionX.setText(str(self.trackNamePosition[0]))
        self.uiNewWindow.trackNamePositionY.setText(str(self.trackNamePosition[1]))
        self.uiNewWindow.trackNameColor1R.setText(str(self.trackNameColor1[0]))
        self.uiNewWindow.trackNameColor1G.setText(str(self.trackNameColor1[1]))
        self.uiNewWindow.trackNameColor1B.setText(str(self.trackNameColor1[2]))
        self.uiNewWindow.trackNameColor1A.setText(str(self.trackNameColor1[3]))
        self.uiNewWindow.fixedColorTrackNameCheckBox.setChecked(self.trackNameColorFixed)
        if self.trackNameColorFixed:
            self.uiNewWindow.trackNameColor2R.setEnabled(False)
            self.uiNewWindow.trackNameColor2G.setEnabled(False)
            self.uiNewWindow.trackNameColor2B.setEnabled(False)
            self.uiNewWindow.trackNameColor2A.setEnabled(False)
            self.uiNewWindow.trackNameThresholdR.setEnabled(False)
            self.uiNewWindow.trackNameThresholdG.setEnabled(False)
            self.uiNewWindow.trackNameThresholdB.setEnabled(False)
            self.uiNewWindow.trackNameThresholdModeComboBox.setEnabled(False)
        self.uiNewWindow.trackNameThresholdR.setText(str(self.trackNameColorThreshold[0]))
        self.uiNewWindow.trackNameThresholdG.setText(str(self.trackNameColorThreshold[1]))
        self.uiNewWindow.trackNameThresholdB.setText(str(self.trackNameColorThreshold[2]))
        mode = self.uiNewWindow.trackNameThresholdModeComboBox.findText(self.trackNameColorThresholdMode)
        self.uiNewWindow.trackNameThresholdModeComboBox.setCurrentIndex(mode)
        self.uiNewWindow.trackNameColor2R.setText(str(self.trackNameColor1[0]))
        self.uiNewWindow.trackNameColor2G.setText(str(self.trackNameColor1[1]))
        self.uiNewWindow.trackNameColor2B.setText(str(self.trackNameColor1[2]))
        self.uiNewWindow.trackNameColor2A.setText(str(self.trackNameColor1[3]))

        mode = self.uiNewWindow.artistsModeComboBox.findText(self.nameArtistsMode)
        self.uiNewWindow.artistsModeComboBox.setCurrentIndex(mode)
        self.uiNewWindow.artistsSizePx.setText(str(self.nameArtistsSize))
        self.uiNewWindow.artistsPositionPx.setText(str(self.nameArtistsMargin))
        self.uiNewWindow.artistsColor1R.setText(str(self.nameArtistsColor1[0]))
        self.uiNewWindow.artistsColor1G.setText(str(self.nameArtistsColor1[1]))
        self.uiNewWindow.artistsColor1B.setText(str(self.nameArtistsColor1[2]))
        self.uiNewWindow.artistsColor1A.setText(str(self.nameArtistsColor1[3]))
        self.uiNewWindow.fixedColorArtistsCheckBox.setChecked(self.nameArtistsColorFixed)
        if self.nameArtistsColorFixed:
            self.uiNewWindow.artistsColor2R.setEnabled(False)
            self.uiNewWindow.artistsColor2G.setEnabled(False)
            self.uiNewWindow.artistsColor2B.setEnabled(False)
            self.uiNewWindow.artistsColor2A.setEnabled(False)
            self.uiNewWindow.artistsThresholdR.setEnabled(False)
            self.uiNewWindow.artistsThresholdG.setEnabled(False)
            self.uiNewWindow.artistsThresholdB.setEnabled(False)
            self.uiNewWindow.artistsThresholdModeComboBox.setEnabled(False)
        self.uiNewWindow.artistsThresholdR.setText(str(self.nameArtistsColorThreshold[0]))
        self.uiNewWindow.artistsThresholdG.setText(str(self.nameArtistsColorThreshold[1]))
        self.uiNewWindow.artistsThresholdB.setText(str(self.nameArtistsColorThreshold[2]))
        mode = self.uiNewWindow.artistsThresholdModeComboBox.findText(self.nameArtistsColorThresholdMode)
        self.uiNewWindow.artistsThresholdModeComboBox.setCurrentIndex(mode)
        self.uiNewWindow.artistsColor2R.setText(str(self.nameArtistsColor1[0]))
        self.uiNewWindow.artistsColor2G.setText(str(self.nameArtistsColor1[1]))
        self.uiNewWindow.artistsColor2B.setText(str(self.nameArtistsColor1[2]))
        self.uiNewWindow.artistsColor2A.setText(str(self.nameArtistsColor1[3]))

        self.uiNewWindow.progressbarSizeX.setText(str(self.trackSliderSizeX))
        self.uiNewWindow.progressbarSizeY.setText(str(self.trackSliderSizeY))
        self.uiNewWindow.progresbarRadiusPx.setText(str(self.trackSliderRadius))
        self.uiNewWindow.progresbarPositionX.setText(str(self.trackSliderMarginLeft))
        self.uiNewWindow.progresbarPositionY.setText(str(self.trackSliderMarginUp))

        self.uiNewWindow.progressbarAddColor1R.setText(str(self.trackSliderAdd_pageColor1[0]))
        self.uiNewWindow.progressbarAddColor1G.setText(str(self.trackSliderAdd_pageColor1[1]))
        self.uiNewWindow.progressbarAddColor1B.setText(str(self.trackSliderAdd_pageColor1[2]))
        self.uiNewWindow.progressbarAddColor1A.setText(str(self.trackSliderAdd_pageColor1[3]))
        self.uiNewWindow.fixedColorProgrsbarAddCheckBox.setChecked(self.trackSliderAdd_pageColorFixed)
        if self.trackSliderAdd_pageColorFixed:
            self.uiNewWindow.progresbarAddColor2R.setEnabled(False)
            self.uiNewWindow.progresbarAddColor2G.setEnabled(False)
            self.uiNewWindow.progresbarAddColor2B.setEnabled(False)
            self.uiNewWindow.progresbarAddColor2A.setEnabled(False)
            self.uiNewWindow.progresbarAddThresholdR.setEnabled(False)
            self.uiNewWindow.progresbarAddThresholdG.setEnabled(False)
            self.uiNewWindow.progresbarAddThresholdB.setEnabled(False)
            self.uiNewWindow.progresbarAddThresholdModeComboBox.setEnabled(False)
        self.uiNewWindow.progresbarAddColor2R.setText((str(self.trackSliderAdd_pageColor2[0])))
        self.uiNewWindow.progresbarAddColor2G.setText((str(self.trackSliderAdd_pageColor2[1])))
        self.uiNewWindow.progresbarAddColor2B.setText((str(self.trackSliderAdd_pageColor2[2])))
        self.uiNewWindow.progresbarAddColor2A.setText((str(self.trackSliderAdd_pageColor2[3])))
        self.uiNewWindow.progresbarAddThresholdR.setText(str(self.trackSliderAdd_pageColorThreshold[0]))
        self.uiNewWindow.progresbarAddThresholdG.setText(str(self.trackSliderAdd_pageColorThreshold[1]))
        self.uiNewWindow.progresbarAddThresholdB.setText(str(self.trackSliderAdd_pageColorThreshold[2]))

        self.uiNewWindow.progressbarSubColor1R.setText(str(self.trackSliderSub_pageColor1[0]))
        self.uiNewWindow.progressbarSubColor1G.setText(str(self.trackSliderSub_pageColor1[1]))
        self.uiNewWindow.progressbarSubColor1B.setText(str(self.trackSliderSub_pageColor1[2]))
        self.uiNewWindow.progressbarSubColor1A.setText(str(self.trackSliderSub_pageColor1[3]))
        self.uiNewWindow.fixedColorProgresbarSubCheckBox.setChecked(self.trackSliderSub_pageColorFixed)
        if self.trackSliderSub_pageColorFixed:
            self.uiNewWindow.progresbarSubColor2R.setEnabled(False)
            self.uiNewWindow.progresbarSubColor2G.setEnabled(False)
            self.uiNewWindow.progresbarSubColor2B.setEnabled(False)
            self.uiNewWindow.progresbarSubColor2A.setEnabled(False)
            self.uiNewWindow.progresbarSubThresholdR.setEnabled(False)
            self.uiNewWindow.progresbarSubThresholdG.setEnabled(False)
            self.uiNewWindow.progresbarSubThresholdB.setEnabled(False)
            self.uiNewWindow.progresbarSubThresholdModeComboBox.setEnabled(False)
        self.uiNewWindow.progresbarSubColor2R.setText((str(self.trackSliderSub_pageColor2[0])))
        self.uiNewWindow.progresbarSubColor2G.setText((str(self.trackSliderSub_pageColor2[1])))
        self.uiNewWindow.progresbarSubColor2B.setText((str(self.trackSliderSub_pageColor2[2])))
        self.uiNewWindow.progresbarSubColor2A.setText((str(self.trackSliderSub_pageColor2[3])))
        self.uiNewWindow.progresbarSubThresholdR.setText(str(self.trackSliderSub_pageColorThreshold[0]))
        self.uiNewWindow.progresbarSubThresholdG.setText(str(self.trackSliderSub_pageColorThreshold[1]))
        self.uiNewWindow.progresbarSubThresholdB.setText(str(self.trackSliderSub_pageColorThreshold[2]))

        self.uiNewWindow.progresbarHandlerSizeX.setText(str(self.trackSliderHandleSizeX))
        self.uiNewWindow.progresbarHandlerSizeY.setText(str(self.trackSliderHandleSizeY))
        self.uiNewWindow.progresbarHandlerRadiusPx.setText(str(self.trackSliderHandleRadius))
        self.uiNewWindow.progresbarHandlerColor1R.setText(str(self.trackSliderSub_pageColor1[0]))
        self.uiNewWindow.progresbarHandlerColor1G.setText(str(self.trackSliderSub_pageColor1[1]))
        self.uiNewWindow.progresbarHandlerColor1B.setText(str(self.trackSliderSub_pageColor1[2]))
        self.uiNewWindow.progresbarHandlerColor1A.setText(str(self.trackSliderSub_pageColor1[3]))
        self.uiNewWindow.fixedColorProgresbarHandlerCheckBox.setChecked(self.trackSliderHandleColorFixed)
        if self.trackSliderSub_pageColorFixed:
            self.uiNewWindow.progresbarHandlerColor2R.setEnabled(False)
            self.uiNewWindow.progresbarHandlerColor2G.setEnabled(False)
            self.uiNewWindow.progresbarHandlerColor2B.setEnabled(False)
            self.uiNewWindow.progresbarHandlerColor2A.setEnabled(False)
            self.uiNewWindow.progresbarHandlerThresholdR.setEnabled(False)
            self.uiNewWindow.progresbarHandlerThresholdG.setEnabled(False)
            self.uiNewWindow.progresbarHandlerThresholdB.setEnabled(False)
            self.uiNewWindow.progresbarHandlerThresholdModeComboBox.setEnabled(False)
        self.uiNewWindow.progresbarHandlerColor2R.setText((str(self.trackSliderSub_pageColor2[0])))
        self.uiNewWindow.progresbarHandlerColor2G.setText((str(self.trackSliderSub_pageColor2[1])))
        self.uiNewWindow.progresbarHandlerColor2B.setText((str(self.trackSliderSub_pageColor2[2])))
        self.uiNewWindow.progresbarHandlerColor2A.setText((str(self.trackSliderSub_pageColor2[3])))
        self.uiNewWindow.progresbarHandlerThresholdR.setText(str(self.trackSliderSub_pageColorThreshold[0]))
        self.uiNewWindow.progresbarHandlerThresholdG.setText(str(self.trackSliderSub_pageColorThreshold[1]))
        self.uiNewWindow.progresbarHandlerThresholdB.setText(str(self.trackSliderSub_pageColorThreshold[2]))

        self.uiNewWindow.progressSizePx.setText(str(self.trackProgressSize))
        self.uiNewWindow.progressPositionX.setText(str(self.trackProgressMarginX))
        self.uiNewWindow.progressPositionY.setText(str(self.trackProgressMarginY))
        self.uiNewWindow.progressColor1R.setText(str(self.trackProgressColor1[0]))
        self.uiNewWindow.progressColor1G.setText(str(self.trackProgressColor1[1]))
        self.uiNewWindow.progressColor1B.setText(str(self.trackProgressColor1[2]))
        self.uiNewWindow.progressColor1A.setText(str(self.trackProgressColor1[3]))
        self.uiNewWindow.fixedColorProgressCheckBox.setChecked(self.trackProgressColorFixed)
        if self.trackProgressColorFixed:
            self.uiNewWindow.progressColor2R.setEnabled(False)
            self.uiNewWindow.progressColor2G.setEnabled(False)
            self.uiNewWindow.progressColor2B.setEnabled(False)
            self.uiNewWindow.progressColor2A.setEnabled(False)
            self.uiNewWindow.progressThresholdR.setEnabled(False)
            self.uiNewWindow.progressThresholdG.setEnabled(False)
            self.uiNewWindow.progressThresholdB.setEnabled(False)
            self.uiNewWindow.progressThresholdModeComboBox.setEnabled(False)
        self.uiNewWindow.progressColor2R.setText((str(self.trackProgressColor2[0])))
        self.uiNewWindow.progressColor2G.setText((str(self.trackProgressColor2[1])))
        self.uiNewWindow.progressColor2B.setText((str(self.trackProgressColor2[2])))
        self.uiNewWindow.progressColor2A.setText((str(self.trackProgressColor2[3])))
        self.uiNewWindow.progressThresholdR.setText(str(self.trackProgressColorThreshold[0]))
        self.uiNewWindow.progressThresholdG.setText(str(self.trackProgressColorThreshold[1]))
        self.uiNewWindow.progressThresholdB.setText(str(self.trackProgressColorThreshold[2]))

        self.uiNewWindow.durationSizePx.setText(str(self.trackDurationSize))
        self.uiNewWindow.durationPositionX.setText(str(self.trackDurationMarginX))
        self.uiNewWindow.durationPositionY.setText(str(self.trackDurationMarginY))
        self.uiNewWindow.durationColor1R.setText(str(self.trackDurationColor1[0]))
        self.uiNewWindow.durationColor1G.setText(str(self.trackDurationColor1[1]))
        self.uiNewWindow.durationColor1B.setText(str(self.trackDurationColor1[2]))
        self.uiNewWindow.durationColor1A.setText(str(self.trackDurationColor1[3]))
        self.uiNewWindow.fixedColorDurationCheckBox.setChecked(self.trackDurationColorFixed)
        if self.trackDurationColorFixed:
            self.uiNewWindow.durationColor2R.setEnabled(False)
            self.uiNewWindow.durationColor2G.setEnabled(False)
            self.uiNewWindow.durationColor2B.setEnabled(False)
            self.uiNewWindow.durationColor2A.setEnabled(False)
            self.uiNewWindow.durationThresholdR.setEnabled(False)
            self.uiNewWindow.durationThresholdG.setEnabled(False)
            self.uiNewWindow.durationThresholdB.setEnabled(False)
            self.uiNewWindow.durationThresholdModeComboBox.setEnabled(False)
        self.uiNewWindow.durationColor2R.setText((str(self.trackDurationColor2[0])))
        self.uiNewWindow.durationColor2G.setText((str(self.trackDurationColor2[1])))
        self.uiNewWindow.durationColor2B.setText((str(self.trackDurationColor2[2])))
        self.uiNewWindow.durationColor2A.setText((str(self.trackDurationColor2[3])))
        self.uiNewWindow.durationThresholdR.setText(str(self.trackDurationColorThreshold[0]))
        self.uiNewWindow.durationThresholdG.setText(str(self.trackDurationColorThreshold[1]))
        self.uiNewWindow.durationThresholdB.setText(str(self.trackDurationColorThreshold[2]))

    def enableChangeBackgroundColor(self):
        checked = self.uiNewWindow.fixedColorBackgroundCheckBox.isChecked()
        self.uiNewWindow.backgroundR.setEnabled(not checked)
        self.uiNewWindow.backgroundG.setEnabled(not checked)
        self.uiNewWindow.backgroundB.setEnabled(not checked)

    def enableChangeTrackNameColor2(self):
        checked = self.uiNewWindow.fixedColorTrackNameCheckBox.isChecked()
        self.uiNewWindow.trackNameColor2R.setEnabled(not checked)
        self.uiNewWindow.trackNameColor2G.setEnabled(not checked)
        self.uiNewWindow.trackNameColor2B.setEnabled(not checked)
        self.uiNewWindow.trackNameColor2A.setEnabled(not checked)
        self.uiNewWindow.trackNameThresholdR.setEnabled(not checked)
        self.uiNewWindow.trackNameThresholdG.setEnabled(not checked)
        self.uiNewWindow.trackNameThresholdB.setEnabled(not checked)
        self.uiNewWindow.trackNameThresholdModeComboBox.setEnabled(not checked)

    def enableChangeNameArtistsColor2(self):
        checked = self.uiNewWindow.fixedColorArtistsCheckBox.isChecked()
        self.uiNewWindow.artistsColor2R.setEnabled(not checked)
        self.uiNewWindow.artistsColor2G.setEnabled(not checked)
        self.uiNewWindow.artistsColor2B.setEnabled(not checked)
        self.uiNewWindow.artistsColor2A.setEnabled(not checked)
        self.uiNewWindow.artistsThresholdR.setEnabled(not checked)
        self.uiNewWindow.artistsThresholdG.setEnabled(not checked)
        self.uiNewWindow.artistsThresholdB.setEnabled(not checked)
        self.uiNewWindow.artistsThresholdModeComboBox.setEnabled(not checked)

    def enableChangeProgressbarAddColor2(self):
        checked = self.uiNewWindow.fixedColorProgrsbarAddCheckBox.isChecked()
        self.uiNewWindow.progresbarAddColor2R.setEnabled(not checked)
        self.uiNewWindow.progresbarAddColor2G.setEnabled(not checked)
        self.uiNewWindow.progresbarAddColor2B.setEnabled(not checked)
        self.uiNewWindow.progresbarAddColor2A.setEnabled(not checked)
        self.uiNewWindow.progresbarAddThresholdR.setEnabled(not checked)
        self.uiNewWindow.progresbarAddThresholdG.setEnabled(not checked)
        self.uiNewWindow.progresbarAddThresholdB.setEnabled(not checked)
        self.uiNewWindow.progresbarAddThresholdModeComboBox.setEnabled(not checked)

    def enableChangeProgressbarSubColor2(self):
        checked = self.uiNewWindow.fixedColorProgresbarSubCheckBox.isChecked()
        self.uiNewWindow.progresbarSubColor2R.setEnabled(not checked)
        self.uiNewWindow.progresbarSubColor2G.setEnabled(not checked)
        self.uiNewWindow.progresbarSubColor2B.setEnabled(not checked)
        self.uiNewWindow.progresbarSubColor2A.setEnabled(not checked)
        self.uiNewWindow.progresbarSubThresholdR.setEnabled(not checked)
        self.uiNewWindow.progresbarSubThresholdG.setEnabled(not checked)
        self.uiNewWindow.progresbarSubThresholdB.setEnabled(not checked)
        self.uiNewWindow.progresbarSubThresholdModeComboBox.setEnabled(not checked)

    def enableChangeProgressbarHandlerColor2(self):
        checked = self.uiNewWindow.fixedColorProgresbarHandlerCheckBox.isChecked()
        self.uiNewWindow.progresbarHandlerColor2R.setEnabled(not checked)
        self.uiNewWindow.progresbarHandlerColor2G.setEnabled(not checked)
        self.uiNewWindow.progresbarHandlerColor2B.setEnabled(not checked)
        self.uiNewWindow.progresbarHandlerColor2A.setEnabled(not checked)
        self.uiNewWindow.progresbarHandlerThresholdR.setEnabled(not checked)
        self.uiNewWindow.progresbarHandlerThresholdG.setEnabled(not checked)
        self.uiNewWindow.progresbarHandlerThresholdB.setEnabled(not checked)
        self.uiNewWindow.progresbarHandlerThresholdModeComboBox.setEnabled(not checked)

    def enableChangeProgressColor2(self):
        checked = self.uiNewWindow.fixedColorProgressCheckBox.isChecked()
        self.uiNewWindow.progressColor2R.setEnabled(not checked)
        self.uiNewWindow.progressColor2G.setEnabled(not checked)
        self.uiNewWindow.progressColor2B.setEnabled(not checked)
        self.uiNewWindow.progressColor2A.setEnabled(not checked)
        self.uiNewWindow.progressThresholdR.setEnabled(not checked)
        self.uiNewWindow.progressThresholdG.setEnabled(not checked)
        self.uiNewWindow.progressThresholdB.setEnabled(not checked)
        self.uiNewWindow.progressThresholdModeComboBox.setEnabled(not checked)

    def enableChangeDurationColor2(self):
        checked = self.uiNewWindow.fixedColorDurationCheckBox.isChecked()
        self.uiNewWindow.durationColor2R.setEnabled(not checked)
        self.uiNewWindow.durationColor2G.setEnabled(not checked)
        self.uiNewWindow.durationColor2B.setEnabled(not checked)
        self.uiNewWindow.durationColor2A.setEnabled(not checked)
        self.uiNewWindow.durationThresholdR.setEnabled(not checked)
        self.uiNewWindow.durationThresholdG.setEnabled(not checked)
        self.uiNewWindow.durationThresholdB.setEnabled(not checked)
        self.uiNewWindow.durationThresholdModeComboBox.setEnabled(not checked)

    def retranslateUi(self, trackName, artists):
        self.ui.retranslateUi(self, trackName, artists)

    def updateProgressBar(self, progress, duration):
        self.ui.updateProgressBar(progress, duration)

    def apply(self):
        self.config['backgroundColorFixed'] = self.uiNewWindow.fixedColorBackgroundCheckBox.isChecked()
        r = int(self.uiNewWindow.backgroundR.text())
        g = int(self.uiNewWindow.backgroundG.text())
        b = int(self.uiNewWindow.backgroundB.text())
        self.config['backgroundColor'] = [r, g, b]
        self.config['albumImageSize'] = int(self.uiNewWindow.albumImgSizePx.text())
        self.config['albumImageRadius'] = int(self.uiNewWindow.albumImgRadiusPx.text())
        self.config['albumImageMarginLeft'] = int(self.uiNewWindow.albumImgPositionX.text())
        self.config['albumImageMarginUp'] = int(self.uiNewWindow.albumImgPositionY.text())
        self.config['trackNameMode'] = self.uiNewWindow.trackNameModeComboBox.currentText()
        self.config['trackNameSize'] = int(self.uiNewWindow.trackNameSizePx.text())
        x = int(self.uiNewWindow.trackNamePositionX.text())
        y = int(self.uiNewWindow.trackNamePositionY.text())
        self.config['trackNamePosition'] = [x, y]
        r = int(self.uiNewWindow.trackNameColor1R.text())
        g = int(self.uiNewWindow.trackNameColor1G.text())
        b = int(self.uiNewWindow.trackNameColor1B.text())
        a = int(self.uiNewWindow.trackNameColor1A.text())
        self.config['trackNameColor1'] = [r, g, b, a]
        self.config['trackNameColorFixed'] = self.uiNewWindow.fixedColorTrackNameCheckBox.isChecked()
        self.config['trackNameColorThresholdMode'] = self.uiNewWindow.trackNameThresholdModeComboBox.currentText()
        r = int(self.uiNewWindow.trackNameColor2R.text())
        g = int(self.uiNewWindow.trackNameColor2G.text())
        b = int(self.uiNewWindow.trackNameColor2B.text())
        a = int(self.uiNewWindow.trackNameColor2A.text())
        self.config['trackNameColor2'] = [r, g, b, a]
        self.config['nameArtistsMode'] = self.uiNewWindow.artistsModeComboBox.currentText()
        self.config['nameArtistsSize'] = int(self.uiNewWindow.artistsSizePx.text())
        self.config['nameArtistsMargin'] = int(self.uiNewWindow.artistsPositionPx.text())
        r = int(self.uiNewWindow.artistsColor1R.text())
        g = int(self.uiNewWindow.artistsColor1G.text())
        b = int(self.uiNewWindow.artistsColor1B.text())
        a = int(self.uiNewWindow.artistsColor1A.text())
        self.config['nameArtistsColor1'] = [r, g, b, a]
        self.config['nameArtistsColorFixed'] = self.uiNewWindow.fixedColorArtistsCheckBox.isChecked()
        self.config['nameArtistsColorThresholdMode'] = self.uiNewWindow.artistsThresholdModeComboBox.currentText()
        r = int(self.uiNewWindow.artistsColor2R.text())
        g = int(self.uiNewWindow.artistsColor2G.text())
        b = int(self.uiNewWindow.artistsColor2B.text())
        a = int(self.uiNewWindow.artistsColor2A.text())
        self.config['nameArtistsColor2'] = [r, g, b, a]
        self.config['trackSliderSizeX'] = int(self.uiNewWindow.progressbarSizeX.text())
        self.config['trackSliderSizeY'] = int(self.uiNewWindow.progressbarSizeY.text())
        self.config['trackSliderMarginLeft'] = int(self.uiNewWindow.progresbarPositionX.text())
        self.config['trackSliderMarginUp'] = int(self.uiNewWindow.progresbarPositionY.text())
        self.config['trackSliderRadius'] = int(self.uiNewWindow.progresbarRadiusPx.text())
        r = int(self.uiNewWindow.progressbarAddColor1R.text())
        g = int(self.uiNewWindow.progressbarAddColor1G.text())
        b = int(self.uiNewWindow.progressbarAddColor1B.text())
        a = int(self.uiNewWindow.progressbarAddColor1A.text())
        self.config['trackSliderAdd-pageColor1'] = [r, g, b, a]
        self.config['trackSliderAdd-pageColorFixed'] = self.uiNewWindow.fixedColorProgrsbarAddCheckBox.isChecked()
        self.config['trackSliderAdd-pageColorThresholdMode'] = self.uiNewWindow.artistsThresholdModeComboBox.currentText()
        r = int(self.uiNewWindow.progresbarAddColor2R.text())
        g = int(self.uiNewWindow.progresbarAddColor2G.text())
        b = int(self.uiNewWindow.progresbarAddColor2B.text())
        a = int(self.uiNewWindow.progresbarAddColor2A.text())
        self.config['trackSliderAdd-pageColor2'] = [r, g, b, a]
        r = int(self.uiNewWindow.progressbarSubColor1R.text())
        g = int(self.uiNewWindow.progressbarSubColor1G.text())
        b = int(self.uiNewWindow.progressbarSubColor1B.text())
        a = int(self.uiNewWindow.progressbarSubColor1A.text())
        self.config['trackSliderSub-pageColor1'] = [r, g, b, a]
        self.config['trackSliderSub-pageColorFixed'] = self.uiNewWindow.fixedColorProgresbarSubCheckBox.isChecked()
        self.config['trackSliderSub-pageColorThresholdMode'] = self.uiNewWindow.artistsThresholdModeComboBox.currentText()
        r = int(self.uiNewWindow.progresbarSubColor2R.text())
        g = int(self.uiNewWindow.progresbarSubColor2G.text())
        b = int(self.uiNewWindow.progresbarSubColor2B.text())
        a = int(self.uiNewWindow.progresbarSubColor2A.text())
        self.config['trackSliderSub-pageColor2'] = [r, g, b, a]
        r = int(self.uiNewWindow.progresbarHandlerColor1R.text())
        g = int(self.uiNewWindow.progresbarHandlerColor1G.text())
        b = int(self.uiNewWindow.progresbarHandlerColor1B.text())
        a = int(self.uiNewWindow.progresbarHandlerColor1A.text())
        self.config['trackSliderHandleColor1'] = [r, g, b, a]
        self.config['trackSliderHandleColorFixed'] = self.uiNewWindow.fixedColorProgresbarHandlerCheckBox.isChecked()
        self.config['trackSliderHandleColorThresholdMode'] = self.uiNewWindow.artistsThresholdModeComboBox.currentText()
        r = int(self.uiNewWindow.progresbarHandlerColor2R.text())
        g = int(self.uiNewWindow.progresbarHandlerColor2G.text())
        b = int(self.uiNewWindow.progresbarHandlerColor2B.text())
        a = int(self.uiNewWindow.progresbarHandlerColor2A.text())
        self.config['trackSliderHandleColor2'] = [r, g, b, a]
        self.config['trackProgressSize'] = int(self.uiNewWindow.progressSizePx.text())
        self.config['trackProgressMarginX'] = int(self.uiNewWindow.progressPositionX.text())
        self.config['trackProgressMarginY'] = int(self.uiNewWindow.progressPositionY.text())
        r = int(self.uiNewWindow.progressColor1R.text())
        g = int(self.uiNewWindow.progressColor1G.text())
        b = int(self.uiNewWindow.progressColor1B.text())
        a = int(self.uiNewWindow.progressColor1A.text())
        self.config['trackProgressColor1'] = [r, g, b, a]
        self.config['trackProgressColorFixed'] = self.uiNewWindow.fixedColorProgressCheckBox.isChecked()
        self.config['trackProgressColorThresholdMode'] = self.uiNewWindow.artistsThresholdModeComboBox.currentText()
        r = int(self.uiNewWindow.progressColor2R.text())
        g = int(self.uiNewWindow.progressColor2G.text())
        b = int(self.uiNewWindow.progressColor2B.text())
        a = int(self.uiNewWindow.progressColor2A.text())
        self.config['trackProgressColor2'] = [r, g, b, a]
        self.config['trackDurationSize'] = int(self.uiNewWindow.progressSizePx.text())
        self.config['trackDurationMarginX'] = int(self.uiNewWindow.progressPositionX.text())
        self.config['trackDurationMarginY'] = int(self.uiNewWindow.progressPositionY.text())
        r = int(self.uiNewWindow.durationColor1R.text())
        g = int(self.uiNewWindow.durationColor1G.text())
        b = int(self.uiNewWindow.durationColor1B.text())
        a = int(self.uiNewWindow.durationColor1A.text())
        self.config['trackDurationColor1'] = [r, g, b, a]
        self.config['trackDurationColorFixed'] = self.uiNewWindow.fixedColorDurationCheckBox.isChecked()
        self.config['trackDurationColorThresholdMode'] = self.uiNewWindow.artistsThresholdModeComboBox.currentText()
        r = int(self.uiNewWindow.durationColor2R.text())
        g = int(self.uiNewWindow.durationColor2G.text())
        b = int(self.uiNewWindow.durationColor2B.text())
        a = int(self.uiNewWindow.durationColor2A.text())
        self.config['trackDurationColor2'] = [r, g, b, a]
        with open('config.json', 'w') as configFile:
            json.dump(self.config, configFile, indent=4)
        SpCaller.albumImageSize = self.config['albumImageSize']
        SpCaller.initMainWindow()

    def applyButton(self):
        self.apply()
        self.ui.updateUi(self)
        self.ui.initializteUi(self)

    def okButton(self):
        self.applyButton()
        self.newWindow.hide()
        del self.configCopy

    def cancelButton(self):
        with open('config.json', 'w') as configFile:
            json.dump(self.configCopy, configFile, indent=4)
        with open('config.json', 'r') as configFile:
            self.config = json.load(configFile)
        SpCaller.albumImageSize = self.config['albumImageSize']
        SpCaller.initMainWindow()
        self.ui.updateUi(self)
        self.newWindow.hide()
        del self.configCopy

    def keyPressEvent(self, event):
        if event.modifiers().name == 'ControlModifier|AltModifier' and event.text() == 'P':
            self.newWindow.show()
            self.configCopy = self.config.copy()

def updateTrack():
    window.retranslateUi(*SpCaller.initMainWindow())
    while True:
        window.retranslateUi(*SpCaller.getTrackUpdate())

def updateProgressBar():
    while True:
        window.updateProgressBar(*SpCaller.getProgressTrack())

def isInit():
    while True:
        time.sleep(5)
        if window.ui.trackName.text() == 'Ничего не воспроизводится':
            window.retranslateUi(*SpCaller.initMainWindow())


if __name__ == "__main__":
    SpCaller = callToSpotifyAPI.SpCaller()

    if not os.path.exists(r".cache"):
        SpCaller.initCache()

    app = QApplication([])
    window = MainWindow()
    window.showFullScreen()

    updateTrackThread = threading.Thread(target = updateTrack)
    updateProgressBarThread = threading.Thread(target = updateProgressBar)

    updateTrackThread.start()
    updateProgressBarThread.start()

    app.exec()
