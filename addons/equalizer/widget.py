import random
import threading
import wave
from statistics import mean

import librosa
import pyaudio
from PySide6.QtWidgets import QFrame
from PySide6 import QtCore

import json

CHUNK = 2 ** 11
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 44100


class Equalizer (QFrame):
    def init(self, playback):
        self.operator_to_func = {
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '==': lambda a, b: a == b
        }
        self.configInit()

        self.setGeometry(QtCore.QRect(*self.equalizerPosition, 10000, 10000))
        self.setStyleSheet(f"background-color: rgba{str(tuple([0, 0, 0, 0]))}")

        self.val_widgets = []
        for i in range(10):
            val = QFrame(self)
            val.setGeometry(QtCore.QRect(0, ((self.equalizer_valWidth + self.equalizer_valSpaces) * i), 100,
                                         self.equalizer_valWidth))
            self.val_widgets.append(val)

        self.vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        threading.Thread(target = self.equalizer).start()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.start_animation)
        self.timer.start(50)

    def updateTrack(self, playback, background):
        if self.operator_to_func[self.equalizerColorThresholdMode](
                sorted(background), sorted(self.equalizerColorThreshold)) and not self.equalizerColorFixed:
            color = f"background-color: rgba{str(tuple(self.equalizerColor2))}"
        else:
            color = f"background-color: rgba{str(tuple(self.equalizerColor1))}"

        for val_widget in self.val_widgets:
            val_widget.setStyleSheet(color)

    def updateWidget(self, background):
        self.configInit()

        self.setGeometry(QtCore.QRect(*self.equalizerPosition, 10000, 10000))

        if self.operator_to_func[self.equalizerColorThresholdMode](
                sorted(background), sorted(self.equalizerColorThreshold)) and not self.equalizerColorFixed:
            color = f"background-color: rgba{str(tuple(self.equalizerColor2))}"
        else:
            color = f"background-color: rgba{str(tuple(self.equalizerColor1))}"

        for i in range(10):
            self.val_widgets[i].setGeometry(QtCore.QRect(0, ((self.equalizer_valWidth + self.equalizer_valSpaces) * i),
                                                         100, self.equalizer_valWidth))
            self.val_widgets[i].setStyleSheet(color)

    def callback(self, in_data, frame_count, time_info, flag):
        if flag:
            print("Playback Error: %i" % flag)

        file_name = 'temp1.wav'
        file = wave.open(file_name, 'wb')
        file.setnchannels(CHANNELS)
        file.setsampwidth(FORMAT)
        file.setframerate(RATE)

        file.writeframes(in_data)
        file.close()

        y, sr = librosa.load(file_name)
        y_harmonic, y_percussive = librosa.effects.hpss(y)

        cof = 400
        val_harmonic = int(abs(y_harmonic[0]) * cof)
        val_16000 = val_harmonic + random.randint(1, 3) if val_harmonic != 0 else 0
        val_4000 = val_harmonic + random.randint(0, 2) if val_harmonic != 0 else 0
        val_8000 = val_4000 + random.randint(0, 1) if val_4000 != 0 else 0
        val_percussive = int(abs(y_percussive[0]) * 6 * cof)
        val_125 = val_percussive - random.randint(0, 2) if val_percussive != 0 else 0
        val_63 = val_percussive - random.randint(0, 1) if val_percussive != 0 else 0
        val_32 = val_63 - random.randint(0, 2) if val_63 != 0 else 0
        val_1000 = int(mean([val_harmonic, val_percussive])) + random.randint(-2,
                                                                              2) if val_percussive != 0 and val_harmonic != 0 else 0
        val_500 = int(mean([val_harmonic, val_percussive])) + random.randint(-2,
                                                                             2) if val_percussive != 0 and val_harmonic != 0 else 0
        self.vals = [val_32, val_63, val_125, val_percussive, val_500, val_1000, val_harmonic, val_4000, val_8000,
                     val_16000]

        return in_data, pyaudio.paContinue

    def equalizer(self):
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK,
                        stream_callback = self.callback)

        while self.stream.is_active():
            pass

    def start_animation(self):
        self.anims = QtCore.QParallelAnimationGroup(self)
        for i in range(len(self.vals)):
            widget = self.val_widgets[i]
            ani = QtCore.QPropertyAnimation(widget, b'geometry')
            ani.setStartValue(QtCore.QRect(0, ((self.equalizer_valWidth + self.equalizer_valSpaces) * i), widget.width(),
                                           self.equalizer_valWidth))
            ani.setEndValue(QtCore.QRect(0, ((self.equalizer_valWidth + self.equalizer_valSpaces) * i), self.vals[i] * 20,
                                         self.equalizer_valWidth))
            ani.setDuration(50)
            self.anims.addAnimation(ani)
        self.anims.start()

    def configInit(self):
        with open(r"addons/equalizer/config.json", 'r') as configFile:
            self.config = json.load(configFile)
        self.equalizer_valWidth = self.config["equalizer_valWidth"]
        self.equalizer_valSpaces = self.config["equalizer_valSpaces"]
        self.equalizerColor1 = self.config["equalizerColor1"]
        self.equalizerColorFixed = self.config["equalizerColorFixed"]
        self.equalizerColorThreshold = self.config["equalizerColorThreshold"]
        self.equalizerColorThresholdMode = self.config["equalizerColorThresholdMode"]
        self.equalizerColor2 = self.config["equalizerColor2"]
        equalizerPosition = self.config["equalizerPosition"]

        with open(r"addons/albumImage/config.json", 'r', encoding = 'utf-8') as configFile:
            self.config = json.load(configFile)
        self.albumImageSize = self.config["albumImageSize"]
        self.albumImagePosition = self.config["albumImagePosition"]

        self.equalizerPosition = (self.albumImagePosition[0] + self.albumImageSize + equalizerPosition[0],
                                  self.albumImagePosition[1] + equalizerPosition[1])


    def stop(self):
        self.stream.close()
        self.p.terminate()
