from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget, QTextBrowser)

class Ui_MainWindow(object):
    def cache_write(self):
        self.isDone = True
        self.label_2.setHtml('''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: "\2610"; }
li.checked::marker { content: "\2612"; }
</style></head><body style=" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Авторизация прошла успешно. Это окно можно закрыть и перезапустить программу.</p></body></html>
''')

    def setupUi(self, MainWindow):
        self.isDone = False
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(371, 280)
        MainWindow.setStyleSheet(u"background-color: rgb(42, 42, 42);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 60, 331, 111))
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(18, 18, 18);\n"
"border: 1px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 331, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 190, 171, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 10px;\n"
"} QPushButton::pressed {\n"
"	background-color: rgb(29, 29, 29);\n"
"}\n")
        self.pushButton.clicked.connect(lambda: self.cache_write())
        self.label_2 = QTextBrowser(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 230, 341, 51))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"font-size: 13px;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 url \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u044b \u0431\u044b\u043b\u0438 \u043d\u0430\u043f\u0440\u0432\u043b\u0435\u043d\u043d\u044b:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
