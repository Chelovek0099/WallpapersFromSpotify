import sys
import callToSpotifyAPI
import threading
from PySide6.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def retranslateUi(self, trackName, artists):
        self.ui.retranslateUi(self, trackName, artists)

    def updateProgressBar(self, progress, duration):
        self.ui.updateProgressBar(progress, duration)


def updateTrack():
    window.retranslateUi(*SpCaller.initMainWindow())
    while True:
        try:
            window.retranslateUi(*SpCaller.getTrackUpdate())
        except Exception as e:
            print(e)


def updateProgressBar():
    while True:
        window.updateProgressBar(*SpCaller.getProgressTrack())


if __name__ == "__main__":
    SpCaller = callToSpotifyAPI.SpCaller()
    SpCaller.initMainWindow()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()

    updateTrackThread = threading.Thread(target = updateTrack)
    updateProgressBarThread = threading.Thread(target = updateProgressBar)

    updateTrackThread.start()
    updateProgressBarThread.start()

    sys.exit(app.exec())
