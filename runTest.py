import sys
import librosa
import wave
import random
import time
from statistics import mean
import threading

import pyaudio
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame

from test import Ui_MainWindow

CHUNK = 2 ** 11
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 44100


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.vals = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.start_animation)
        self.timer.start(50)
        threading.Thread(target = self.equalizer, args = (0,)).start()

    def start_animation(self):
        self.anims = QtCore.QParallelAnimationGroup(self)
        for i in range(len(self.vals)):
            widget = self.ui.val_widgets[i]
            ani = QtCore.QPropertyAnimation(widget, b'geometry')
            ani.setStartValue(QtCore.QRect(50, 150 + (20 * i), widget.width(), 15))
            ani.setEndValue(QtCore.QRect(50, 150 + (20 * i), self.vals[i] * 50, 15))
            ani.setDuration(50)
            self.anims.addAnimation(ani)
        self.anims.start()
        print(self.vals)

    def callback(self, in_data, frame_count, time_info, flag):
        if flag:
            print("Playback Error: %i" % flag)

        file_name = f'temp{1}.wav'
        file = wave.open(file_name, 'wb')
        file.setnchannels(CHANNELS)
        file.setsampwidth(FORMAT)
        file.setframerate(RATE)

        file.writeframes(in_data)
        file.close()

        y, sr = librosa.load(file_name)
        y_harmonic, y_percussive = librosa.effects.hpss(y)

        cof = 500
        val_harmonic = int(abs(y_harmonic[0]) * cof)
        val_16000 = val_harmonic + random.randint(1, 3) if val_harmonic != 0 else 0
        val_4000 = val_harmonic + random.randint(0, 2) if val_harmonic != 0 else 0
        val_8000 = val_4000 + random.randint(0, 1) if val_4000 != 0 else 0
        val_percussive = int(abs(y_percussive[0]) * 4 * cof)
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

    def equalizer(self, x):
        time.sleep(x)
        p = pyaudio.PyAudio()

        stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK,
                        stream_callback = self.callback)

        while stream.is_active():
            pass

        stream.close()
        p.terminate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
