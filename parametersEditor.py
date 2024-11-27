import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QLabel,
    QLineEdit, QScrollArea, QSizePolicy, QMainWindow, QWidget)

class Ui_Dialog(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(599, 475)
        MainWindow.setStyleSheet(u"background-color: rgb(42, 42, 42);\n"
"color: white;\n"
"font-size: 14px;")
        self.gridLayout_2 = QGridLayout(MainWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 579, 422))
        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 74, 41, 22))
        self.lineEdit_2.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")
        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(150, 74, 41, 22))
        self.lineEdit_4.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 114, 181, 21))
        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(100, 74, 41, 22))
        self.lineEdit_3.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")
        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(0, 144, 69, 31))
        self.comboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 4, 91, 21))
        self.label.setStyleSheet(u"")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 39, 181, 31))
        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 74, 41, 22))
        self.lineEdit.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")
        self.checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(0, 0, 21, 31))
        self.checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.checkBox.setIconSize(QSize(18, 18))
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"right", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"left", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"up", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"down", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.checkBox.setText("")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
