import json
import os
import sys
import time

import requests
import threading

from PySide6.QtWidgets import QWidget, QLabel, QGraphicsBlurEffect
from PySide6.QtGui import QPixmap

from PIL import Image, ImageFilter
from spotipyHandler import SpCaller
from domColor import sqrt_algorithm

updateTrack = []
updatePlayback = []
updateWidget = []
nonePlayback = []


def capitalize(string):
    return string[0].upper() + string[1:]


class Ui_MainWindow(object):
    with open('enabledWidgets.json') as widgets_config:
        widgets = json.load(widgets_config)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(0, 0, 10000, 10000)

        with open('addons/background/config.json', 'r') as backgroundConfig:
            self.backgroundConfig = json.load(backgroundConfig)
            self.backgroundColorFixed = self.backgroundConfig['backgroundColorFixed']
            self.backgroundColor = self.backgroundConfig['backgroundColor']
            self.backgroundColor_noneTrack = self.backgroundConfig['backgroundColor-NoneTrack']

        self.backgroundBlur = QGraphicsBlurEffect()
        self.background = QLabel(self.centralwidget)
        self.background.setGeometry(-80, -420, 2000, 2000)
        self.background.setGraphicsEffect(self.backgroundBlur)

        if self.backgroundColorFixed:
            self.backgroundColor = str(tuple(self.backgroundColor))
        else:
            self.backgroundColor = str(sqrt_algorithm(Image.open('callback_resources/albumImg.jpg')))

        self.sp_caller = SpCaller()
        self.playback = self.sp_caller.getTrackInfo()

        for widget in self.widgets:
            self.addWidget(widget)
            time.sleep(0.1)

        track_update = threading.Thread(target=self.trackUpdate)
        track_update.start()

    def addWidget(self, widget):
        class_name = capitalize(widget)
        exec(f'from addons.{widget}.widget import {class_name}')

        exec(f'self.{widget} = {class_name}(self.centralwidget)')
        exec(f'self.{widget}.show()')
        exec(f'self.{widget}.init({self.playback})')
        time.sleep(0.1)
        exec(f'self.{widget}.updateTrack({self.playback}, {self.backgroundColor})')

        if hasattr(eval(class_name), 'updateTrack'):
            updateTrack.append(widget)
        if hasattr(eval(class_name), 'updatePlayback'):
            updatePlayback.append(widget)
        if hasattr(eval(class_name), 'updateWidget'):
            updateWidget.append(widget)
        if hasattr(eval(class_name), 'nonePlayback'):
            nonePlayback.append(widget)

        exec(f'del {class_name}')

    def deleteWidget(self, widget):
        exec(f'self.{widget}.hide()')
        exec(f'self.{widget}.stop()')
        exec(f'del self.{widget}')

        if widget in updateTrack:
            updateTrack.remove(widget)
        if widget in updatePlayback:
            updatePlayback.remove(widget)
        if widget in updateWidget:
            updateWidget.remove(widget)
        if widget in nonePlayback:
            nonePlayback.remove(widget)

    def trackUpdate(self):
        playback = self.sp_caller.getTrackInfo()
        none = False

        if playback is not None:
            last_id = playback['item']['id']

            background_update = threading.Thread(target=self.updateTrackThread, args=(playback, ))
            background_update.start()
        while 1:
            playback = self.sp_caller.getTrackInfo()

            if playback is None and not none:
                threading.Thread(target = self.noneTrackThread).start()
                none = True
            elif not none:
                track_id = playback['item']['id']

                for widget in updatePlayback:
                    exec('self.' + widget + f'.updatePlayback({playback})')
                    time.sleep(0.1)

                if track_id != last_id:
                    last_id = track_id

                    background_update = threading.Thread(target = self.updateTrackThread, args = (playback,))
                    background_update.start()
            elif playback is not None and none:
                none = False

    def widgetsUpdate(self):
        self.changeBackground()
        for widget in updateWidget:
            exec('self.' + widget + f'.updateWidget({self.currentBackgroundColor})')
            time.sleep(0.1)

    def changeBackground(self):
        with open('addons/background/config.json', 'r') as backgroundConfig:
            self.backgroundConfig = json.load(backgroundConfig)
            self.backgroundMode = self.backgroundConfig['backgroundMode']
            self.backgroundBlurStrength = self.backgroundConfig['backgroundBlur']
            self.backgroundColorFixed = self.backgroundConfig['backgroundColorFixed']
            self.backgroundColor = self.backgroundConfig['backgroundColor']
            self.backgroundColor_noneTrack = self.backgroundConfig['backgroundColor-NoneTrack']

        if self.backgroundColorFixed:
            backgroundColor = str(tuple(self.backgroundColor))
        else:
            backgroundColor = str(sqrt_algorithm(Image.open('callback_resources/albumImg.jpg')))
        if self.backgroundMode == "Цвет":
            self.centralwidget.setStyleSheet(f'background-color: rgb{backgroundColor}')
            self.backgroundBlur.setEnabled(False)
            self.background.setPixmap(QPixmap(""))
        else:
            img = Image.open('callback_resources/albumImg.jpg')
            newImg = img.resize((2000, 2000))
            if self.backgroundMode == "boxBlur" or self.backgroundMode == "gaussianBlur":
                if self.backgroundMode == "boxBlur":
                    newImg = newImg.filter(ImageFilter.BoxBlur(self.backgroundBlurStrength))
                elif self.backgroundMode == "gaussianBlur":
                    newImg = newImg.filter(ImageFilter.GaussianBlur(self.backgroundBlurStrength))
                self.backgroundBlur.setEnabled(False)
            elif self.backgroundMode == "qFilterBlur":
                self.backgroundBlur.setBlurRadius(self.backgroundBlurStrength)
                self.backgroundBlur.setEnabled(True)
            newImg.save('callback_resources/albumImg.jpg')
            self.centralwidget.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
            self.background.setPixmap(QPixmap('callback_resources/albumImg.jpg'))
        self.currentBackgroundColor = backgroundColor
        print(backgroundColor)

    def updateTrackThread(self, playback):
        self.changeBackground()
        for widget in updateTrack:
            exec('self.' + widget + f'.updateTrack({playback}, {self.currentBackgroundColor})')

    def noneTrackThread(self):
        currentBackgroundColor = str(tuple(self.backgroundColor_noneTrack))
        self.centralwidget.setStyleSheet(f'background-color: rgb{currentBackgroundColor}')
        for widget in nonePlayback:
            exec('self.' + widget + f'.nonePlayback({currentBackgroundColor})')
            time.sleep(0.1)
