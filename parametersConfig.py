# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parametersConfig.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QScrollArea, QSizePolicy, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)
import sys

class ClickedLabel(QLabel):
    clicked = Signal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(937, 809)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(750, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(18, 18, 18);\n"
"color: white;\n"
"font-size: 14px;")
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_13 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(430, 0))
        self.tabWidget.setMaximumSize(QSize(430, 16777215))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane\n"
"{\n"
"	border: 1px;\n"
"	background: rgb(42, 42, 42);\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"	background: rgb(18, 18, 18);\n"
"	color: rgb(85, 255, 255);\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"	background: rgb(42, 42, 42);\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(0, 0))
        self.tab.setMaximumSize(QSize(16777215, 16777215))
        self.tab.setStyleSheet(u"background: rgb(42, 42, 42);")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -1130, 388, 3653))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 9, 0, 12)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"font-size: 26px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 20))
        self.frame_2.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(16, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(195, 0))
        self.label_2.setMaximumSize(QSize(195, 24))
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.checkBox_2 = QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMaximumSize(QSize(16777215, 24))
        self.checkBox_2.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.checkBox_2.setIconSize(QSize(18, 18))
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setTristate(False)

        self.horizontalLayout_4.addWidget(self.checkBox_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 24))
        self.frame_3.setMaximumSize(QSize(16777215, 24))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(16, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(0, 24))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(0)

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 24))
        self.label_3.setMaximumSize(QSize(16777215, 24))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 24))
        self.frame.setMaximumSize(QSize(16777215, 24))
        self.frame.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(16, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMinimumSize(QSize(50, 24))
        self.lineEdit.setMaximumSize(QSize(50, 24))
        self.lineEdit.setSizeIncrement(QSize(0, 0))
        self.lineEdit.setBaseSize(QSize(0, 18))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(18, 18, 18, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit.setPalette(palette)
        self.lineEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setMinimumSize(QSize(50, 24))
        self.lineEdit_2.setMaximumSize(QSize(50, 24))
        self.lineEdit_2.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        self.lineEdit_3.setMinimumSize(QSize(50, 24))
        self.lineEdit_3.setMaximumSize(QSize(50, 24))
        self.lineEdit_3.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)
        self.lineEdit_4.setMinimumSize(QSize(50, 24))
        self.lineEdit_4.setMaximumSize(QSize(50, 24))
        self.lineEdit_4.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout.addWidget(self.lineEdit_4)

        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(99)
        sizePolicy3.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy3)
        self.frame1.setMinimumSize(QSize(0, 24))
        self.frame1.setMaximumSize(QSize(16777215, 24))
        font = QFont()
        font.setBold(False)
        font.setKerning(True)
        self.frame1.setFont(font)
        self.frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame1)


        self.verticalLayout_2.addWidget(self.frame)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 40))
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.label_4)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 24))
        self.frame_5.setMaximumSize(QSize(16777215, 24))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(0, 24))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_6.addWidget(self.frame_6)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(24)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(0, 24))
        self.label_5.setMaximumSize(QSize(16777215, 24))
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 24))
        self.frame_10.setMaximumSize(QSize(16777215, 24))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(16, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 24))
        self.frame_11.setMaximumSize(QSize(0, 24))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.frame_11)

        self.lineEdit_5 = QLineEdit(self.frame_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(80, 24))
        self.lineEdit_5.setMaximumSize(QSize(80, 24))
        self.lineEdit_5.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_7.addWidget(self.lineEdit_5)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 24))
        self.frame_13.setMaximumSize(QSize(16777215, 24))
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 24))
        self.frame_14.setMaximumSize(QSize(0, 24))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_8.addWidget(self.frame_14)

        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setMinimumSize(QSize(0, 24))
        self.label_6.setMaximumSize(QSize(16777215, 24))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_8.addWidget(self.label_6)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 24))
        self.frame_15.setMaximumSize(QSize(16777215, 24))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(16, 0, 0, -1)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 24))
        self.frame_17.setMaximumSize(QSize(0, 24))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_10.addWidget(self.frame_17)

        self.lineEdit_6 = QLineEdit(self.frame_15)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(80, 24))
        self.lineEdit_6.setMaximumSize(QSize(80, 24))
        self.lineEdit_6.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_10.addWidget(self.lineEdit_6)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_10.addWidget(self.frame_18)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 24))
        self.frame_16.setMaximumSize(QSize(16777215, 24))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(0, 24))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_9.addWidget(self.frame_19)

        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(0, 24))
        self.label_7.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_9.addWidget(self.label_7)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 24))
        self.frame_7.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 0, 0, 0)
        self.lineEdit_8 = QLineEdit(self.frame_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(70, 24))
        self.lineEdit_8.setMaximumSize(QSize(70, 24))
        self.lineEdit_8.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_2.addWidget(self.lineEdit_8)

        self.lineEdit_7 = QLineEdit(self.frame_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(70, 24))
        self.lineEdit_7.setMaximumSize(QSize(70, 24))
        self.lineEdit_7.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_2.addWidget(self.lineEdit_7)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 40))
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.label_8)

        self.frame_20 = QFrame(self.scrollAreaWidgetContents)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 24))
        self.frame_20.setMaximumSize(QSize(16777215, 24))
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(16, 0, 0, 0)
        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 24))
        self.frame_23.setMaximumSize(QSize(0, 24))
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_11.addWidget(self.frame_23)


        self.verticalLayout_2.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 24))
        self.frame_21.setMaximumSize(QSize(16777215, 24))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(16, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 24))
        self.frame_24.setMaximumSize(QSize(0, 24))
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frame_24)

        self.comboBox = QComboBox(self.frame_21)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 24))
        self.comboBox.setMaximumSize(QSize(80, 24))
        self.comboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_12.addWidget(self.comboBox)

        self.frame_25 = QFrame(self.frame_21)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 24))
        self.frame_25.setMaximumSize(QSize(16777215, 24))
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frame_25)


        self.verticalLayout_2.addWidget(self.frame_21)

        self.frame_27 = QFrame(self.scrollAreaWidgetContents)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 24))
        self.frame_27.setMaximumSize(QSize(16777215, 24))
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(16, 0, 0, 0)
        self.label_11 = QLabel(self.frame_27)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 24))
        self.frame_29.setMaximumSize(QSize(0, 24))
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_14.addWidget(self.frame_29)


        self.verticalLayout_2.addWidget(self.frame_27)

        self.frame_30 = QFrame(self.scrollAreaWidgetContents)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 24))
        self.frame_30.setMaximumSize(QSize(16777215, 24))
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(16, 0, 0, -1)
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 24))
        self.frame_31.setMaximumSize(QSize(0, 24))
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_15.addWidget(self.frame_31)

        self.lineEdit_9 = QLineEdit(self.frame_30)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(80, 24))
        self.lineEdit_9.setMaximumSize(QSize(80, 24))
        self.lineEdit_9.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_15.addWidget(self.lineEdit_9)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_15.addWidget(self.frame_32)


        self.verticalLayout_2.addWidget(self.frame_30)

        self.frame_33 = QFrame(self.scrollAreaWidgetContents)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 24))
        self.frame_33.setMaximumSize(QSize(16777215, 24))
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(16, 0, 0, 0)
        self.label_12 = QLabel(self.frame_33)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 24))
        self.frame_34.setMaximumSize(QSize(0, 24))
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_16.addWidget(self.frame_34)


        self.verticalLayout_2.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.scrollAreaWidgetContents)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 24))
        self.frame_35.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_17 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(16, 0, 0, 0)
        self.lineEdit_10 = QLineEdit(self.frame_35)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(70, 24))
        self.lineEdit_10.setMaximumSize(QSize(70, 24))
        self.lineEdit_10.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_17.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.frame_35)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(70, 24))
        self.lineEdit_11.setMaximumSize(QSize(70, 24))
        self.lineEdit_11.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_17.addWidget(self.lineEdit_11)

        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_17.addWidget(self.frame_36)


        self.verticalLayout_2.addWidget(self.frame_35)

        self.frame_37 = QFrame(self.scrollAreaWidgetContents)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 30))
        self.frame_37.setMaximumSize(QSize(16777215, 30))
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(16, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 30))
        self.frame_38.setMaximumSize(QSize(0, 30))
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_18.addWidget(self.frame_38)

        self.label_13 = QLabel(self.frame_37)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_18.addWidget(self.label_13)


        self.verticalLayout_2.addWidget(self.frame_37)

        self.frame_39 = QFrame(self.scrollAreaWidgetContents)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 24))
        self.frame_39.setMaximumSize(QSize(16777215, 24))
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(32, 0, 0, 0)
        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(0, 24))
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_40.setLineWidth(0)

        self.horizontalLayout_20.addWidget(self.frame_40)

        self.label_14 = QLabel(self.frame_39)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 24))
        self.label_14.setMaximumSize(QSize(16777215, 24))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_20.addWidget(self.label_14)


        self.verticalLayout_2.addWidget(self.frame_39)

        self.frame_41 = QFrame(self.scrollAreaWidgetContents)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 24))
        self.frame_41.setMaximumSize(QSize(16777215, 24))
        self.frame_41.setStyleSheet(u"")
        self.horizontalLayout_21 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_12 = QLineEdit(self.frame_41)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy2.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy2)
        self.lineEdit_12.setMinimumSize(QSize(50, 24))
        self.lineEdit_12.setMaximumSize(QSize(50, 24))
        self.lineEdit_12.setSizeIncrement(QSize(0, 0))
        self.lineEdit_12.setBaseSize(QSize(0, 18))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_12.setPalette(palette1)
        self.lineEdit_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_12.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_21.addWidget(self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.frame_41)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy2.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy2)
        self.lineEdit_13.setMinimumSize(QSize(50, 24))
        self.lineEdit_13.setMaximumSize(QSize(50, 24))
        self.lineEdit_13.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_21.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.frame_41)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy2.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy2)
        self.lineEdit_14.setMinimumSize(QSize(50, 24))
        self.lineEdit_14.setMaximumSize(QSize(50, 24))
        self.lineEdit_14.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_21.addWidget(self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.frame_41)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy2.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy2)
        self.lineEdit_15.setMinimumSize(QSize(50, 24))
        self.lineEdit_15.setMaximumSize(QSize(50, 24))
        self.lineEdit_15.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_21.addWidget(self.lineEdit_15)

        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy3.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy3)
        self.frame_42.setMinimumSize(QSize(0, 24))
        self.frame_42.setMaximumSize(QSize(16777215, 24))
        self.frame_42.setFont(font)
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_21.addWidget(self.frame_42)


        self.verticalLayout_2.addWidget(self.frame_41)

        self.frame_43 = QFrame(self.scrollAreaWidgetContents)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 20))
        self.frame_43.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_22 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(32, 0, 0, 0)
        self.label_15 = QLabel(self.frame_43)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(195, 0))
        self.label_15.setMaximumSize(QSize(195, 24))
        self.label_15.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.label_15)

        self.checkBox_3 = QCheckBox(self.frame_43)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMaximumSize(QSize(16777215, 24))
        self.checkBox_3.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.checkBox_3.setIconSize(QSize(18, 18))
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setTristate(False)

        self.horizontalLayout_22.addWidget(self.checkBox_3)


        self.verticalLayout_2.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.scrollAreaWidgetContents)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(0, 24))
        self.frame_44.setMaximumSize(QSize(16777215, 24))
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(32, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(0, 24))
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_45.setLineWidth(0)

        self.horizontalLayout_23.addWidget(self.frame_45)

        self.label_16 = QLabel(self.frame_44)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 24))
        self.label_16.setMaximumSize(QSize(16777215, 24))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_23.addWidget(self.label_16)


        self.verticalLayout_2.addWidget(self.frame_44)

        self.frame_46 = QFrame(self.scrollAreaWidgetContents)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 24))
        self.frame_46.setMaximumSize(QSize(16777215, 24))
        self.frame_46.setStyleSheet(u"")
        self.horizontalLayout_24 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_16 = QLineEdit(self.frame_46)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        sizePolicy2.setHeightForWidth(self.lineEdit_16.sizePolicy().hasHeightForWidth())
        self.lineEdit_16.setSizePolicy(sizePolicy2)
        self.lineEdit_16.setMinimumSize(QSize(50, 24))
        self.lineEdit_16.setMaximumSize(QSize(50, 24))
        self.lineEdit_16.setSizeIncrement(QSize(0, 0))
        self.lineEdit_16.setBaseSize(QSize(0, 18))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_16.setPalette(palette2)
        self.lineEdit_16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_16.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_24.addWidget(self.lineEdit_16)

        self.lineEdit_17 = QLineEdit(self.frame_46)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        sizePolicy2.setHeightForWidth(self.lineEdit_17.sizePolicy().hasHeightForWidth())
        self.lineEdit_17.setSizePolicy(sizePolicy2)
        self.lineEdit_17.setMinimumSize(QSize(50, 24))
        self.lineEdit_17.setMaximumSize(QSize(50, 24))
        self.lineEdit_17.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_24.addWidget(self.lineEdit_17)

        self.lineEdit_18 = QLineEdit(self.frame_46)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        sizePolicy2.setHeightForWidth(self.lineEdit_18.sizePolicy().hasHeightForWidth())
        self.lineEdit_18.setSizePolicy(sizePolicy2)
        self.lineEdit_18.setMinimumSize(QSize(50, 24))
        self.lineEdit_18.setMaximumSize(QSize(50, 24))
        self.lineEdit_18.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_24.addWidget(self.lineEdit_18)

        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy3.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy3)
        self.frame_47.setMinimumSize(QSize(0, 24))
        self.frame_47.setMaximumSize(QSize(16777215, 24))
        self.frame_47.setFont(font)
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_24.addWidget(self.frame_47)


        self.verticalLayout_2.addWidget(self.frame_46)

        self.frame_48 = QFrame(self.scrollAreaWidgetContents)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 24))
        self.frame_48.setMaximumSize(QSize(16777215, 24))
        self.frame_48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(32, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(0, 24))
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_49.setLineWidth(0)

        self.horizontalLayout_25.addWidget(self.frame_49)

        self.label_17 = QLabel(self.frame_48)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 24))
        self.label_17.setMaximumSize(QSize(16777215, 24))
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_25.addWidget(self.label_17)


        self.verticalLayout_2.addWidget(self.frame_48)

        self.frame_50 = QFrame(self.scrollAreaWidgetContents)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 24))
        self.frame_50.setMaximumSize(QSize(16777215, 24))
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(32, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_50)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 24))
        self.frame_53.setMaximumSize(QSize(0, 24))
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_27.addWidget(self.frame_53)

        self.comboBox_3 = QComboBox(self.frame_50)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 24))
        self.comboBox_3.setMaximumSize(QSize(80, 24))
        self.comboBox_3.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_27.addWidget(self.comboBox_3)

        self.frame_54 = QFrame(self.frame_50)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 24))
        self.frame_54.setMaximumSize(QSize(16777215, 24))
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_27.addWidget(self.frame_54)


        self.verticalLayout_2.addWidget(self.frame_50)

        self.frame_55 = QFrame(self.scrollAreaWidgetContents)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 24))
        self.frame_55.setMaximumSize(QSize(16777215, 24))
        self.frame_55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(32, 0, 0, 0)
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMaximumSize(QSize(0, 24))
        self.frame_56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_56.setLineWidth(0)

        self.horizontalLayout_28.addWidget(self.frame_56)

        self.label_18 = QLabel(self.frame_55)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 24))
        self.label_18.setMaximumSize(QSize(16777215, 24))
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_28.addWidget(self.label_18)


        self.verticalLayout_2.addWidget(self.frame_55)

        self.frame_57 = QFrame(self.scrollAreaWidgetContents)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(0, 24))
        self.frame_57.setMaximumSize(QSize(16777215, 24))
        self.frame_57.setStyleSheet(u"")
        self.horizontalLayout_29 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_29.setSpacing(6)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_19 = QLineEdit(self.frame_57)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        sizePolicy2.setHeightForWidth(self.lineEdit_19.sizePolicy().hasHeightForWidth())
        self.lineEdit_19.setSizePolicy(sizePolicy2)
        self.lineEdit_19.setMinimumSize(QSize(50, 24))
        self.lineEdit_19.setMaximumSize(QSize(50, 24))
        self.lineEdit_19.setSizeIncrement(QSize(0, 0))
        self.lineEdit_19.setBaseSize(QSize(0, 18))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_19.setPalette(palette3)
        self.lineEdit_19.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_19.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_29.addWidget(self.lineEdit_19)

        self.lineEdit_20 = QLineEdit(self.frame_57)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        sizePolicy2.setHeightForWidth(self.lineEdit_20.sizePolicy().hasHeightForWidth())
        self.lineEdit_20.setSizePolicy(sizePolicy2)
        self.lineEdit_20.setMinimumSize(QSize(50, 24))
        self.lineEdit_20.setMaximumSize(QSize(50, 24))
        self.lineEdit_20.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_29.addWidget(self.lineEdit_20)

        self.lineEdit_21 = QLineEdit(self.frame_57)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        sizePolicy2.setHeightForWidth(self.lineEdit_21.sizePolicy().hasHeightForWidth())
        self.lineEdit_21.setSizePolicy(sizePolicy2)
        self.lineEdit_21.setMinimumSize(QSize(50, 24))
        self.lineEdit_21.setMaximumSize(QSize(50, 24))
        self.lineEdit_21.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_29.addWidget(self.lineEdit_21)

        self.lineEdit_22 = QLineEdit(self.frame_57)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        sizePolicy2.setHeightForWidth(self.lineEdit_22.sizePolicy().hasHeightForWidth())
        self.lineEdit_22.setSizePolicy(sizePolicy2)
        self.lineEdit_22.setMinimumSize(QSize(50, 24))
        self.lineEdit_22.setMaximumSize(QSize(50, 24))
        self.lineEdit_22.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_29.addWidget(self.lineEdit_22)

        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        sizePolicy3.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy3)
        self.frame_58.setMinimumSize(QSize(0, 24))
        self.frame_58.setMaximumSize(QSize(16777215, 24))
        self.frame_58.setFont(font)
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_29.addWidget(self.frame_58)


        self.verticalLayout_2.addWidget(self.frame_57)

        self.label_111 = QLabel(self.scrollAreaWidgetContents)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(0, 40))
        self.label_111.setMaximumSize(QSize(16777215, 40))
        self.label_111.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.label_111)

        self.frame_284 = QFrame(self.scrollAreaWidgetContents)
        self.frame_284.setObjectName(u"frame_284")
        self.frame_284.setMinimumSize(QSize(0, 24))
        self.frame_284.setMaximumSize(QSize(16777215, 24))
        self.frame_284.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_284.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_182 = QHBoxLayout(self.frame_284)
        self.horizontalLayout_182.setSpacing(0)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(16, 0, 0, 0)
        self.label_109 = QLabel(self.frame_284)
        self.label_109.setObjectName(u"label_109")

        self.horizontalLayout_182.addWidget(self.label_109)

        self.frame_285 = QFrame(self.frame_284)
        self.frame_285.setObjectName(u"frame_285")
        self.frame_285.setMinimumSize(QSize(0, 24))
        self.frame_285.setMaximumSize(QSize(0, 24))
        self.frame_285.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_285.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_182.addWidget(self.frame_285)


        self.verticalLayout_2.addWidget(self.frame_284)

        self.frame_286 = QFrame(self.scrollAreaWidgetContents)
        self.frame_286.setObjectName(u"frame_286")
        self.frame_286.setMinimumSize(QSize(0, 24))
        self.frame_286.setMaximumSize(QSize(16777215, 24))
        self.frame_286.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_286.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_183 = QHBoxLayout(self.frame_286)
        self.horizontalLayout_183.setSpacing(0)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.horizontalLayout_183.setContentsMargins(16, 0, 0, 0)
        self.frame_287 = QFrame(self.frame_286)
        self.frame_287.setObjectName(u"frame_287")
        self.frame_287.setMinimumSize(QSize(0, 24))
        self.frame_287.setMaximumSize(QSize(0, 24))
        self.frame_287.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_287.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_183.addWidget(self.frame_287)

        self.comboBox_20 = QComboBox(self.frame_286)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setMinimumSize(QSize(0, 24))
        self.comboBox_20.setMaximumSize(QSize(80, 24))
        self.comboBox_20.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_183.addWidget(self.comboBox_20)

        self.frame_288 = QFrame(self.frame_286)
        self.frame_288.setObjectName(u"frame_288")
        self.frame_288.setMinimumSize(QSize(0, 24))
        self.frame_288.setMaximumSize(QSize(16777215, 24))
        self.frame_288.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_288.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_183.addWidget(self.frame_288)


        self.verticalLayout_2.addWidget(self.frame_286)

        self.frame_28 = QFrame(self.scrollAreaWidgetContents)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 24))
        self.frame_28.setMaximumSize(QSize(16777215, 24))
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_172 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_172.setSpacing(0)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.horizontalLayout_172.setContentsMargins(16, 0, 0, 0)
        self.label_102 = QLabel(self.frame_28)
        self.label_102.setObjectName(u"label_102")

        self.horizontalLayout_172.addWidget(self.label_102)

        self.frame_119 = QFrame(self.frame_28)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMinimumSize(QSize(0, 24))
        self.frame_119.setMaximumSize(QSize(0, 24))
        self.frame_119.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_172.addWidget(self.frame_119)


        self.verticalLayout_2.addWidget(self.frame_28)

        self.frame_246 = QFrame(self.scrollAreaWidgetContents)
        self.frame_246.setObjectName(u"frame_246")
        self.frame_246.setMinimumSize(QSize(0, 24))
        self.frame_246.setMaximumSize(QSize(16777215, 24))
        self.frame_246.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_246.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_174 = QHBoxLayout(self.frame_246)
        self.horizontalLayout_174.setSpacing(0)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_174.setContentsMargins(16, 0, 0, -1)
        self.frame_250 = QFrame(self.frame_246)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setMinimumSize(QSize(0, 24))
        self.frame_250.setMaximumSize(QSize(0, 24))
        self.frame_250.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_174.addWidget(self.frame_250)

        self.lineEdit_151 = QLineEdit(self.frame_246)
        self.lineEdit_151.setObjectName(u"lineEdit_151")
        self.lineEdit_151.setMinimumSize(QSize(80, 24))
        self.lineEdit_151.setMaximumSize(QSize(80, 24))
        self.lineEdit_151.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_174.addWidget(self.lineEdit_151)

        self.frame_255 = QFrame(self.frame_246)
        self.frame_255.setObjectName(u"frame_255")
        self.frame_255.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_174.addWidget(self.frame_255)


        self.verticalLayout_2.addWidget(self.frame_246)

        self.frame_228 = QFrame(self.scrollAreaWidgetContents)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setMinimumSize(QSize(0, 24))
        self.frame_228.setMaximumSize(QSize(16777215, 24))
        self.frame_228.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_173 = QHBoxLayout(self.frame_228)
        self.horizontalLayout_173.setSpacing(0)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalLayout_173.setContentsMargins(16, 0, 0, 0)
        self.label_105 = QLabel(self.frame_228)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_173.addWidget(self.label_105)

        self.frame_242 = QFrame(self.frame_228)
        self.frame_242.setObjectName(u"frame_242")
        self.frame_242.setMinimumSize(QSize(0, 24))
        self.frame_242.setMaximumSize(QSize(0, 24))
        self.frame_242.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_173.addWidget(self.frame_242)


        self.verticalLayout_2.addWidget(self.frame_228)

        self.frame_260 = QFrame(self.scrollAreaWidgetContents)
        self.frame_260.setObjectName(u"frame_260")
        self.frame_260.setMinimumSize(QSize(0, 24))
        self.frame_260.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_175 = QHBoxLayout(self.frame_260)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(16, 0, 0, 0)
        self.lineEdit_152 = QLineEdit(self.frame_260)
        self.lineEdit_152.setObjectName(u"lineEdit_152")
        self.lineEdit_152.setMinimumSize(QSize(70, 24))
        self.lineEdit_152.setMaximumSize(QSize(70, 24))
        self.lineEdit_152.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_175.addWidget(self.lineEdit_152)

        self.lineEdit_153 = QLineEdit(self.frame_260)
        self.lineEdit_153.setObjectName(u"lineEdit_153")
        self.lineEdit_153.setMinimumSize(QSize(70, 24))
        self.lineEdit_153.setMaximumSize(QSize(70, 24))
        self.lineEdit_153.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_175.addWidget(self.lineEdit_153)

        self.frame_262 = QFrame(self.frame_260)
        self.frame_262.setObjectName(u"frame_262")
        self.frame_262.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_262.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_175.addWidget(self.frame_262)


        self.verticalLayout_2.addWidget(self.frame_260)

        self.frame_289 = QFrame(self.scrollAreaWidgetContents)
        self.frame_289.setObjectName(u"frame_289")
        self.frame_289.setMinimumSize(QSize(0, 30))
        self.frame_289.setMaximumSize(QSize(16777215, 30))
        self.frame_289.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_289.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_184 = QHBoxLayout(self.frame_289)
        self.horizontalLayout_184.setSpacing(0)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(16, 0, 0, 0)
        self.frame_290 = QFrame(self.frame_289)
        self.frame_290.setObjectName(u"frame_290")
        self.frame_290.setMinimumSize(QSize(0, 30))
        self.frame_290.setMaximumSize(QSize(0, 30))
        self.frame_290.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_290.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_184.addWidget(self.frame_290)

        self.label_110 = QLabel(self.frame_289)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setMinimumSize(QSize(0, 30))
        self.label_110.setMaximumSize(QSize(16777215, 30))
        self.label_110.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_184.addWidget(self.label_110)


        self.verticalLayout_2.addWidget(self.frame_289)

        self.frame_282 = QFrame(self.scrollAreaWidgetContents)
        self.frame_282.setObjectName(u"frame_282")
        self.frame_282.setMinimumSize(QSize(0, 24))
        self.frame_282.setMaximumSize(QSize(16777215, 24))
        self.frame_282.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_282.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_181 = QHBoxLayout(self.frame_282)
        self.horizontalLayout_181.setSpacing(0)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(32, 0, 0, 0)
        self.frame_283 = QFrame(self.frame_282)
        self.frame_283.setObjectName(u"frame_283")
        self.frame_283.setMaximumSize(QSize(0, 24))
        self.frame_283.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_283.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_283.setLineWidth(0)

        self.horizontalLayout_181.addWidget(self.frame_283)

        self.label_108 = QLabel(self.frame_282)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(0, 24))
        self.label_108.setMaximumSize(QSize(16777215, 24))
        self.label_108.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_181.addWidget(self.label_108)


        self.verticalLayout_2.addWidget(self.frame_282)

        self.frame_280 = QFrame(self.scrollAreaWidgetContents)
        self.frame_280.setObjectName(u"frame_280")
        self.frame_280.setMinimumSize(QSize(0, 24))
        self.frame_280.setMaximumSize(QSize(16777215, 24))
        self.frame_280.setStyleSheet(u"")
        self.horizontalLayout_180 = QHBoxLayout(self.frame_280)
        self.horizontalLayout_180.setSpacing(6)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_157 = QLineEdit(self.frame_280)
        self.lineEdit_157.setObjectName(u"lineEdit_157")
        sizePolicy2.setHeightForWidth(self.lineEdit_157.sizePolicy().hasHeightForWidth())
        self.lineEdit_157.setSizePolicy(sizePolicy2)
        self.lineEdit_157.setMinimumSize(QSize(50, 24))
        self.lineEdit_157.setMaximumSize(QSize(50, 24))
        self.lineEdit_157.setSizeIncrement(QSize(0, 0))
        self.lineEdit_157.setBaseSize(QSize(0, 18))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_157.setPalette(palette4)
        self.lineEdit_157.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_157.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_180.addWidget(self.lineEdit_157)

        self.lineEdit_158 = QLineEdit(self.frame_280)
        self.lineEdit_158.setObjectName(u"lineEdit_158")
        sizePolicy2.setHeightForWidth(self.lineEdit_158.sizePolicy().hasHeightForWidth())
        self.lineEdit_158.setSizePolicy(sizePolicy2)
        self.lineEdit_158.setMinimumSize(QSize(50, 24))
        self.lineEdit_158.setMaximumSize(QSize(50, 24))
        self.lineEdit_158.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_180.addWidget(self.lineEdit_158)

        self.lineEdit_159 = QLineEdit(self.frame_280)
        self.lineEdit_159.setObjectName(u"lineEdit_159")
        sizePolicy2.setHeightForWidth(self.lineEdit_159.sizePolicy().hasHeightForWidth())
        self.lineEdit_159.setSizePolicy(sizePolicy2)
        self.lineEdit_159.setMinimumSize(QSize(50, 24))
        self.lineEdit_159.setMaximumSize(QSize(50, 24))
        self.lineEdit_159.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_180.addWidget(self.lineEdit_159)

        self.lineEdit_160 = QLineEdit(self.frame_280)
        self.lineEdit_160.setObjectName(u"lineEdit_160")
        sizePolicy2.setHeightForWidth(self.lineEdit_160.sizePolicy().hasHeightForWidth())
        self.lineEdit_160.setSizePolicy(sizePolicy2)
        self.lineEdit_160.setMinimumSize(QSize(50, 24))
        self.lineEdit_160.setMaximumSize(QSize(50, 24))
        self.lineEdit_160.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_180.addWidget(self.lineEdit_160)

        self.frame_281 = QFrame(self.frame_280)
        self.frame_281.setObjectName(u"frame_281")
        sizePolicy3.setHeightForWidth(self.frame_281.sizePolicy().hasHeightForWidth())
        self.frame_281.setSizePolicy(sizePolicy3)
        self.frame_281.setMinimumSize(QSize(0, 24))
        self.frame_281.setMaximumSize(QSize(16777215, 24))
        self.frame_281.setFont(font)
        self.frame_281.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_281.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_180.addWidget(self.frame_281)


        self.verticalLayout_2.addWidget(self.frame_280)

        self.frame_291 = QFrame(self.scrollAreaWidgetContents)
        self.frame_291.setObjectName(u"frame_291")
        self.frame_291.setMinimumSize(QSize(0, 20))
        self.frame_291.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_185 = QHBoxLayout(self.frame_291)
        self.horizontalLayout_185.setSpacing(5)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.horizontalLayout_185.setContentsMargins(32, 0, 0, 0)
        self.label_112 = QLabel(self.frame_291)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(195, 0))
        self.label_112.setMaximumSize(QSize(195, 24))
        self.label_112.setStyleSheet(u"")

        self.horizontalLayout_185.addWidget(self.label_112)

        self.checkBox_13 = QCheckBox(self.frame_291)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setMaximumSize(QSize(16777215, 24))
        self.checkBox_13.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.checkBox_13.setIconSize(QSize(18, 18))
        self.checkBox_13.setChecked(False)
        self.checkBox_13.setTristate(False)

        self.horizontalLayout_185.addWidget(self.checkBox_13)


        self.verticalLayout_2.addWidget(self.frame_291)

        self.frame_264 = QFrame(self.scrollAreaWidgetContents)
        self.frame_264.setObjectName(u"frame_264")
        self.frame_264.setMinimumSize(QSize(0, 24))
        self.frame_264.setMaximumSize(QSize(16777215, 24))
        self.frame_264.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_264.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_176 = QHBoxLayout(self.frame_264)
        self.horizontalLayout_176.setSpacing(0)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(32, 0, 0, 0)
        self.frame_266 = QFrame(self.frame_264)
        self.frame_266.setObjectName(u"frame_266")
        self.frame_266.setMaximumSize(QSize(0, 24))
        self.frame_266.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_266.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_266.setLineWidth(0)

        self.horizontalLayout_176.addWidget(self.frame_266)

        self.label_106 = QLabel(self.frame_264)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(0, 24))
        self.label_106.setMaximumSize(QSize(16777215, 24))
        self.label_106.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_176.addWidget(self.label_106)


        self.verticalLayout_2.addWidget(self.frame_264)

        self.frame_278 = QFrame(self.scrollAreaWidgetContents)
        self.frame_278.setObjectName(u"frame_278")
        self.frame_278.setMinimumSize(QSize(0, 24))
        self.frame_278.setMaximumSize(QSize(16777215, 24))
        self.frame_278.setStyleSheet(u"")
        self.horizontalLayout_179 = QHBoxLayout(self.frame_278)
        self.horizontalLayout_179.setSpacing(6)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_154 = QLineEdit(self.frame_278)
        self.lineEdit_154.setObjectName(u"lineEdit_154")
        sizePolicy2.setHeightForWidth(self.lineEdit_154.sizePolicy().hasHeightForWidth())
        self.lineEdit_154.setSizePolicy(sizePolicy2)
        self.lineEdit_154.setMinimumSize(QSize(50, 24))
        self.lineEdit_154.setMaximumSize(QSize(50, 24))
        self.lineEdit_154.setSizeIncrement(QSize(0, 0))
        self.lineEdit_154.setBaseSize(QSize(0, 18))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_154.setPalette(palette5)
        self.lineEdit_154.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_154.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_179.addWidget(self.lineEdit_154)

        self.lineEdit_155 = QLineEdit(self.frame_278)
        self.lineEdit_155.setObjectName(u"lineEdit_155")
        sizePolicy2.setHeightForWidth(self.lineEdit_155.sizePolicy().hasHeightForWidth())
        self.lineEdit_155.setSizePolicy(sizePolicy2)
        self.lineEdit_155.setMinimumSize(QSize(50, 24))
        self.lineEdit_155.setMaximumSize(QSize(50, 24))
        self.lineEdit_155.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_179.addWidget(self.lineEdit_155)

        self.lineEdit_156 = QLineEdit(self.frame_278)
        self.lineEdit_156.setObjectName(u"lineEdit_156")
        sizePolicy2.setHeightForWidth(self.lineEdit_156.sizePolicy().hasHeightForWidth())
        self.lineEdit_156.setSizePolicy(sizePolicy2)
        self.lineEdit_156.setMinimumSize(QSize(50, 24))
        self.lineEdit_156.setMaximumSize(QSize(50, 24))
        self.lineEdit_156.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_179.addWidget(self.lineEdit_156)

        self.frame_279 = QFrame(self.frame_278)
        self.frame_279.setObjectName(u"frame_279")
        sizePolicy3.setHeightForWidth(self.frame_279.sizePolicy().hasHeightForWidth())
        self.frame_279.setSizePolicy(sizePolicy3)
        self.frame_279.setMinimumSize(QSize(0, 24))
        self.frame_279.setMaximumSize(QSize(16777215, 24))
        self.frame_279.setFont(font)
        self.frame_279.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_279.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_179.addWidget(self.frame_279)


        self.verticalLayout_2.addWidget(self.frame_278)

        self.frame_268 = QFrame(self.scrollAreaWidgetContents)
        self.frame_268.setObjectName(u"frame_268")
        self.frame_268.setMinimumSize(QSize(0, 24))
        self.frame_268.setMaximumSize(QSize(16777215, 24))
        self.frame_268.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_268.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_177 = QHBoxLayout(self.frame_268)
        self.horizontalLayout_177.setSpacing(0)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(32, 0, 0, 0)
        self.frame_271 = QFrame(self.frame_268)
        self.frame_271.setObjectName(u"frame_271")
        self.frame_271.setMaximumSize(QSize(0, 24))
        self.frame_271.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_271.setLineWidth(0)

        self.horizontalLayout_177.addWidget(self.frame_271)

        self.label_107 = QLabel(self.frame_268)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(0, 24))
        self.label_107.setMaximumSize(QSize(16777215, 24))
        self.label_107.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_177.addWidget(self.label_107)


        self.verticalLayout_2.addWidget(self.frame_268)

        self.frame_273 = QFrame(self.scrollAreaWidgetContents)
        self.frame_273.setObjectName(u"frame_273")
        self.frame_273.setMinimumSize(QSize(0, 24))
        self.frame_273.setMaximumSize(QSize(16777215, 24))
        self.frame_273.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_273.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_178 = QHBoxLayout(self.frame_273)
        self.horizontalLayout_178.setSpacing(0)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalLayout_178.setContentsMargins(32, 0, 0, 0)
        self.frame_274 = QFrame(self.frame_273)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setMinimumSize(QSize(0, 24))
        self.frame_274.setMaximumSize(QSize(0, 24))
        self.frame_274.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_178.addWidget(self.frame_274)

        self.comboBox_19 = QComboBox(self.frame_273)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setMinimumSize(QSize(0, 24))
        self.comboBox_19.setMaximumSize(QSize(80, 24))
        self.comboBox_19.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_178.addWidget(self.comboBox_19)

        self.frame_276 = QFrame(self.frame_273)
        self.frame_276.setObjectName(u"frame_276")
        self.frame_276.setMinimumSize(QSize(0, 24))
        self.frame_276.setMaximumSize(QSize(16777215, 24))
        self.frame_276.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_276.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_178.addWidget(self.frame_276)


        self.verticalLayout_2.addWidget(self.frame_273)

        self.frame_292 = QFrame(self.scrollAreaWidgetContents)
        self.frame_292.setObjectName(u"frame_292")
        self.frame_292.setMinimumSize(QSize(0, 24))
        self.frame_292.setMaximumSize(QSize(16777215, 24))
        self.frame_292.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_292.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_186 = QHBoxLayout(self.frame_292)
        self.horizontalLayout_186.setSpacing(0)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(32, 0, 0, 0)
        self.frame_293 = QFrame(self.frame_292)
        self.frame_293.setObjectName(u"frame_293")
        self.frame_293.setMaximumSize(QSize(0, 24))
        self.frame_293.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_293.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_293.setLineWidth(0)

        self.horizontalLayout_186.addWidget(self.frame_293)

        self.label_113 = QLabel(self.frame_292)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(0, 24))
        self.label_113.setMaximumSize(QSize(16777215, 24))
        self.label_113.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_186.addWidget(self.label_113)


        self.verticalLayout_2.addWidget(self.frame_292)

        self.frame_294 = QFrame(self.scrollAreaWidgetContents)
        self.frame_294.setObjectName(u"frame_294")
        self.frame_294.setMinimumSize(QSize(0, 24))
        self.frame_294.setMaximumSize(QSize(16777215, 24))
        self.frame_294.setStyleSheet(u"")
        self.horizontalLayout_187 = QHBoxLayout(self.frame_294)
        self.horizontalLayout_187.setSpacing(6)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_187.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_161 = QLineEdit(self.frame_294)
        self.lineEdit_161.setObjectName(u"lineEdit_161")
        sizePolicy2.setHeightForWidth(self.lineEdit_161.sizePolicy().hasHeightForWidth())
        self.lineEdit_161.setSizePolicy(sizePolicy2)
        self.lineEdit_161.setMinimumSize(QSize(50, 24))
        self.lineEdit_161.setMaximumSize(QSize(50, 24))
        self.lineEdit_161.setSizeIncrement(QSize(0, 0))
        self.lineEdit_161.setBaseSize(QSize(0, 18))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_161.setPalette(palette6)
        self.lineEdit_161.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_161.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_187.addWidget(self.lineEdit_161)

        self.lineEdit_162 = QLineEdit(self.frame_294)
        self.lineEdit_162.setObjectName(u"lineEdit_162")
        sizePolicy2.setHeightForWidth(self.lineEdit_162.sizePolicy().hasHeightForWidth())
        self.lineEdit_162.setSizePolicy(sizePolicy2)
        self.lineEdit_162.setMinimumSize(QSize(50, 24))
        self.lineEdit_162.setMaximumSize(QSize(50, 24))
        self.lineEdit_162.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_187.addWidget(self.lineEdit_162)

        self.lineEdit_163 = QLineEdit(self.frame_294)
        self.lineEdit_163.setObjectName(u"lineEdit_163")
        sizePolicy2.setHeightForWidth(self.lineEdit_163.sizePolicy().hasHeightForWidth())
        self.lineEdit_163.setSizePolicy(sizePolicy2)
        self.lineEdit_163.setMinimumSize(QSize(50, 24))
        self.lineEdit_163.setMaximumSize(QSize(50, 24))
        self.lineEdit_163.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_187.addWidget(self.lineEdit_163)

        self.lineEdit_164 = QLineEdit(self.frame_294)
        self.lineEdit_164.setObjectName(u"lineEdit_164")
        sizePolicy2.setHeightForWidth(self.lineEdit_164.sizePolicy().hasHeightForWidth())
        self.lineEdit_164.setSizePolicy(sizePolicy2)
        self.lineEdit_164.setMinimumSize(QSize(50, 24))
        self.lineEdit_164.setMaximumSize(QSize(50, 24))
        self.lineEdit_164.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_187.addWidget(self.lineEdit_164)

        self.frame_295 = QFrame(self.frame_294)
        self.frame_295.setObjectName(u"frame_295")
        sizePolicy3.setHeightForWidth(self.frame_295.sizePolicy().hasHeightForWidth())
        self.frame_295.setSizePolicy(sizePolicy3)
        self.frame_295.setMinimumSize(QSize(0, 24))
        self.frame_295.setMaximumSize(QSize(16777215, 24))
        self.frame_295.setFont(font)
        self.frame_295.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_295.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_187.addWidget(self.frame_295)


        self.verticalLayout_2.addWidget(self.frame_294)

        self.label_114 = QLabel(self.scrollAreaWidgetContents)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(0, 40))
        self.label_114.setMaximumSize(QSize(16777215, 40))
        self.label_114.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.label_114)

        self.frame_298 = QFrame(self.scrollAreaWidgetContents)
        self.frame_298.setObjectName(u"frame_298")
        self.frame_298.setMinimumSize(QSize(0, 24))
        self.frame_298.setMaximumSize(QSize(16777215, 24))
        self.frame_298.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_298.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_189 = QHBoxLayout(self.frame_298)
        self.horizontalLayout_189.setSpacing(0)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_189.setContentsMargins(16, 0, 0, 0)
        self.frame_299 = QFrame(self.frame_298)
        self.frame_299.setObjectName(u"frame_299")
        self.frame_299.setMaximumSize(QSize(0, 24))
        self.frame_299.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_299.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_299.setLineWidth(0)

        self.horizontalLayout_189.addWidget(self.frame_299)

        self.label_115 = QLabel(self.frame_298)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(0, 24))
        self.label_115.setMaximumSize(QSize(16777215, 24))
        self.label_115.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_189.addWidget(self.label_115)


        self.verticalLayout_2.addWidget(self.frame_298)

        self.frame_296 = QFrame(self.scrollAreaWidgetContents)
        self.frame_296.setObjectName(u"frame_296")
        self.frame_296.setMinimumSize(QSize(0, 24))
        self.frame_296.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_188 = QHBoxLayout(self.frame_296)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_188.setContentsMargins(16, 0, 0, 0)
        self.lineEdit_165 = QLineEdit(self.frame_296)
        self.lineEdit_165.setObjectName(u"lineEdit_165")
        self.lineEdit_165.setMinimumSize(QSize(70, 24))
        self.lineEdit_165.setMaximumSize(QSize(70, 24))
        self.lineEdit_165.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_188.addWidget(self.lineEdit_165)

        self.lineEdit_166 = QLineEdit(self.frame_296)
        self.lineEdit_166.setObjectName(u"lineEdit_166")
        self.lineEdit_166.setMinimumSize(QSize(70, 24))
        self.lineEdit_166.setMaximumSize(QSize(70, 24))
        self.lineEdit_166.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_188.addWidget(self.lineEdit_166)

        self.frame_297 = QFrame(self.frame_296)
        self.frame_297.setObjectName(u"frame_297")
        self.frame_297.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_297.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_188.addWidget(self.frame_297)


        self.verticalLayout_2.addWidget(self.frame_296)

        self.frame_300 = QFrame(self.scrollAreaWidgetContents)
        self.frame_300.setObjectName(u"frame_300")
        self.frame_300.setMinimumSize(QSize(0, 24))
        self.frame_300.setMaximumSize(QSize(16777215, 24))
        self.frame_300.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_300.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_190 = QHBoxLayout(self.frame_300)
        self.horizontalLayout_190.setSpacing(0)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(16, 0, 0, 0)
        self.frame_301 = QFrame(self.frame_300)
        self.frame_301.setObjectName(u"frame_301")
        self.frame_301.setMaximumSize(QSize(0, 24))
        self.frame_301.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_301.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_301.setLineWidth(0)

        self.horizontalLayout_190.addWidget(self.frame_301)

        self.label_116 = QLabel(self.frame_300)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(0, 24))
        self.label_116.setMaximumSize(QSize(16777215, 24))
        self.label_116.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_190.addWidget(self.label_116)


        self.verticalLayout_2.addWidget(self.frame_300)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 24))
        self.frame_8.setMaximumSize(QSize(16777215, 24))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_251 = QFrame(self.frame_8)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMinimumSize(QSize(0, 24))
        self.frame_251.setMaximumSize(QSize(0, 24))
        self.frame_251.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_19.addWidget(self.frame_251)

        self.lineEdit_167 = QLineEdit(self.frame_8)
        self.lineEdit_167.setObjectName(u"lineEdit_167")
        self.lineEdit_167.setMinimumSize(QSize(80, 24))
        self.lineEdit_167.setMaximumSize(QSize(80, 24))
        self.lineEdit_167.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_19.addWidget(self.lineEdit_167)

        self.frame_256 = QFrame(self.frame_8)
        self.frame_256.setObjectName(u"frame_256")
        self.frame_256.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_19.addWidget(self.frame_256)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_327 = QFrame(self.scrollAreaWidgetContents)
        self.frame_327.setObjectName(u"frame_327")
        self.frame_327.setMinimumSize(QSize(0, 24))
        self.frame_327.setMaximumSize(QSize(16777215, 24))
        self.frame_327.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_327.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_203 = QHBoxLayout(self.frame_327)
        self.horizontalLayout_203.setSpacing(0)
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.horizontalLayout_203.setContentsMargins(16, 0, 0, 0)
        self.frame_330 = QFrame(self.frame_327)
        self.frame_330.setObjectName(u"frame_330")
        self.frame_330.setMaximumSize(QSize(0, 24))
        self.frame_330.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_330.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_330.setLineWidth(0)

        self.horizontalLayout_203.addWidget(self.frame_330)

        self.label_124 = QLabel(self.frame_327)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(0, 24))
        self.label_124.setMaximumSize(QSize(16777215, 24))
        self.label_124.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_203.addWidget(self.label_124)


        self.verticalLayout_2.addWidget(self.frame_327)

        self.frame_315 = QFrame(self.scrollAreaWidgetContents)
        self.frame_315.setObjectName(u"frame_315")
        self.frame_315.setMinimumSize(QSize(0, 24))
        self.frame_315.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_197 = QHBoxLayout(self.frame_315)
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.horizontalLayout_197.setContentsMargins(16, 0, 0, 0)
        self.lineEdit_183 = QLineEdit(self.frame_315)
        self.lineEdit_183.setObjectName(u"lineEdit_183")
        self.lineEdit_183.setMinimumSize(QSize(70, 24))
        self.lineEdit_183.setMaximumSize(QSize(70, 24))
        self.lineEdit_183.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_197.addWidget(self.lineEdit_183)

        self.lineEdit_184 = QLineEdit(self.frame_315)
        self.lineEdit_184.setObjectName(u"lineEdit_184")
        self.lineEdit_184.setMinimumSize(QSize(70, 24))
        self.lineEdit_184.setMaximumSize(QSize(70, 24))
        self.lineEdit_184.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_197.addWidget(self.lineEdit_184)

        self.frame_316 = QFrame(self.frame_315)
        self.frame_316.setObjectName(u"frame_316")
        self.frame_316.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_316.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_197.addWidget(self.frame_316)


        self.verticalLayout_2.addWidget(self.frame_315)

        self.frame_341 = QFrame(self.scrollAreaWidgetContents)
        self.frame_341.setObjectName(u"frame_341")
        self.frame_341.setMinimumSize(QSize(0, 30))
        self.frame_341.setMaximumSize(QSize(16777215, 30))
        self.frame_341.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_341.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_209 = QHBoxLayout(self.frame_341)
        self.horizontalLayout_209.setSpacing(0)
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.horizontalLayout_209.setContentsMargins(16, 0, 0, 0)
        self.label_121 = QLabel(self.frame_341)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(0, 30))
        self.label_121.setMaximumSize(QSize(16777215, 30))
        self.label_121.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_209.addWidget(self.label_121)

        self.frame_342 = QFrame(self.frame_341)
        self.frame_342.setObjectName(u"frame_342")
        self.frame_342.setMinimumSize(QSize(0, 30))
        self.frame_342.setMaximumSize(QSize(0, 30))
        self.frame_342.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_342.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_209.addWidget(self.frame_342)


        self.verticalLayout_2.addWidget(self.frame_341)

        self.frame_339 = QFrame(self.scrollAreaWidgetContents)
        self.frame_339.setObjectName(u"frame_339")
        self.frame_339.setMinimumSize(QSize(0, 24))
        self.frame_339.setMaximumSize(QSize(16777215, 24))
        self.frame_339.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_339.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_208 = QHBoxLayout(self.frame_339)
        self.horizontalLayout_208.setSpacing(0)
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.horizontalLayout_208.setContentsMargins(32, 0, 0, 0)
        self.frame_340 = QFrame(self.frame_339)
        self.frame_340.setObjectName(u"frame_340")
        self.frame_340.setMaximumSize(QSize(0, 24))
        self.frame_340.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_340.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_340.setLineWidth(0)

        self.horizontalLayout_208.addWidget(self.frame_340)

        self.label_118 = QLabel(self.frame_339)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(0, 24))
        self.label_118.setMaximumSize(QSize(16777215, 24))
        self.label_118.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_208.addWidget(self.label_118)


        self.verticalLayout_2.addWidget(self.frame_339)

        self.frame_323 = QFrame(self.scrollAreaWidgetContents)
        self.frame_323.setObjectName(u"frame_323")
        self.frame_323.setMinimumSize(QSize(0, 24))
        self.frame_323.setMaximumSize(QSize(16777215, 24))
        self.frame_323.setStyleSheet(u"")
        self.horizontalLayout_201 = QHBoxLayout(self.frame_323)
        self.horizontalLayout_201.setSpacing(6)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_175 = QLineEdit(self.frame_323)
        self.lineEdit_175.setObjectName(u"lineEdit_175")
        sizePolicy2.setHeightForWidth(self.lineEdit_175.sizePolicy().hasHeightForWidth())
        self.lineEdit_175.setSizePolicy(sizePolicy2)
        self.lineEdit_175.setMinimumSize(QSize(50, 24))
        self.lineEdit_175.setMaximumSize(QSize(50, 24))
        self.lineEdit_175.setSizeIncrement(QSize(0, 0))
        self.lineEdit_175.setBaseSize(QSize(0, 18))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_175.setPalette(palette7)
        self.lineEdit_175.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_175.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_201.addWidget(self.lineEdit_175)

        self.lineEdit_176 = QLineEdit(self.frame_323)
        self.lineEdit_176.setObjectName(u"lineEdit_176")
        sizePolicy2.setHeightForWidth(self.lineEdit_176.sizePolicy().hasHeightForWidth())
        self.lineEdit_176.setSizePolicy(sizePolicy2)
        self.lineEdit_176.setMinimumSize(QSize(50, 24))
        self.lineEdit_176.setMaximumSize(QSize(50, 24))
        self.lineEdit_176.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_201.addWidget(self.lineEdit_176)

        self.lineEdit_177 = QLineEdit(self.frame_323)
        self.lineEdit_177.setObjectName(u"lineEdit_177")
        sizePolicy2.setHeightForWidth(self.lineEdit_177.sizePolicy().hasHeightForWidth())
        self.lineEdit_177.setSizePolicy(sizePolicy2)
        self.lineEdit_177.setMinimumSize(QSize(50, 24))
        self.lineEdit_177.setMaximumSize(QSize(50, 24))
        self.lineEdit_177.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_201.addWidget(self.lineEdit_177)

        self.lineEdit_178 = QLineEdit(self.frame_323)
        self.lineEdit_178.setObjectName(u"lineEdit_178")
        sizePolicy2.setHeightForWidth(self.lineEdit_178.sizePolicy().hasHeightForWidth())
        self.lineEdit_178.setSizePolicy(sizePolicy2)
        self.lineEdit_178.setMinimumSize(QSize(50, 24))
        self.lineEdit_178.setMaximumSize(QSize(50, 24))
        self.lineEdit_178.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_201.addWidget(self.lineEdit_178)

        self.frame_324 = QFrame(self.frame_323)
        self.frame_324.setObjectName(u"frame_324")
        sizePolicy3.setHeightForWidth(self.frame_324.sizePolicy().hasHeightForWidth())
        self.frame_324.setSizePolicy(sizePolicy3)
        self.frame_324.setMinimumSize(QSize(0, 24))
        self.frame_324.setMaximumSize(QSize(16777215, 24))
        self.frame_324.setFont(font)
        self.frame_324.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_324.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_201.addWidget(self.frame_324)


        self.verticalLayout_2.addWidget(self.frame_323)

        self.frame_322 = QFrame(self.scrollAreaWidgetContents)
        self.frame_322.setObjectName(u"frame_322")
        self.frame_322.setMinimumSize(QSize(0, 20))
        self.frame_322.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_200 = QHBoxLayout(self.frame_322)
        self.horizontalLayout_200.setSpacing(5)
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalLayout_200.setContentsMargins(32, 0, 0, 0)
        self.label_122 = QLabel(self.frame_322)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(195, 0))
        self.label_122.setMaximumSize(QSize(195, 24))
        self.label_122.setStyleSheet(u"")

        self.horizontalLayout_200.addWidget(self.label_122)

        self.checkBox_14 = QCheckBox(self.frame_322)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setMaximumSize(QSize(16777215, 24))
        self.checkBox_14.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.checkBox_14.setIconSize(QSize(18, 18))
        self.checkBox_14.setChecked(False)
        self.checkBox_14.setTristate(False)

        self.horizontalLayout_200.addWidget(self.checkBox_14)


        self.verticalLayout_2.addWidget(self.frame_322)

        self.frame_325 = QFrame(self.scrollAreaWidgetContents)
        self.frame_325.setObjectName(u"frame_325")
        self.frame_325.setMinimumSize(QSize(0, 24))
        self.frame_325.setMaximumSize(QSize(16777215, 24))
        self.frame_325.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_325.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_202 = QHBoxLayout(self.frame_325)
        self.horizontalLayout_202.setSpacing(0)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(32, 0, 0, 0)
        self.frame_326 = QFrame(self.frame_325)
        self.frame_326.setObjectName(u"frame_326")
        self.frame_326.setMaximumSize(QSize(0, 24))
        self.frame_326.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_326.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_326.setLineWidth(0)

        self.horizontalLayout_202.addWidget(self.frame_326)

        self.label_120 = QLabel(self.frame_325)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(0, 24))
        self.label_120.setMaximumSize(QSize(16777215, 24))
        self.label_120.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_202.addWidget(self.label_120)


        self.verticalLayout_2.addWidget(self.frame_325)

        self.frame_313 = QFrame(self.scrollAreaWidgetContents)
        self.frame_313.setObjectName(u"frame_313")
        self.frame_313.setMinimumSize(QSize(0, 24))
        self.frame_313.setMaximumSize(QSize(16777215, 24))
        self.frame_313.setStyleSheet(u"")
        self.horizontalLayout_196 = QHBoxLayout(self.frame_313)
        self.horizontalLayout_196.setSpacing(6)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_196.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_172 = QLineEdit(self.frame_313)
        self.lineEdit_172.setObjectName(u"lineEdit_172")
        sizePolicy2.setHeightForWidth(self.lineEdit_172.sizePolicy().hasHeightForWidth())
        self.lineEdit_172.setSizePolicy(sizePolicy2)
        self.lineEdit_172.setMinimumSize(QSize(50, 24))
        self.lineEdit_172.setMaximumSize(QSize(50, 24))
        self.lineEdit_172.setSizeIncrement(QSize(0, 0))
        self.lineEdit_172.setBaseSize(QSize(0, 18))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_172.setPalette(palette8)
        self.lineEdit_172.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_172.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_196.addWidget(self.lineEdit_172)

        self.lineEdit_173 = QLineEdit(self.frame_313)
        self.lineEdit_173.setObjectName(u"lineEdit_173")
        sizePolicy2.setHeightForWidth(self.lineEdit_173.sizePolicy().hasHeightForWidth())
        self.lineEdit_173.setSizePolicy(sizePolicy2)
        self.lineEdit_173.setMinimumSize(QSize(50, 24))
        self.lineEdit_173.setMaximumSize(QSize(50, 24))
        self.lineEdit_173.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_196.addWidget(self.lineEdit_173)

        self.lineEdit_174 = QLineEdit(self.frame_313)
        self.lineEdit_174.setObjectName(u"lineEdit_174")
        sizePolicy2.setHeightForWidth(self.lineEdit_174.sizePolicy().hasHeightForWidth())
        self.lineEdit_174.setSizePolicy(sizePolicy2)
        self.lineEdit_174.setMinimumSize(QSize(50, 24))
        self.lineEdit_174.setMaximumSize(QSize(50, 24))
        self.lineEdit_174.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_196.addWidget(self.lineEdit_174)

        self.frame_314 = QFrame(self.frame_313)
        self.frame_314.setObjectName(u"frame_314")
        sizePolicy3.setHeightForWidth(self.frame_314.sizePolicy().hasHeightForWidth())
        self.frame_314.setSizePolicy(sizePolicy3)
        self.frame_314.setMinimumSize(QSize(0, 24))
        self.frame_314.setMaximumSize(QSize(16777215, 24))
        self.frame_314.setFont(font)
        self.frame_314.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_314.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_196.addWidget(self.frame_314)


        self.verticalLayout_2.addWidget(self.frame_313)

        self.frame_305 = QFrame(self.scrollAreaWidgetContents)
        self.frame_305.setObjectName(u"frame_305")
        self.frame_305.setMinimumSize(QSize(0, 24))
        self.frame_305.setMaximumSize(QSize(16777215, 24))
        self.frame_305.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_305.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_192 = QHBoxLayout(self.frame_305)
        self.horizontalLayout_192.setSpacing(0)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.horizontalLayout_192.setContentsMargins(32, 0, 0, 0)
        self.frame_306 = QFrame(self.frame_305)
        self.frame_306.setObjectName(u"frame_306")
        self.frame_306.setMaximumSize(QSize(0, 24))
        self.frame_306.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_306.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_306.setLineWidth(0)

        self.horizontalLayout_192.addWidget(self.frame_306)

        self.label_117 = QLabel(self.frame_305)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(0, 24))
        self.label_117.setMaximumSize(QSize(16777215, 24))
        self.label_117.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_192.addWidget(self.label_117)


        self.verticalLayout_2.addWidget(self.frame_305)

        self.frame_319 = QFrame(self.scrollAreaWidgetContents)
        self.frame_319.setObjectName(u"frame_319")
        self.frame_319.setMinimumSize(QSize(0, 24))
        self.frame_319.setMaximumSize(QSize(16777215, 24))
        self.frame_319.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_319.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_199 = QHBoxLayout(self.frame_319)
        self.horizontalLayout_199.setSpacing(0)
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.horizontalLayout_199.setContentsMargins(32, 0, 0, 0)
        self.frame_320 = QFrame(self.frame_319)
        self.frame_320.setObjectName(u"frame_320")
        self.frame_320.setMinimumSize(QSize(0, 24))
        self.frame_320.setMaximumSize(QSize(0, 24))
        self.frame_320.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_320.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_199.addWidget(self.frame_320)

        self.comboBox_21 = QComboBox(self.frame_319)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setMinimumSize(QSize(0, 24))
        self.comboBox_21.setMaximumSize(QSize(80, 24))
        self.comboBox_21.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_199.addWidget(self.comboBox_21)

        self.frame_321 = QFrame(self.frame_319)
        self.frame_321.setObjectName(u"frame_321")
        self.frame_321.setMinimumSize(QSize(0, 24))
        self.frame_321.setMaximumSize(QSize(16777215, 24))
        self.frame_321.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_321.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_199.addWidget(self.frame_321)


        self.verticalLayout_2.addWidget(self.frame_319)

        self.frame_311 = QFrame(self.scrollAreaWidgetContents)
        self.frame_311.setObjectName(u"frame_311")
        self.frame_311.setMinimumSize(QSize(0, 24))
        self.frame_311.setMaximumSize(QSize(16777215, 24))
        self.frame_311.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_311.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_195 = QHBoxLayout(self.frame_311)
        self.horizontalLayout_195.setSpacing(0)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(32, 0, 0, 0)
        self.frame_312 = QFrame(self.frame_311)
        self.frame_312.setObjectName(u"frame_312")
        self.frame_312.setMaximumSize(QSize(0, 24))
        self.frame_312.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_312.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_312.setLineWidth(0)

        self.horizontalLayout_195.addWidget(self.frame_312)

        self.label_119 = QLabel(self.frame_311)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(0, 24))
        self.label_119.setMaximumSize(QSize(16777215, 24))
        self.label_119.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_195.addWidget(self.label_119)


        self.verticalLayout_2.addWidget(self.frame_311)

        self.frame_307 = QFrame(self.scrollAreaWidgetContents)
        self.frame_307.setObjectName(u"frame_307")
        self.frame_307.setMinimumSize(QSize(0, 24))
        self.frame_307.setMaximumSize(QSize(16777215, 24))
        self.frame_307.setStyleSheet(u"")
        self.horizontalLayout_193 = QHBoxLayout(self.frame_307)
        self.horizontalLayout_193.setSpacing(6)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_168 = QLineEdit(self.frame_307)
        self.lineEdit_168.setObjectName(u"lineEdit_168")
        sizePolicy2.setHeightForWidth(self.lineEdit_168.sizePolicy().hasHeightForWidth())
        self.lineEdit_168.setSizePolicy(sizePolicy2)
        self.lineEdit_168.setMinimumSize(QSize(50, 24))
        self.lineEdit_168.setMaximumSize(QSize(50, 24))
        self.lineEdit_168.setSizeIncrement(QSize(0, 0))
        self.lineEdit_168.setBaseSize(QSize(0, 18))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_168.setPalette(palette9)
        self.lineEdit_168.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_168.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_193.addWidget(self.lineEdit_168)

        self.lineEdit_169 = QLineEdit(self.frame_307)
        self.lineEdit_169.setObjectName(u"lineEdit_169")
        sizePolicy2.setHeightForWidth(self.lineEdit_169.sizePolicy().hasHeightForWidth())
        self.lineEdit_169.setSizePolicy(sizePolicy2)
        self.lineEdit_169.setMinimumSize(QSize(50, 24))
        self.lineEdit_169.setMaximumSize(QSize(50, 24))
        self.lineEdit_169.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_193.addWidget(self.lineEdit_169)

        self.lineEdit_170 = QLineEdit(self.frame_307)
        self.lineEdit_170.setObjectName(u"lineEdit_170")
        sizePolicy2.setHeightForWidth(self.lineEdit_170.sizePolicy().hasHeightForWidth())
        self.lineEdit_170.setSizePolicy(sizePolicy2)
        self.lineEdit_170.setMinimumSize(QSize(50, 24))
        self.lineEdit_170.setMaximumSize(QSize(50, 24))
        self.lineEdit_170.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_193.addWidget(self.lineEdit_170)

        self.lineEdit_171 = QLineEdit(self.frame_307)
        self.lineEdit_171.setObjectName(u"lineEdit_171")
        sizePolicy2.setHeightForWidth(self.lineEdit_171.sizePolicy().hasHeightForWidth())
        self.lineEdit_171.setSizePolicy(sizePolicy2)
        self.lineEdit_171.setMinimumSize(QSize(50, 24))
        self.lineEdit_171.setMaximumSize(QSize(50, 24))
        self.lineEdit_171.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_193.addWidget(self.lineEdit_171)

        self.frame_308 = QFrame(self.frame_307)
        self.frame_308.setObjectName(u"frame_308")
        sizePolicy3.setHeightForWidth(self.frame_308.sizePolicy().hasHeightForWidth())
        self.frame_308.setSizePolicy(sizePolicy3)
        self.frame_308.setMinimumSize(QSize(0, 24))
        self.frame_308.setMaximumSize(QSize(16777215, 24))
        self.frame_308.setFont(font)
        self.frame_308.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_308.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_193.addWidget(self.frame_308)


        self.verticalLayout_2.addWidget(self.frame_307)

        self.frame_343 = QFrame(self.scrollAreaWidgetContents)
        self.frame_343.setObjectName(u"frame_343")
        self.frame_343.setMinimumSize(QSize(0, 30))
        self.frame_343.setMaximumSize(QSize(16777215, 30))
        self.frame_343.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_343.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_210 = QHBoxLayout(self.frame_343)
        self.horizontalLayout_210.setSpacing(0)
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.horizontalLayout_210.setContentsMargins(16, 0, 0, 0)
        self.label_123 = QLabel(self.frame_343)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(0, 30))
        self.label_123.setMaximumSize(QSize(16777215, 30))
        self.label_123.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_210.addWidget(self.label_123)

        self.frame_344 = QFrame(self.frame_343)
        self.frame_344.setObjectName(u"frame_344")
        self.frame_344.setMinimumSize(QSize(0, 30))
        self.frame_344.setMaximumSize(QSize(0, 30))
        self.frame_344.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_344.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_210.addWidget(self.frame_344)


        self.verticalLayout_2.addWidget(self.frame_343)

        self.frame_345 = QFrame(self.scrollAreaWidgetContents)
        self.frame_345.setObjectName(u"frame_345")
        self.frame_345.setMinimumSize(QSize(0, 24))
        self.frame_345.setMaximumSize(QSize(16777215, 24))
        self.frame_345.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_345.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_211 = QHBoxLayout(self.frame_345)
        self.horizontalLayout_211.setSpacing(0)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.horizontalLayout_211.setContentsMargins(32, 0, 0, 0)
        self.frame_346 = QFrame(self.frame_345)
        self.frame_346.setObjectName(u"frame_346")
        self.frame_346.setMaximumSize(QSize(0, 24))
        self.frame_346.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_346.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_346.setLineWidth(0)

        self.horizontalLayout_211.addWidget(self.frame_346)

        self.label_125 = QLabel(self.frame_345)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(0, 24))
        self.label_125.setMaximumSize(QSize(16777215, 24))
        self.label_125.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_211.addWidget(self.label_125)


        self.verticalLayout_2.addWidget(self.frame_345)

        self.frame_328 = QFrame(self.scrollAreaWidgetContents)
        self.frame_328.setObjectName(u"frame_328")
        self.frame_328.setMinimumSize(QSize(0, 24))
        self.frame_328.setMaximumSize(QSize(16777215, 24))
        self.frame_328.setStyleSheet(u"")
        self.horizontalLayout_204 = QHBoxLayout(self.frame_328)
        self.horizontalLayout_204.setSpacing(6)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.horizontalLayout_204.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_179 = QLineEdit(self.frame_328)
        self.lineEdit_179.setObjectName(u"lineEdit_179")
        sizePolicy2.setHeightForWidth(self.lineEdit_179.sizePolicy().hasHeightForWidth())
        self.lineEdit_179.setSizePolicy(sizePolicy2)
        self.lineEdit_179.setMinimumSize(QSize(50, 24))
        self.lineEdit_179.setMaximumSize(QSize(50, 24))
        self.lineEdit_179.setSizeIncrement(QSize(0, 0))
        self.lineEdit_179.setBaseSize(QSize(0, 18))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_179.setPalette(palette10)
        self.lineEdit_179.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_179.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_204.addWidget(self.lineEdit_179)

        self.lineEdit_180 = QLineEdit(self.frame_328)
        self.lineEdit_180.setObjectName(u"lineEdit_180")
        sizePolicy2.setHeightForWidth(self.lineEdit_180.sizePolicy().hasHeightForWidth())
        self.lineEdit_180.setSizePolicy(sizePolicy2)
        self.lineEdit_180.setMinimumSize(QSize(50, 24))
        self.lineEdit_180.setMaximumSize(QSize(50, 24))
        self.lineEdit_180.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_204.addWidget(self.lineEdit_180)

        self.lineEdit_181 = QLineEdit(self.frame_328)
        self.lineEdit_181.setObjectName(u"lineEdit_181")
        sizePolicy2.setHeightForWidth(self.lineEdit_181.sizePolicy().hasHeightForWidth())
        self.lineEdit_181.setSizePolicy(sizePolicy2)
        self.lineEdit_181.setMinimumSize(QSize(50, 24))
        self.lineEdit_181.setMaximumSize(QSize(50, 24))
        self.lineEdit_181.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_204.addWidget(self.lineEdit_181)

        self.lineEdit_182 = QLineEdit(self.frame_328)
        self.lineEdit_182.setObjectName(u"lineEdit_182")
        sizePolicy2.setHeightForWidth(self.lineEdit_182.sizePolicy().hasHeightForWidth())
        self.lineEdit_182.setSizePolicy(sizePolicy2)
        self.lineEdit_182.setMinimumSize(QSize(50, 24))
        self.lineEdit_182.setMaximumSize(QSize(50, 24))
        self.lineEdit_182.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_204.addWidget(self.lineEdit_182)

        self.frame_329 = QFrame(self.frame_328)
        self.frame_329.setObjectName(u"frame_329")
        sizePolicy3.setHeightForWidth(self.frame_329.sizePolicy().hasHeightForWidth())
        self.frame_329.setSizePolicy(sizePolicy3)
        self.frame_329.setMinimumSize(QSize(0, 24))
        self.frame_329.setMaximumSize(QSize(16777215, 24))
        self.frame_329.setFont(font)
        self.frame_329.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_329.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_204.addWidget(self.frame_329)


        self.verticalLayout_2.addWidget(self.frame_328)

        self.frame_347 = QFrame(self.scrollAreaWidgetContents)
        self.frame_347.setObjectName(u"frame_347")
        self.frame_347.setMinimumSize(QSize(0, 20))
        self.frame_347.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_212 = QHBoxLayout(self.frame_347)
        self.horizontalLayout_212.setSpacing(5)
        self.horizontalLayout_212.setObjectName(u"horizontalLayout_212")
        self.horizontalLayout_212.setContentsMargins(32, 0, 0, 0)
        self.label_129 = QLabel(self.frame_347)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(195, 0))
        self.label_129.setMaximumSize(QSize(195, 24))
        self.label_129.setStyleSheet(u"")

        self.horizontalLayout_212.addWidget(self.label_129)

        self.checkBox_16 = QCheckBox(self.frame_347)
        self.checkBox_16.setObjectName(u"checkBox_16")
        self.checkBox_16.setMaximumSize(QSize(16777215, 24))
        self.checkBox_16.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.checkBox_16.setIconSize(QSize(18, 18))
        self.checkBox_16.setChecked(False)
        self.checkBox_16.setTristate(False)

        self.horizontalLayout_212.addWidget(self.checkBox_16)


        self.verticalLayout_2.addWidget(self.frame_347)

        self.frame_348 = QFrame(self.scrollAreaWidgetContents)
        self.frame_348.setObjectName(u"frame_348")
        self.frame_348.setMinimumSize(QSize(0, 24))
        self.frame_348.setMaximumSize(QSize(16777215, 24))
        self.frame_348.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_348.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_213 = QHBoxLayout(self.frame_348)
        self.horizontalLayout_213.setSpacing(0)
        self.horizontalLayout_213.setObjectName(u"horizontalLayout_213")
        self.horizontalLayout_213.setContentsMargins(32, 0, 0, 0)
        self.frame_349 = QFrame(self.frame_348)
        self.frame_349.setObjectName(u"frame_349")
        self.frame_349.setMaximumSize(QSize(0, 24))
        self.frame_349.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_349.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_349.setLineWidth(0)

        self.horizontalLayout_213.addWidget(self.frame_349)

        self.label_130 = QLabel(self.frame_348)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(0, 24))
        self.label_130.setMaximumSize(QSize(16777215, 24))
        self.label_130.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_213.addWidget(self.label_130)


        self.verticalLayout_2.addWidget(self.frame_348)

        self.frame_350 = QFrame(self.scrollAreaWidgetContents)
        self.frame_350.setObjectName(u"frame_350")
        self.frame_350.setMinimumSize(QSize(0, 24))
        self.frame_350.setMaximumSize(QSize(16777215, 24))
        self.frame_350.setStyleSheet(u"")
        self.horizontalLayout_214 = QHBoxLayout(self.frame_350)
        self.horizontalLayout_214.setSpacing(6)
        self.horizontalLayout_214.setObjectName(u"horizontalLayout_214")
        self.horizontalLayout_214.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_190 = QLineEdit(self.frame_350)
        self.lineEdit_190.setObjectName(u"lineEdit_190")
        sizePolicy2.setHeightForWidth(self.lineEdit_190.sizePolicy().hasHeightForWidth())
        self.lineEdit_190.setSizePolicy(sizePolicy2)
        self.lineEdit_190.setMinimumSize(QSize(50, 24))
        self.lineEdit_190.setMaximumSize(QSize(50, 24))
        self.lineEdit_190.setSizeIncrement(QSize(0, 0))
        self.lineEdit_190.setBaseSize(QSize(0, 18))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_190.setPalette(palette11)
        self.lineEdit_190.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_190.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_214.addWidget(self.lineEdit_190)

        self.lineEdit_191 = QLineEdit(self.frame_350)
        self.lineEdit_191.setObjectName(u"lineEdit_191")
        sizePolicy2.setHeightForWidth(self.lineEdit_191.sizePolicy().hasHeightForWidth())
        self.lineEdit_191.setSizePolicy(sizePolicy2)
        self.lineEdit_191.setMinimumSize(QSize(50, 24))
        self.lineEdit_191.setMaximumSize(QSize(50, 24))
        self.lineEdit_191.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_214.addWidget(self.lineEdit_191)

        self.lineEdit_192 = QLineEdit(self.frame_350)
        self.lineEdit_192.setObjectName(u"lineEdit_192")
        sizePolicy2.setHeightForWidth(self.lineEdit_192.sizePolicy().hasHeightForWidth())
        self.lineEdit_192.setSizePolicy(sizePolicy2)
        self.lineEdit_192.setMinimumSize(QSize(50, 24))
        self.lineEdit_192.setMaximumSize(QSize(50, 24))
        self.lineEdit_192.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_214.addWidget(self.lineEdit_192)

        self.frame_351 = QFrame(self.frame_350)
        self.frame_351.setObjectName(u"frame_351")
        sizePolicy3.setHeightForWidth(self.frame_351.sizePolicy().hasHeightForWidth())
        self.frame_351.setSizePolicy(sizePolicy3)
        self.frame_351.setMinimumSize(QSize(0, 24))
        self.frame_351.setMaximumSize(QSize(16777215, 24))
        self.frame_351.setFont(font)
        self.frame_351.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_351.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_214.addWidget(self.frame_351)


        self.verticalLayout_2.addWidget(self.frame_350)

        self.frame_333 = QFrame(self.scrollAreaWidgetContents)
        self.frame_333.setObjectName(u"frame_333")
        self.frame_333.setMinimumSize(QSize(0, 24))
        self.frame_333.setMaximumSize(QSize(16777215, 24))
        self.frame_333.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_333.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_194 = QHBoxLayout(self.frame_333)
        self.horizontalLayout_194.setSpacing(0)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(32, 0, 0, 0)
        self.frame_334 = QFrame(self.frame_333)
        self.frame_334.setObjectName(u"frame_334")
        self.frame_334.setMaximumSize(QSize(0, 24))
        self.frame_334.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_334.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_334.setLineWidth(0)

        self.horizontalLayout_194.addWidget(self.frame_334)

        self.label_127 = QLabel(self.frame_333)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(0, 24))
        self.label_127.setMaximumSize(QSize(16777215, 24))
        self.label_127.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_194.addWidget(self.label_127)


        self.verticalLayout_2.addWidget(self.frame_333)

        self.frame_352 = QFrame(self.scrollAreaWidgetContents)
        self.frame_352.setObjectName(u"frame_352")
        self.frame_352.setMinimumSize(QSize(0, 24))
        self.frame_352.setMaximumSize(QSize(16777215, 24))
        self.frame_352.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_352.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_215 = QHBoxLayout(self.frame_352)
        self.horizontalLayout_215.setSpacing(0)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.horizontalLayout_215.setContentsMargins(32, 0, 0, 0)
        self.frame_353 = QFrame(self.frame_352)
        self.frame_353.setObjectName(u"frame_353")
        self.frame_353.setMinimumSize(QSize(0, 24))
        self.frame_353.setMaximumSize(QSize(0, 24))
        self.frame_353.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_353.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_215.addWidget(self.frame_353)

        self.comboBox_23 = QComboBox(self.frame_352)
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.setObjectName(u"comboBox_23")
        self.comboBox_23.setMinimumSize(QSize(0, 24))
        self.comboBox_23.setMaximumSize(QSize(80, 24))
        self.comboBox_23.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_215.addWidget(self.comboBox_23)

        self.frame_354 = QFrame(self.frame_352)
        self.frame_354.setObjectName(u"frame_354")
        self.frame_354.setMinimumSize(QSize(0, 24))
        self.frame_354.setMaximumSize(QSize(16777215, 24))
        self.frame_354.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_354.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_215.addWidget(self.frame_354)


        self.verticalLayout_2.addWidget(self.frame_352)

        self.frame_317 = QFrame(self.scrollAreaWidgetContents)
        self.frame_317.setObjectName(u"frame_317")
        self.frame_317.setMinimumSize(QSize(0, 24))
        self.frame_317.setMaximumSize(QSize(16777215, 24))
        self.frame_317.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_317.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_198 = QHBoxLayout(self.frame_317)
        self.horizontalLayout_198.setSpacing(0)
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.horizontalLayout_198.setContentsMargins(32, 0, 0, 0)
        self.frame_318 = QFrame(self.frame_317)
        self.frame_318.setObjectName(u"frame_318")
        self.frame_318.setMaximumSize(QSize(0, 24))
        self.frame_318.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_318.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_318.setLineWidth(0)

        self.horizontalLayout_198.addWidget(self.frame_318)

        self.label_126 = QLabel(self.frame_317)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(0, 24))
        self.label_126.setMaximumSize(QSize(16777215, 24))
        self.label_126.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_198.addWidget(self.label_126)


        self.verticalLayout_2.addWidget(self.frame_317)

        self.frame_335 = QFrame(self.scrollAreaWidgetContents)
        self.frame_335.setObjectName(u"frame_335")
        self.frame_335.setMinimumSize(QSize(0, 24))
        self.frame_335.setMaximumSize(QSize(16777215, 24))
        self.frame_335.setStyleSheet(u"")
        self.horizontalLayout_206 = QHBoxLayout(self.frame_335)
        self.horizontalLayout_206.setSpacing(6)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_206.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_186 = QLineEdit(self.frame_335)
        self.lineEdit_186.setObjectName(u"lineEdit_186")
        sizePolicy2.setHeightForWidth(self.lineEdit_186.sizePolicy().hasHeightForWidth())
        self.lineEdit_186.setSizePolicy(sizePolicy2)
        self.lineEdit_186.setMinimumSize(QSize(50, 24))
        self.lineEdit_186.setMaximumSize(QSize(50, 24))
        self.lineEdit_186.setSizeIncrement(QSize(0, 0))
        self.lineEdit_186.setBaseSize(QSize(0, 18))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_186.setPalette(palette12)
        self.lineEdit_186.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_186.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_206.addWidget(self.lineEdit_186)

        self.lineEdit_187 = QLineEdit(self.frame_335)
        self.lineEdit_187.setObjectName(u"lineEdit_187")
        sizePolicy2.setHeightForWidth(self.lineEdit_187.sizePolicy().hasHeightForWidth())
        self.lineEdit_187.setSizePolicy(sizePolicy2)
        self.lineEdit_187.setMinimumSize(QSize(50, 24))
        self.lineEdit_187.setMaximumSize(QSize(50, 24))
        self.lineEdit_187.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_206.addWidget(self.lineEdit_187)

        self.lineEdit_188 = QLineEdit(self.frame_335)
        self.lineEdit_188.setObjectName(u"lineEdit_188")
        sizePolicy2.setHeightForWidth(self.lineEdit_188.sizePolicy().hasHeightForWidth())
        self.lineEdit_188.setSizePolicy(sizePolicy2)
        self.lineEdit_188.setMinimumSize(QSize(50, 24))
        self.lineEdit_188.setMaximumSize(QSize(50, 24))
        self.lineEdit_188.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_206.addWidget(self.lineEdit_188)

        self.lineEdit_189 = QLineEdit(self.frame_335)
        self.lineEdit_189.setObjectName(u"lineEdit_189")
        sizePolicy2.setHeightForWidth(self.lineEdit_189.sizePolicy().hasHeightForWidth())
        self.lineEdit_189.setSizePolicy(sizePolicy2)
        self.lineEdit_189.setMinimumSize(QSize(50, 24))
        self.lineEdit_189.setMaximumSize(QSize(50, 24))
        self.lineEdit_189.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_206.addWidget(self.lineEdit_189)

        self.frame_336 = QFrame(self.frame_335)
        self.frame_336.setObjectName(u"frame_336")
        sizePolicy3.setHeightForWidth(self.frame_336.sizePolicy().hasHeightForWidth())
        self.frame_336.setSizePolicy(sizePolicy3)
        self.frame_336.setMinimumSize(QSize(0, 24))
        self.frame_336.setMaximumSize(QSize(16777215, 24))
        self.frame_336.setFont(font)
        self.frame_336.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_336.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_206.addWidget(self.frame_336)


        self.verticalLayout_2.addWidget(self.frame_335)

        self.frame_355 = QFrame(self.scrollAreaWidgetContents)
        self.frame_355.setObjectName(u"frame_355")
        self.frame_355.setMinimumSize(QSize(0, 30))
        self.frame_355.setMaximumSize(QSize(16777215, 30))
        self.frame_355.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_355.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_216 = QHBoxLayout(self.frame_355)
        self.horizontalLayout_216.setSpacing(0)
        self.horizontalLayout_216.setObjectName(u"horizontalLayout_216")
        self.horizontalLayout_216.setContentsMargins(16, 0, 0, 0)
        self.label_128 = QLabel(self.frame_355)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(0, 30))
        self.label_128.setMaximumSize(QSize(16777215, 30))
        self.label_128.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_216.addWidget(self.label_128)

        self.frame_356 = QFrame(self.frame_355)
        self.frame_356.setObjectName(u"frame_356")
        self.frame_356.setMinimumSize(QSize(0, 30))
        self.frame_356.setMaximumSize(QSize(0, 30))
        self.frame_356.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_356.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_216.addWidget(self.frame_356)


        self.verticalLayout_2.addWidget(self.frame_355)

        self.frame_357 = QFrame(self.scrollAreaWidgetContents)
        self.frame_357.setObjectName(u"frame_357")
        self.frame_357.setMinimumSize(QSize(0, 24))
        self.frame_357.setMaximumSize(QSize(16777215, 24))
        self.frame_357.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_357.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_218 = QHBoxLayout(self.frame_357)
        self.horizontalLayout_218.setSpacing(0)
        self.horizontalLayout_218.setObjectName(u"horizontalLayout_218")
        self.horizontalLayout_218.setContentsMargins(32, 0, 0, 0)
        self.frame_358 = QFrame(self.frame_357)
        self.frame_358.setObjectName(u"frame_358")
        self.frame_358.setMaximumSize(QSize(0, 24))
        self.frame_358.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_358.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_358.setLineWidth(0)

        self.horizontalLayout_218.addWidget(self.frame_358)

        self.label_131 = QLabel(self.frame_357)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(0, 24))
        self.label_131.setMaximumSize(QSize(16777215, 24))
        self.label_131.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_218.addWidget(self.label_131)


        self.verticalLayout_2.addWidget(self.frame_357)

        self.frame_337 = QFrame(self.scrollAreaWidgetContents)
        self.frame_337.setObjectName(u"frame_337")
        self.frame_337.setMinimumSize(QSize(0, 24))
        self.frame_337.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_217 = QHBoxLayout(self.frame_337)
        self.horizontalLayout_217.setObjectName(u"horizontalLayout_217")
        self.horizontalLayout_217.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_194 = QLineEdit(self.frame_337)
        self.lineEdit_194.setObjectName(u"lineEdit_194")
        self.lineEdit_194.setMinimumSize(QSize(70, 24))
        self.lineEdit_194.setMaximumSize(QSize(70, 24))
        self.lineEdit_194.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_217.addWidget(self.lineEdit_194)

        self.lineEdit_195 = QLineEdit(self.frame_337)
        self.lineEdit_195.setObjectName(u"lineEdit_195")
        self.lineEdit_195.setMinimumSize(QSize(70, 24))
        self.lineEdit_195.setMaximumSize(QSize(70, 24))
        self.lineEdit_195.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_217.addWidget(self.lineEdit_195)

        self.frame_338 = QFrame(self.frame_337)
        self.frame_338.setObjectName(u"frame_338")
        self.frame_338.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_338.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_217.addWidget(self.frame_338)


        self.verticalLayout_2.addWidget(self.frame_337)

        self.frame_359 = QFrame(self.scrollAreaWidgetContents)
        self.frame_359.setObjectName(u"frame_359")
        self.frame_359.setMinimumSize(QSize(0, 24))
        self.frame_359.setMaximumSize(QSize(16777215, 24))
        self.frame_359.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_359.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_219 = QHBoxLayout(self.frame_359)
        self.horizontalLayout_219.setSpacing(0)
        self.horizontalLayout_219.setObjectName(u"horizontalLayout_219")
        self.horizontalLayout_219.setContentsMargins(32, 0, 0, 0)
        self.frame_360 = QFrame(self.frame_359)
        self.frame_360.setObjectName(u"frame_360")
        self.frame_360.setMaximumSize(QSize(0, 24))
        self.frame_360.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_360.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_360.setLineWidth(0)

        self.horizontalLayout_219.addWidget(self.frame_360)

        self.label_132 = QLabel(self.frame_359)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(0, 24))
        self.label_132.setMaximumSize(QSize(16777215, 24))
        self.label_132.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_219.addWidget(self.label_132)


        self.verticalLayout_2.addWidget(self.frame_359)

        self.frame_399 = QFrame(self.scrollAreaWidgetContents)
        self.frame_399.setObjectName(u"frame_399")
        self.frame_399.setMinimumSize(QSize(0, 24))
        self.frame_399.setMaximumSize(QSize(16777215, 24))
        self.frame_399.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_399.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_244 = QHBoxLayout(self.frame_399)
        self.horizontalLayout_244.setSpacing(0)
        self.horizontalLayout_244.setObjectName(u"horizontalLayout_244")
        self.horizontalLayout_244.setContentsMargins(32, 0, 0, -1)
        self.frame_400 = QFrame(self.frame_399)
        self.frame_400.setObjectName(u"frame_400")
        self.frame_400.setMinimumSize(QSize(0, 24))
        self.frame_400.setMaximumSize(QSize(0, 24))
        self.frame_400.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_400.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_244.addWidget(self.frame_400)

        self.lineEdit_223 = QLineEdit(self.frame_399)
        self.lineEdit_223.setObjectName(u"lineEdit_223")
        self.lineEdit_223.setMinimumSize(QSize(80, 24))
        self.lineEdit_223.setMaximumSize(QSize(80, 24))
        self.lineEdit_223.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_244.addWidget(self.lineEdit_223)

        self.frame_401 = QFrame(self.frame_399)
        self.frame_401.setObjectName(u"frame_401")
        self.frame_401.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_401.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_244.addWidget(self.frame_401)


        self.verticalLayout_2.addWidget(self.frame_399)

        self.frame_372 = QFrame(self.scrollAreaWidgetContents)
        self.frame_372.setObjectName(u"frame_372")
        self.frame_372.setMinimumSize(QSize(0, 30))
        self.frame_372.setMaximumSize(QSize(16777215, 30))
        self.frame_372.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_372.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_234 = QHBoxLayout(self.frame_372)
        self.horizontalLayout_234.setSpacing(0)
        self.horizontalLayout_234.setObjectName(u"horizontalLayout_234")
        self.horizontalLayout_234.setContentsMargins(32, 0, 0, 0)
        self.label_140 = QLabel(self.frame_372)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(0, 30))
        self.label_140.setMaximumSize(QSize(16777215, 30))
        self.label_140.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_234.addWidget(self.label_140)

        self.frame_373 = QFrame(self.frame_372)
        self.frame_373.setObjectName(u"frame_373")
        self.frame_373.setMinimumSize(QSize(0, 30))
        self.frame_373.setMaximumSize(QSize(0, 30))
        self.frame_373.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_373.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_234.addWidget(self.frame_373)


        self.verticalLayout_2.addWidget(self.frame_372)

        self.frame_378 = QFrame(self.scrollAreaWidgetContents)
        self.frame_378.setObjectName(u"frame_378")
        self.frame_378.setMinimumSize(QSize(0, 24))
        self.frame_378.setMaximumSize(QSize(16777215, 24))
        self.frame_378.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_378.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_236 = QHBoxLayout(self.frame_378)
        self.horizontalLayout_236.setSpacing(0)
        self.horizontalLayout_236.setObjectName(u"horizontalLayout_236")
        self.horizontalLayout_236.setContentsMargins(48, 0, 0, 0)
        self.frame_380 = QFrame(self.frame_378)
        self.frame_380.setObjectName(u"frame_380")
        self.frame_380.setMaximumSize(QSize(0, 24))
        self.frame_380.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_380.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_380.setLineWidth(0)

        self.horizontalLayout_236.addWidget(self.frame_380)

        self.label_142 = QLabel(self.frame_378)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMinimumSize(QSize(0, 24))
        self.label_142.setMaximumSize(QSize(16777215, 24))
        self.label_142.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_236.addWidget(self.label_142)


        self.verticalLayout_2.addWidget(self.frame_378)

        self.frame_364 = QFrame(self.scrollAreaWidgetContents)
        self.frame_364.setObjectName(u"frame_364")
        self.frame_364.setMinimumSize(QSize(0, 24))
        self.frame_364.setMaximumSize(QSize(16777215, 24))
        self.frame_364.setStyleSheet(u"")
        self.horizontalLayout_232 = QHBoxLayout(self.frame_364)
        self.horizontalLayout_232.setSpacing(6)
        self.horizontalLayout_232.setObjectName(u"horizontalLayout_232")
        self.horizontalLayout_232.setContentsMargins(48, 0, 0, 0)
        self.lineEdit_210 = QLineEdit(self.frame_364)
        self.lineEdit_210.setObjectName(u"lineEdit_210")
        sizePolicy2.setHeightForWidth(self.lineEdit_210.sizePolicy().hasHeightForWidth())
        self.lineEdit_210.setSizePolicy(sizePolicy2)
        self.lineEdit_210.setMinimumSize(QSize(50, 24))
        self.lineEdit_210.setMaximumSize(QSize(50, 24))
        self.lineEdit_210.setSizeIncrement(QSize(0, 0))
        self.lineEdit_210.setBaseSize(QSize(0, 18))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_210.setPalette(palette13)
        self.lineEdit_210.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_210.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_232.addWidget(self.lineEdit_210)

        self.lineEdit_211 = QLineEdit(self.frame_364)
        self.lineEdit_211.setObjectName(u"lineEdit_211")
        sizePolicy2.setHeightForWidth(self.lineEdit_211.sizePolicy().hasHeightForWidth())
        self.lineEdit_211.setSizePolicy(sizePolicy2)
        self.lineEdit_211.setMinimumSize(QSize(50, 24))
        self.lineEdit_211.setMaximumSize(QSize(50, 24))
        self.lineEdit_211.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_232.addWidget(self.lineEdit_211)

        self.lineEdit_212 = QLineEdit(self.frame_364)
        self.lineEdit_212.setObjectName(u"lineEdit_212")
        sizePolicy2.setHeightForWidth(self.lineEdit_212.sizePolicy().hasHeightForWidth())
        self.lineEdit_212.setSizePolicy(sizePolicy2)
        self.lineEdit_212.setMinimumSize(QSize(50, 24))
        self.lineEdit_212.setMaximumSize(QSize(50, 24))
        self.lineEdit_212.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_232.addWidget(self.lineEdit_212)

        self.lineEdit_213 = QLineEdit(self.frame_364)
        self.lineEdit_213.setObjectName(u"lineEdit_213")
        sizePolicy2.setHeightForWidth(self.lineEdit_213.sizePolicy().hasHeightForWidth())
        self.lineEdit_213.setSizePolicy(sizePolicy2)
        self.lineEdit_213.setMinimumSize(QSize(50, 24))
        self.lineEdit_213.setMaximumSize(QSize(50, 24))
        self.lineEdit_213.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_232.addWidget(self.lineEdit_213)

        self.frame_366 = QFrame(self.frame_364)
        self.frame_366.setObjectName(u"frame_366")
        sizePolicy3.setHeightForWidth(self.frame_366.sizePolicy().hasHeightForWidth())
        self.frame_366.setSizePolicy(sizePolicy3)
        self.frame_366.setMinimumSize(QSize(0, 24))
        self.frame_366.setMaximumSize(QSize(16777215, 24))
        self.frame_366.setFont(font)
        self.frame_366.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_366.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_232.addWidget(self.frame_366)


        self.verticalLayout_2.addWidget(self.frame_364)

        self.frame_375 = QFrame(self.scrollAreaWidgetContents)
        self.frame_375.setObjectName(u"frame_375")
        self.frame_375.setMinimumSize(QSize(0, 20))
        self.frame_375.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_235 = QHBoxLayout(self.frame_375)
        self.horizontalLayout_235.setSpacing(5)
        self.horizontalLayout_235.setObjectName(u"horizontalLayout_235")
        self.horizontalLayout_235.setContentsMargins(48, 0, 0, 0)
        self.label_141 = QLabel(self.frame_375)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(195, 0))
        self.label_141.setMaximumSize(QSize(195, 24))
        self.label_141.setStyleSheet(u"")

        self.horizontalLayout_235.addWidget(self.label_141)

        self.checkBox_18 = QCheckBox(self.frame_375)
        self.checkBox_18.setObjectName(u"checkBox_18")
        self.checkBox_18.setMaximumSize(QSize(16777215, 24))
        self.checkBox_18.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.checkBox_18.setIconSize(QSize(18, 18))
        self.checkBox_18.setChecked(False)
        self.checkBox_18.setTristate(False)

        self.horizontalLayout_235.addWidget(self.checkBox_18)


        self.verticalLayout_2.addWidget(self.frame_375)

        self.frame_368 = QFrame(self.scrollAreaWidgetContents)
        self.frame_368.setObjectName(u"frame_368")
        self.frame_368.setMinimumSize(QSize(0, 24))
        self.frame_368.setMaximumSize(QSize(16777215, 24))
        self.frame_368.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_368.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_233 = QHBoxLayout(self.frame_368)
        self.horizontalLayout_233.setSpacing(0)
        self.horizontalLayout_233.setObjectName(u"horizontalLayout_233")
        self.horizontalLayout_233.setContentsMargins(48, 0, 0, 0)
        self.frame_370 = QFrame(self.frame_368)
        self.frame_370.setObjectName(u"frame_370")
        self.frame_370.setMaximumSize(QSize(0, 24))
        self.frame_370.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_370.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_370.setLineWidth(0)

        self.horizontalLayout_233.addWidget(self.frame_370)

        self.label_139 = QLabel(self.frame_368)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(0, 24))
        self.label_139.setMaximumSize(QSize(16777215, 24))
        self.label_139.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_233.addWidget(self.label_139)


        self.verticalLayout_2.addWidget(self.frame_368)

        self.frame_391 = QFrame(self.scrollAreaWidgetContents)
        self.frame_391.setObjectName(u"frame_391")
        self.frame_391.setMinimumSize(QSize(0, 24))
        self.frame_391.setMaximumSize(QSize(16777215, 24))
        self.frame_391.setStyleSheet(u"")
        self.horizontalLayout_240 = QHBoxLayout(self.frame_391)
        self.horizontalLayout_240.setSpacing(6)
        self.horizontalLayout_240.setObjectName(u"horizontalLayout_240")
        self.horizontalLayout_240.setContentsMargins(48, 0, 0, 0)
        self.lineEdit_214 = QLineEdit(self.frame_391)
        self.lineEdit_214.setObjectName(u"lineEdit_214")
        sizePolicy2.setHeightForWidth(self.lineEdit_214.sizePolicy().hasHeightForWidth())
        self.lineEdit_214.setSizePolicy(sizePolicy2)
        self.lineEdit_214.setMinimumSize(QSize(50, 24))
        self.lineEdit_214.setMaximumSize(QSize(50, 24))
        self.lineEdit_214.setSizeIncrement(QSize(0, 0))
        self.lineEdit_214.setBaseSize(QSize(0, 18))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_214.setPalette(palette14)
        self.lineEdit_214.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_214.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_240.addWidget(self.lineEdit_214)

        self.lineEdit_215 = QLineEdit(self.frame_391)
        self.lineEdit_215.setObjectName(u"lineEdit_215")
        sizePolicy2.setHeightForWidth(self.lineEdit_215.sizePolicy().hasHeightForWidth())
        self.lineEdit_215.setSizePolicy(sizePolicy2)
        self.lineEdit_215.setMinimumSize(QSize(50, 24))
        self.lineEdit_215.setMaximumSize(QSize(50, 24))
        self.lineEdit_215.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_240.addWidget(self.lineEdit_215)

        self.lineEdit_216 = QLineEdit(self.frame_391)
        self.lineEdit_216.setObjectName(u"lineEdit_216")
        sizePolicy2.setHeightForWidth(self.lineEdit_216.sizePolicy().hasHeightForWidth())
        self.lineEdit_216.setSizePolicy(sizePolicy2)
        self.lineEdit_216.setMinimumSize(QSize(50, 24))
        self.lineEdit_216.setMaximumSize(QSize(50, 24))
        self.lineEdit_216.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_240.addWidget(self.lineEdit_216)

        self.frame_392 = QFrame(self.frame_391)
        self.frame_392.setObjectName(u"frame_392")
        sizePolicy3.setHeightForWidth(self.frame_392.sizePolicy().hasHeightForWidth())
        self.frame_392.setSizePolicy(sizePolicy3)
        self.frame_392.setMinimumSize(QSize(0, 24))
        self.frame_392.setMaximumSize(QSize(16777215, 24))
        self.frame_392.setFont(font)
        self.frame_392.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_392.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_240.addWidget(self.frame_392)


        self.verticalLayout_2.addWidget(self.frame_391)

        self.frame_389 = QFrame(self.scrollAreaWidgetContents)
        self.frame_389.setObjectName(u"frame_389")
        self.frame_389.setMinimumSize(QSize(0, 24))
        self.frame_389.setMaximumSize(QSize(16777215, 24))
        self.frame_389.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_389.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_239 = QHBoxLayout(self.frame_389)
        self.horizontalLayout_239.setSpacing(0)
        self.horizontalLayout_239.setObjectName(u"horizontalLayout_239")
        self.horizontalLayout_239.setContentsMargins(48, 0, 0, 0)
        self.frame_390 = QFrame(self.frame_389)
        self.frame_390.setObjectName(u"frame_390")
        self.frame_390.setMaximumSize(QSize(0, 24))
        self.frame_390.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_390.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_390.setLineWidth(0)

        self.horizontalLayout_239.addWidget(self.frame_390)

        self.label_144 = QLabel(self.frame_389)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(0, 24))
        self.label_144.setMaximumSize(QSize(16777215, 24))
        self.label_144.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_239.addWidget(self.label_144)


        self.verticalLayout_2.addWidget(self.frame_389)

        self.frame_382 = QFrame(self.scrollAreaWidgetContents)
        self.frame_382.setObjectName(u"frame_382")
        self.frame_382.setMinimumSize(QSize(0, 24))
        self.frame_382.setMaximumSize(QSize(16777215, 24))
        self.frame_382.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_382.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_237 = QHBoxLayout(self.frame_382)
        self.horizontalLayout_237.setSpacing(0)
        self.horizontalLayout_237.setObjectName(u"horizontalLayout_237")
        self.horizontalLayout_237.setContentsMargins(48, 0, 0, 0)
        self.frame_384 = QFrame(self.frame_382)
        self.frame_384.setObjectName(u"frame_384")
        self.frame_384.setMinimumSize(QSize(0, 24))
        self.frame_384.setMaximumSize(QSize(0, 24))
        self.frame_384.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_384.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_237.addWidget(self.frame_384)

        self.comboBox_25 = QComboBox(self.frame_382)
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.setObjectName(u"comboBox_25")
        self.comboBox_25.setMinimumSize(QSize(0, 24))
        self.comboBox_25.setMaximumSize(QSize(80, 24))
        self.comboBox_25.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_237.addWidget(self.comboBox_25)

        self.frame_386 = QFrame(self.frame_382)
        self.frame_386.setObjectName(u"frame_386")
        self.frame_386.setMinimumSize(QSize(0, 24))
        self.frame_386.setMaximumSize(QSize(16777215, 24))
        self.frame_386.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_386.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_237.addWidget(self.frame_386)


        self.verticalLayout_2.addWidget(self.frame_382)

        self.frame_387 = QFrame(self.scrollAreaWidgetContents)
        self.frame_387.setObjectName(u"frame_387")
        self.frame_387.setMinimumSize(QSize(0, 24))
        self.frame_387.setMaximumSize(QSize(16777215, 24))
        self.frame_387.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_387.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_238 = QHBoxLayout(self.frame_387)
        self.horizontalLayout_238.setSpacing(0)
        self.horizontalLayout_238.setObjectName(u"horizontalLayout_238")
        self.horizontalLayout_238.setContentsMargins(48, 0, 0, 0)
        self.frame_388 = QFrame(self.frame_387)
        self.frame_388.setObjectName(u"frame_388")
        self.frame_388.setMaximumSize(QSize(0, 24))
        self.frame_388.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_388.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_388.setLineWidth(0)

        self.horizontalLayout_238.addWidget(self.frame_388)

        self.label_143 = QLabel(self.frame_387)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(0, 24))
        self.label_143.setMaximumSize(QSize(16777215, 24))
        self.label_143.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_238.addWidget(self.label_143)


        self.verticalLayout_2.addWidget(self.frame_387)

        self.frame_393 = QFrame(self.scrollAreaWidgetContents)
        self.frame_393.setObjectName(u"frame_393")
        self.frame_393.setMinimumSize(QSize(0, 24))
        self.frame_393.setMaximumSize(QSize(16777215, 24))
        self.frame_393.setStyleSheet(u"")
        self.horizontalLayout_241 = QHBoxLayout(self.frame_393)
        self.horizontalLayout_241.setSpacing(6)
        self.horizontalLayout_241.setObjectName(u"horizontalLayout_241")
        self.horizontalLayout_241.setContentsMargins(48, 0, 0, 0)
        self.lineEdit_217 = QLineEdit(self.frame_393)
        self.lineEdit_217.setObjectName(u"lineEdit_217")
        sizePolicy2.setHeightForWidth(self.lineEdit_217.sizePolicy().hasHeightForWidth())
        self.lineEdit_217.setSizePolicy(sizePolicy2)
        self.lineEdit_217.setMinimumSize(QSize(50, 24))
        self.lineEdit_217.setMaximumSize(QSize(50, 24))
        self.lineEdit_217.setSizeIncrement(QSize(0, 0))
        self.lineEdit_217.setBaseSize(QSize(0, 18))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_217.setPalette(palette15)
        self.lineEdit_217.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_217.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_241.addWidget(self.lineEdit_217)

        self.lineEdit_218 = QLineEdit(self.frame_393)
        self.lineEdit_218.setObjectName(u"lineEdit_218")
        sizePolicy2.setHeightForWidth(self.lineEdit_218.sizePolicy().hasHeightForWidth())
        self.lineEdit_218.setSizePolicy(sizePolicy2)
        self.lineEdit_218.setMinimumSize(QSize(50, 24))
        self.lineEdit_218.setMaximumSize(QSize(50, 24))
        self.lineEdit_218.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_241.addWidget(self.lineEdit_218)

        self.lineEdit_219 = QLineEdit(self.frame_393)
        self.lineEdit_219.setObjectName(u"lineEdit_219")
        sizePolicy2.setHeightForWidth(self.lineEdit_219.sizePolicy().hasHeightForWidth())
        self.lineEdit_219.setSizePolicy(sizePolicy2)
        self.lineEdit_219.setMinimumSize(QSize(50, 24))
        self.lineEdit_219.setMaximumSize(QSize(50, 24))
        self.lineEdit_219.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_241.addWidget(self.lineEdit_219)

        self.lineEdit_220 = QLineEdit(self.frame_393)
        self.lineEdit_220.setObjectName(u"lineEdit_220")
        sizePolicy2.setHeightForWidth(self.lineEdit_220.sizePolicy().hasHeightForWidth())
        self.lineEdit_220.setSizePolicy(sizePolicy2)
        self.lineEdit_220.setMinimumSize(QSize(50, 24))
        self.lineEdit_220.setMaximumSize(QSize(50, 24))
        self.lineEdit_220.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_241.addWidget(self.lineEdit_220)

        self.frame_394 = QFrame(self.frame_393)
        self.frame_394.setObjectName(u"frame_394")
        sizePolicy3.setHeightForWidth(self.frame_394.sizePolicy().hasHeightForWidth())
        self.frame_394.setSizePolicy(sizePolicy3)
        self.frame_394.setMinimumSize(QSize(0, 24))
        self.frame_394.setMaximumSize(QSize(16777215, 24))
        self.frame_394.setFont(font)
        self.frame_394.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_394.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_241.addWidget(self.frame_394)


        self.verticalLayout_2.addWidget(self.frame_393)

        self.label_145 = QLabel(self.scrollAreaWidgetContents)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(0, 40))
        self.label_145.setMaximumSize(QSize(16777215, 40))
        self.label_145.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.label_145)

        self.frame_397 = QFrame(self.scrollAreaWidgetContents)
        self.frame_397.setObjectName(u"frame_397")
        self.frame_397.setMinimumSize(QSize(0, 24))
        self.frame_397.setMaximumSize(QSize(16777215, 24))
        self.frame_397.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_397.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_243 = QHBoxLayout(self.frame_397)
        self.horizontalLayout_243.setSpacing(0)
        self.horizontalLayout_243.setObjectName(u"horizontalLayout_243")
        self.horizontalLayout_243.setContentsMargins(32, 0, 0, 0)
        self.frame_398 = QFrame(self.frame_397)
        self.frame_398.setObjectName(u"frame_398")
        self.frame_398.setMaximumSize(QSize(0, 24))
        self.frame_398.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_398.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_398.setLineWidth(0)

        self.horizontalLayout_243.addWidget(self.frame_398)

        self.label_146 = QLabel(self.frame_397)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(0, 24))
        self.label_146.setMaximumSize(QSize(16777215, 24))
        self.label_146.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_243.addWidget(self.label_146)


        self.verticalLayout_2.addWidget(self.frame_397)

        self.frame_361 = QFrame(self.scrollAreaWidgetContents)
        self.frame_361.setObjectName(u"frame_361")
        self.frame_361.setMinimumSize(QSize(0, 24))
        self.frame_361.setMaximumSize(QSize(16777215, 24))
        self.frame_361.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_361.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_220 = QHBoxLayout(self.frame_361)
        self.horizontalLayout_220.setSpacing(0)
        self.horizontalLayout_220.setObjectName(u"horizontalLayout_220")
        self.horizontalLayout_220.setContentsMargins(32, 0, 0, -1)
        self.frame_362 = QFrame(self.frame_361)
        self.frame_362.setObjectName(u"frame_362")
        self.frame_362.setMinimumSize(QSize(0, 24))
        self.frame_362.setMaximumSize(QSize(0, 24))
        self.frame_362.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_362.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_220.addWidget(self.frame_362)

        self.lineEdit_196 = QLineEdit(self.frame_361)
        self.lineEdit_196.setObjectName(u"lineEdit_196")
        self.lineEdit_196.setMinimumSize(QSize(80, 24))
        self.lineEdit_196.setMaximumSize(QSize(80, 24))
        self.lineEdit_196.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_220.addWidget(self.lineEdit_196)

        self.frame_363 = QFrame(self.frame_361)
        self.frame_363.setObjectName(u"frame_363")
        self.frame_363.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_363.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_220.addWidget(self.frame_363)


        self.verticalLayout_2.addWidget(self.frame_361)

        self.frame_402 = QFrame(self.scrollAreaWidgetContents)
        self.frame_402.setObjectName(u"frame_402")
        self.frame_402.setMinimumSize(QSize(0, 24))
        self.frame_402.setMaximumSize(QSize(16777215, 24))
        self.frame_402.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_402.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_245 = QHBoxLayout(self.frame_402)
        self.horizontalLayout_245.setSpacing(0)
        self.horizontalLayout_245.setObjectName(u"horizontalLayout_245")
        self.horizontalLayout_245.setContentsMargins(32, 0, 0, 0)
        self.frame_403 = QFrame(self.frame_402)
        self.frame_403.setObjectName(u"frame_403")
        self.frame_403.setMaximumSize(QSize(0, 24))
        self.frame_403.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_403.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_403.setLineWidth(0)

        self.horizontalLayout_245.addWidget(self.frame_403)

        self.label_147 = QLabel(self.frame_402)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setMinimumSize(QSize(0, 24))
        self.label_147.setMaximumSize(QSize(16777215, 24))
        self.label_147.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_245.addWidget(self.label_147)


        self.verticalLayout_2.addWidget(self.frame_402)

        self.frame_395 = QFrame(self.scrollAreaWidgetContents)
        self.frame_395.setObjectName(u"frame_395")
        self.frame_395.setMinimumSize(QSize(0, 24))
        self.frame_395.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_242 = QHBoxLayout(self.frame_395)
        self.horizontalLayout_242.setObjectName(u"horizontalLayout_242")
        self.horizontalLayout_242.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_221 = QLineEdit(self.frame_395)
        self.lineEdit_221.setObjectName(u"lineEdit_221")
        self.lineEdit_221.setMinimumSize(QSize(70, 24))
        self.lineEdit_221.setMaximumSize(QSize(70, 24))
        self.lineEdit_221.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_242.addWidget(self.lineEdit_221)

        self.lineEdit_222 = QLineEdit(self.frame_395)
        self.lineEdit_222.setObjectName(u"lineEdit_222")
        self.lineEdit_222.setMinimumSize(QSize(70, 24))
        self.lineEdit_222.setMaximumSize(QSize(70, 24))
        self.lineEdit_222.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_242.addWidget(self.lineEdit_222)

        self.frame_396 = QFrame(self.frame_395)
        self.frame_396.setObjectName(u"frame_396")
        self.frame_396.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_396.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_242.addWidget(self.frame_396)


        self.verticalLayout_2.addWidget(self.frame_395)

        self.frame_408 = QFrame(self.scrollAreaWidgetContents)
        self.frame_408.setObjectName(u"frame_408")
        self.frame_408.setMinimumSize(QSize(0, 30))
        self.frame_408.setMaximumSize(QSize(16777215, 30))
        self.frame_408.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_408.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_248 = QHBoxLayout(self.frame_408)
        self.horizontalLayout_248.setSpacing(0)
        self.horizontalLayout_248.setObjectName(u"horizontalLayout_248")
        self.horizontalLayout_248.setContentsMargins(16, 0, 0, 0)
        self.label_149 = QLabel(self.frame_408)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMinimumSize(QSize(0, 30))
        self.label_149.setMaximumSize(QSize(16777215, 30))
        self.label_149.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_248.addWidget(self.label_149)

        self.frame_409 = QFrame(self.frame_408)
        self.frame_409.setObjectName(u"frame_409")
        self.frame_409.setMinimumSize(QSize(0, 30))
        self.frame_409.setMaximumSize(QSize(0, 30))
        self.frame_409.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_409.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_248.addWidget(self.frame_409)


        self.verticalLayout_2.addWidget(self.frame_408)

        self.frame_411 = QFrame(self.scrollAreaWidgetContents)
        self.frame_411.setObjectName(u"frame_411")
        self.frame_411.setMinimumSize(QSize(0, 24))
        self.frame_411.setMaximumSize(QSize(16777215, 24))
        self.frame_411.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_411.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_250 = QHBoxLayout(self.frame_411)
        self.horizontalLayout_250.setSpacing(0)
        self.horizontalLayout_250.setObjectName(u"horizontalLayout_250")
        self.horizontalLayout_250.setContentsMargins(32, 0, 0, 0)
        self.frame_412 = QFrame(self.frame_411)
        self.frame_412.setObjectName(u"frame_412")
        self.frame_412.setMaximumSize(QSize(0, 24))
        self.frame_412.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_412.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_412.setLineWidth(0)

        self.horizontalLayout_250.addWidget(self.frame_412)

        self.label_151 = QLabel(self.frame_411)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMinimumSize(QSize(0, 24))
        self.label_151.setMaximumSize(QSize(16777215, 24))
        self.label_151.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_250.addWidget(self.label_151)


        self.verticalLayout_2.addWidget(self.frame_411)

        self.frame_404 = QFrame(self.scrollAreaWidgetContents)
        self.frame_404.setObjectName(u"frame_404")
        self.frame_404.setMinimumSize(QSize(0, 24))
        self.frame_404.setMaximumSize(QSize(16777215, 24))
        self.frame_404.setStyleSheet(u"")
        self.horizontalLayout_246 = QHBoxLayout(self.frame_404)
        self.horizontalLayout_246.setSpacing(6)
        self.horizontalLayout_246.setObjectName(u"horizontalLayout_246")
        self.horizontalLayout_246.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_224 = QLineEdit(self.frame_404)
        self.lineEdit_224.setObjectName(u"lineEdit_224")
        sizePolicy2.setHeightForWidth(self.lineEdit_224.sizePolicy().hasHeightForWidth())
        self.lineEdit_224.setSizePolicy(sizePolicy2)
        self.lineEdit_224.setMinimumSize(QSize(50, 24))
        self.lineEdit_224.setMaximumSize(QSize(50, 24))
        self.lineEdit_224.setSizeIncrement(QSize(0, 0))
        self.lineEdit_224.setBaseSize(QSize(0, 18))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_224.setPalette(palette16)
        self.lineEdit_224.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_224.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_246.addWidget(self.lineEdit_224)

        self.lineEdit_225 = QLineEdit(self.frame_404)
        self.lineEdit_225.setObjectName(u"lineEdit_225")
        sizePolicy2.setHeightForWidth(self.lineEdit_225.sizePolicy().hasHeightForWidth())
        self.lineEdit_225.setSizePolicy(sizePolicy2)
        self.lineEdit_225.setMinimumSize(QSize(50, 24))
        self.lineEdit_225.setMaximumSize(QSize(50, 24))
        self.lineEdit_225.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_246.addWidget(self.lineEdit_225)

        self.lineEdit_226 = QLineEdit(self.frame_404)
        self.lineEdit_226.setObjectName(u"lineEdit_226")
        sizePolicy2.setHeightForWidth(self.lineEdit_226.sizePolicy().hasHeightForWidth())
        self.lineEdit_226.setSizePolicy(sizePolicy2)
        self.lineEdit_226.setMinimumSize(QSize(50, 24))
        self.lineEdit_226.setMaximumSize(QSize(50, 24))
        self.lineEdit_226.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_246.addWidget(self.lineEdit_226)

        self.lineEdit_227 = QLineEdit(self.frame_404)
        self.lineEdit_227.setObjectName(u"lineEdit_227")
        sizePolicy2.setHeightForWidth(self.lineEdit_227.sizePolicy().hasHeightForWidth())
        self.lineEdit_227.setSizePolicy(sizePolicy2)
        self.lineEdit_227.setMinimumSize(QSize(50, 24))
        self.lineEdit_227.setMaximumSize(QSize(50, 24))
        self.lineEdit_227.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_246.addWidget(self.lineEdit_227)

        self.frame_405 = QFrame(self.frame_404)
        self.frame_405.setObjectName(u"frame_405")
        sizePolicy3.setHeightForWidth(self.frame_405.sizePolicy().hasHeightForWidth())
        self.frame_405.setSizePolicy(sizePolicy3)
        self.frame_405.setMinimumSize(QSize(0, 24))
        self.frame_405.setMaximumSize(QSize(16777215, 24))
        self.frame_405.setFont(font)
        self.frame_405.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_405.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_246.addWidget(self.frame_405)


        self.verticalLayout_2.addWidget(self.frame_404)

        self.frame_410 = QFrame(self.scrollAreaWidgetContents)
        self.frame_410.setObjectName(u"frame_410")
        self.frame_410.setMinimumSize(QSize(0, 20))
        self.frame_410.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_249 = QHBoxLayout(self.frame_410)
        self.horizontalLayout_249.setSpacing(5)
        self.horizontalLayout_249.setObjectName(u"horizontalLayout_249")
        self.horizontalLayout_249.setContentsMargins(32, 0, 0, 0)
        self.label_150 = QLabel(self.frame_410)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setMinimumSize(QSize(195, 0))
        self.label_150.setMaximumSize(QSize(195, 24))
        self.label_150.setStyleSheet(u"")

        self.horizontalLayout_249.addWidget(self.label_150)

        self.checkBox_19 = QCheckBox(self.frame_410)
        self.checkBox_19.setObjectName(u"checkBox_19")
        self.checkBox_19.setMaximumSize(QSize(16777215, 24))
        self.checkBox_19.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.checkBox_19.setIconSize(QSize(18, 18))
        self.checkBox_19.setChecked(False)
        self.checkBox_19.setTristate(False)

        self.horizontalLayout_249.addWidget(self.checkBox_19)


        self.verticalLayout_2.addWidget(self.frame_410)

        self.frame_406 = QFrame(self.scrollAreaWidgetContents)
        self.frame_406.setObjectName(u"frame_406")
        self.frame_406.setMinimumSize(QSize(0, 24))
        self.frame_406.setMaximumSize(QSize(16777215, 24))
        self.frame_406.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_406.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_247 = QHBoxLayout(self.frame_406)
        self.horizontalLayout_247.setSpacing(0)
        self.horizontalLayout_247.setObjectName(u"horizontalLayout_247")
        self.horizontalLayout_247.setContentsMargins(32, 0, 0, 0)
        self.frame_407 = QFrame(self.frame_406)
        self.frame_407.setObjectName(u"frame_407")
        self.frame_407.setMaximumSize(QSize(0, 24))
        self.frame_407.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_407.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_407.setLineWidth(0)

        self.horizontalLayout_247.addWidget(self.frame_407)

        self.label_148 = QLabel(self.frame_406)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setMinimumSize(QSize(0, 24))
        self.label_148.setMaximumSize(QSize(16777215, 24))
        self.label_148.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_247.addWidget(self.label_148)


        self.verticalLayout_2.addWidget(self.frame_406)

        self.frame_420 = QFrame(self.scrollAreaWidgetContents)
        self.frame_420.setObjectName(u"frame_420")
        self.frame_420.setMinimumSize(QSize(0, 24))
        self.frame_420.setMaximumSize(QSize(16777215, 24))
        self.frame_420.setStyleSheet(u"")
        self.horizontalLayout_254 = QHBoxLayout(self.frame_420)
        self.horizontalLayout_254.setSpacing(6)
        self.horizontalLayout_254.setObjectName(u"horizontalLayout_254")
        self.horizontalLayout_254.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_228 = QLineEdit(self.frame_420)
        self.lineEdit_228.setObjectName(u"lineEdit_228")
        sizePolicy2.setHeightForWidth(self.lineEdit_228.sizePolicy().hasHeightForWidth())
        self.lineEdit_228.setSizePolicy(sizePolicy2)
        self.lineEdit_228.setMinimumSize(QSize(50, 24))
        self.lineEdit_228.setMaximumSize(QSize(50, 24))
        self.lineEdit_228.setSizeIncrement(QSize(0, 0))
        self.lineEdit_228.setBaseSize(QSize(0, 18))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_228.setPalette(palette17)
        self.lineEdit_228.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_228.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_254.addWidget(self.lineEdit_228)

        self.lineEdit_229 = QLineEdit(self.frame_420)
        self.lineEdit_229.setObjectName(u"lineEdit_229")
        sizePolicy2.setHeightForWidth(self.lineEdit_229.sizePolicy().hasHeightForWidth())
        self.lineEdit_229.setSizePolicy(sizePolicy2)
        self.lineEdit_229.setMinimumSize(QSize(50, 24))
        self.lineEdit_229.setMaximumSize(QSize(50, 24))
        self.lineEdit_229.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_254.addWidget(self.lineEdit_229)

        self.lineEdit_230 = QLineEdit(self.frame_420)
        self.lineEdit_230.setObjectName(u"lineEdit_230")
        sizePolicy2.setHeightForWidth(self.lineEdit_230.sizePolicy().hasHeightForWidth())
        self.lineEdit_230.setSizePolicy(sizePolicy2)
        self.lineEdit_230.setMinimumSize(QSize(50, 24))
        self.lineEdit_230.setMaximumSize(QSize(50, 24))
        self.lineEdit_230.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_254.addWidget(self.lineEdit_230)

        self.frame_421 = QFrame(self.frame_420)
        self.frame_421.setObjectName(u"frame_421")
        sizePolicy3.setHeightForWidth(self.frame_421.sizePolicy().hasHeightForWidth())
        self.frame_421.setSizePolicy(sizePolicy3)
        self.frame_421.setMinimumSize(QSize(0, 24))
        self.frame_421.setMaximumSize(QSize(16777215, 24))
        self.frame_421.setFont(font)
        self.frame_421.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_421.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_254.addWidget(self.frame_421)


        self.verticalLayout_2.addWidget(self.frame_420)

        self.frame_418 = QFrame(self.scrollAreaWidgetContents)
        self.frame_418.setObjectName(u"frame_418")
        self.frame_418.setMinimumSize(QSize(0, 24))
        self.frame_418.setMaximumSize(QSize(16777215, 24))
        self.frame_418.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_418.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_253 = QHBoxLayout(self.frame_418)
        self.horizontalLayout_253.setSpacing(0)
        self.horizontalLayout_253.setObjectName(u"horizontalLayout_253")
        self.horizontalLayout_253.setContentsMargins(32, 0, 0, 0)
        self.frame_419 = QFrame(self.frame_418)
        self.frame_419.setObjectName(u"frame_419")
        self.frame_419.setMaximumSize(QSize(0, 24))
        self.frame_419.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_419.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_419.setLineWidth(0)

        self.horizontalLayout_253.addWidget(self.frame_419)

        self.label_153 = QLabel(self.frame_418)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMinimumSize(QSize(0, 24))
        self.label_153.setMaximumSize(QSize(16777215, 24))
        self.label_153.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_253.addWidget(self.label_153)


        self.verticalLayout_2.addWidget(self.frame_418)

        self.frame_413 = QFrame(self.scrollAreaWidgetContents)
        self.frame_413.setObjectName(u"frame_413")
        self.frame_413.setMinimumSize(QSize(0, 24))
        self.frame_413.setMaximumSize(QSize(16777215, 24))
        self.frame_413.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_413.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_251 = QHBoxLayout(self.frame_413)
        self.horizontalLayout_251.setSpacing(0)
        self.horizontalLayout_251.setObjectName(u"horizontalLayout_251")
        self.horizontalLayout_251.setContentsMargins(32, 0, 0, 0)
        self.frame_414 = QFrame(self.frame_413)
        self.frame_414.setObjectName(u"frame_414")
        self.frame_414.setMinimumSize(QSize(0, 24))
        self.frame_414.setMaximumSize(QSize(0, 24))
        self.frame_414.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_414.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_251.addWidget(self.frame_414)

        self.comboBox_26 = QComboBox(self.frame_413)
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.setObjectName(u"comboBox_26")
        self.comboBox_26.setMinimumSize(QSize(0, 24))
        self.comboBox_26.setMaximumSize(QSize(80, 24))
        self.comboBox_26.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_251.addWidget(self.comboBox_26)

        self.frame_415 = QFrame(self.frame_413)
        self.frame_415.setObjectName(u"frame_415")
        self.frame_415.setMinimumSize(QSize(0, 24))
        self.frame_415.setMaximumSize(QSize(16777215, 24))
        self.frame_415.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_415.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_251.addWidget(self.frame_415)


        self.verticalLayout_2.addWidget(self.frame_413)

        self.frame_416 = QFrame(self.scrollAreaWidgetContents)
        self.frame_416.setObjectName(u"frame_416")
        self.frame_416.setMinimumSize(QSize(0, 24))
        self.frame_416.setMaximumSize(QSize(16777215, 24))
        self.frame_416.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_416.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_252 = QHBoxLayout(self.frame_416)
        self.horizontalLayout_252.setSpacing(0)
        self.horizontalLayout_252.setObjectName(u"horizontalLayout_252")
        self.horizontalLayout_252.setContentsMargins(32, 0, 0, 0)
        self.frame_417 = QFrame(self.frame_416)
        self.frame_417.setObjectName(u"frame_417")
        self.frame_417.setMaximumSize(QSize(0, 24))
        self.frame_417.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_417.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_417.setLineWidth(0)

        self.horizontalLayout_252.addWidget(self.frame_417)

        self.label_152 = QLabel(self.frame_416)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setMinimumSize(QSize(0, 24))
        self.label_152.setMaximumSize(QSize(16777215, 24))
        self.label_152.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_252.addWidget(self.label_152)


        self.verticalLayout_2.addWidget(self.frame_416)

        self.frame_422 = QFrame(self.scrollAreaWidgetContents)
        self.frame_422.setObjectName(u"frame_422")
        self.frame_422.setMinimumSize(QSize(0, 24))
        self.frame_422.setMaximumSize(QSize(16777215, 24))
        self.frame_422.setStyleSheet(u"")
        self.horizontalLayout_255 = QHBoxLayout(self.frame_422)
        self.horizontalLayout_255.setSpacing(6)
        self.horizontalLayout_255.setObjectName(u"horizontalLayout_255")
        self.horizontalLayout_255.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_231 = QLineEdit(self.frame_422)
        self.lineEdit_231.setObjectName(u"lineEdit_231")
        sizePolicy2.setHeightForWidth(self.lineEdit_231.sizePolicy().hasHeightForWidth())
        self.lineEdit_231.setSizePolicy(sizePolicy2)
        self.lineEdit_231.setMinimumSize(QSize(50, 24))
        self.lineEdit_231.setMaximumSize(QSize(50, 24))
        self.lineEdit_231.setSizeIncrement(QSize(0, 0))
        self.lineEdit_231.setBaseSize(QSize(0, 18))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_231.setPalette(palette18)
        self.lineEdit_231.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_231.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_255.addWidget(self.lineEdit_231)

        self.lineEdit_232 = QLineEdit(self.frame_422)
        self.lineEdit_232.setObjectName(u"lineEdit_232")
        sizePolicy2.setHeightForWidth(self.lineEdit_232.sizePolicy().hasHeightForWidth())
        self.lineEdit_232.setSizePolicy(sizePolicy2)
        self.lineEdit_232.setMinimumSize(QSize(50, 24))
        self.lineEdit_232.setMaximumSize(QSize(50, 24))
        self.lineEdit_232.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_255.addWidget(self.lineEdit_232)

        self.lineEdit_233 = QLineEdit(self.frame_422)
        self.lineEdit_233.setObjectName(u"lineEdit_233")
        sizePolicy2.setHeightForWidth(self.lineEdit_233.sizePolicy().hasHeightForWidth())
        self.lineEdit_233.setSizePolicy(sizePolicy2)
        self.lineEdit_233.setMinimumSize(QSize(50, 24))
        self.lineEdit_233.setMaximumSize(QSize(50, 24))
        self.lineEdit_233.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_255.addWidget(self.lineEdit_233)

        self.lineEdit_234 = QLineEdit(self.frame_422)
        self.lineEdit_234.setObjectName(u"lineEdit_234")
        sizePolicy2.setHeightForWidth(self.lineEdit_234.sizePolicy().hasHeightForWidth())
        self.lineEdit_234.setSizePolicy(sizePolicy2)
        self.lineEdit_234.setMinimumSize(QSize(50, 24))
        self.lineEdit_234.setMaximumSize(QSize(50, 24))
        self.lineEdit_234.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_255.addWidget(self.lineEdit_234)

        self.frame_423 = QFrame(self.frame_422)
        self.frame_423.setObjectName(u"frame_423")
        sizePolicy3.setHeightForWidth(self.frame_423.sizePolicy().hasHeightForWidth())
        self.frame_423.setSizePolicy(sizePolicy3)
        self.frame_423.setMinimumSize(QSize(0, 24))
        self.frame_423.setMaximumSize(QSize(16777215, 24))
        self.frame_423.setFont(font)
        self.frame_423.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_423.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_255.addWidget(self.frame_423)


        self.verticalLayout_2.addWidget(self.frame_422)

        self.label_172 = QLabel(self.scrollAreaWidgetContents)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMinimumSize(QSize(0, 40))
        self.label_172.setMaximumSize(QSize(16777215, 40))
        self.label_172.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.label_172)

        self.frame_449 = QFrame(self.scrollAreaWidgetContents)
        self.frame_449.setObjectName(u"frame_449")
        self.frame_449.setMinimumSize(QSize(0, 24))
        self.frame_449.setMaximumSize(QSize(16777215, 24))
        self.frame_449.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_449.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_287 = QHBoxLayout(self.frame_449)
        self.horizontalLayout_287.setSpacing(0)
        self.horizontalLayout_287.setObjectName(u"horizontalLayout_287")
        self.horizontalLayout_287.setContentsMargins(32, 0, 0, 0)
        self.frame_454 = QFrame(self.frame_449)
        self.frame_454.setObjectName(u"frame_454")
        self.frame_454.setMaximumSize(QSize(0, 24))
        self.frame_454.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_454.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_454.setLineWidth(0)

        self.horizontalLayout_287.addWidget(self.frame_454)

        self.label_173 = QLabel(self.frame_449)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setMinimumSize(QSize(0, 24))
        self.label_173.setMaximumSize(QSize(16777215, 24))
        self.label_173.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_287.addWidget(self.label_173)


        self.verticalLayout_2.addWidget(self.frame_449)

        self.frame_472 = QFrame(self.scrollAreaWidgetContents)
        self.frame_472.setObjectName(u"frame_472")
        self.frame_472.setMinimumSize(QSize(0, 24))
        self.frame_472.setMaximumSize(QSize(16777215, 24))
        self.frame_472.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_472.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_293 = QHBoxLayout(self.frame_472)
        self.horizontalLayout_293.setSpacing(0)
        self.horizontalLayout_293.setObjectName(u"horizontalLayout_293")
        self.horizontalLayout_293.setContentsMargins(32, 0, 0, -1)
        self.frame_473 = QFrame(self.frame_472)
        self.frame_473.setObjectName(u"frame_473")
        self.frame_473.setMinimumSize(QSize(0, 24))
        self.frame_473.setMaximumSize(QSize(0, 24))
        self.frame_473.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_473.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_293.addWidget(self.frame_473)

        self.lineEdit_268 = QLineEdit(self.frame_472)
        self.lineEdit_268.setObjectName(u"lineEdit_268")
        self.lineEdit_268.setMinimumSize(QSize(80, 24))
        self.lineEdit_268.setMaximumSize(QSize(80, 24))
        self.lineEdit_268.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_293.addWidget(self.lineEdit_268)

        self.frame_474 = QFrame(self.frame_472)
        self.frame_474.setObjectName(u"frame_474")
        self.frame_474.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_474.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_293.addWidget(self.frame_474)


        self.verticalLayout_2.addWidget(self.frame_472)

        self.frame_456 = QFrame(self.scrollAreaWidgetContents)
        self.frame_456.setObjectName(u"frame_456")
        self.frame_456.setMinimumSize(QSize(0, 24))
        self.frame_456.setMaximumSize(QSize(16777215, 24))
        self.frame_456.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_456.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_288 = QHBoxLayout(self.frame_456)
        self.horizontalLayout_288.setSpacing(0)
        self.horizontalLayout_288.setObjectName(u"horizontalLayout_288")
        self.horizontalLayout_288.setContentsMargins(32, 0, 0, 0)
        self.frame_457 = QFrame(self.frame_456)
        self.frame_457.setObjectName(u"frame_457")
        self.frame_457.setMaximumSize(QSize(0, 24))
        self.frame_457.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_457.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_457.setLineWidth(0)

        self.horizontalLayout_288.addWidget(self.frame_457)

        self.label_174 = QLabel(self.frame_456)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setMinimumSize(QSize(0, 24))
        self.label_174.setMaximumSize(QSize(16777215, 24))
        self.label_174.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_288.addWidget(self.label_174)


        self.verticalLayout_2.addWidget(self.frame_456)

        self.frame_460 = QFrame(self.scrollAreaWidgetContents)
        self.frame_460.setObjectName(u"frame_460")
        self.frame_460.setMinimumSize(QSize(0, 24))
        self.frame_460.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_289 = QHBoxLayout(self.frame_460)
        self.horizontalLayout_289.setObjectName(u"horizontalLayout_289")
        self.horizontalLayout_289.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_266 = QLineEdit(self.frame_460)
        self.lineEdit_266.setObjectName(u"lineEdit_266")
        self.lineEdit_266.setMinimumSize(QSize(70, 24))
        self.lineEdit_266.setMaximumSize(QSize(70, 24))
        self.lineEdit_266.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_289.addWidget(self.lineEdit_266)

        self.lineEdit_267 = QLineEdit(self.frame_460)
        self.lineEdit_267.setObjectName(u"lineEdit_267")
        self.lineEdit_267.setMinimumSize(QSize(70, 24))
        self.lineEdit_267.setMaximumSize(QSize(70, 24))
        self.lineEdit_267.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_289.addWidget(self.lineEdit_267)

        self.frame_462 = QFrame(self.frame_460)
        self.frame_462.setObjectName(u"frame_462")
        self.frame_462.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_462.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_289.addWidget(self.frame_462)


        self.verticalLayout_2.addWidget(self.frame_460)

        self.frame_432 = QFrame(self.scrollAreaWidgetContents)
        self.frame_432.setObjectName(u"frame_432")
        self.frame_432.setMinimumSize(QSize(0, 30))
        self.frame_432.setMaximumSize(QSize(16777215, 30))
        self.frame_432.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_432.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_285 = QHBoxLayout(self.frame_432)
        self.horizontalLayout_285.setSpacing(0)
        self.horizontalLayout_285.setObjectName(u"horizontalLayout_285")
        self.horizontalLayout_285.setContentsMargins(16, 0, 0, 0)
        self.label_167 = QLabel(self.frame_432)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setMinimumSize(QSize(0, 30))
        self.label_167.setMaximumSize(QSize(16777215, 30))
        self.label_167.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_285.addWidget(self.label_167)

        self.frame_436 = QFrame(self.frame_432)
        self.frame_436.setObjectName(u"frame_436")
        self.frame_436.setMinimumSize(QSize(0, 30))
        self.frame_436.setMaximumSize(QSize(0, 30))
        self.frame_436.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_436.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_285.addWidget(self.frame_436)


        self.verticalLayout_2.addWidget(self.frame_432)

        self.frame_469 = QFrame(self.scrollAreaWidgetContents)
        self.frame_469.setObjectName(u"frame_469")
        self.frame_469.setMinimumSize(QSize(0, 24))
        self.frame_469.setMaximumSize(QSize(16777215, 24))
        self.frame_469.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_469.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_291 = QHBoxLayout(self.frame_469)
        self.horizontalLayout_291.setSpacing(0)
        self.horizontalLayout_291.setObjectName(u"horizontalLayout_291")
        self.horizontalLayout_291.setContentsMargins(32, 0, 0, 0)
        self.frame_470 = QFrame(self.frame_469)
        self.frame_470.setObjectName(u"frame_470")
        self.frame_470.setMaximumSize(QSize(0, 24))
        self.frame_470.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_470.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_470.setLineWidth(0)

        self.horizontalLayout_291.addWidget(self.frame_470)

        self.label_176 = QLabel(self.frame_469)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setMinimumSize(QSize(0, 24))
        self.label_176.setMaximumSize(QSize(16777215, 24))
        self.label_176.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_291.addWidget(self.label_176)


        self.verticalLayout_2.addWidget(self.frame_469)

        self.frame_477 = QFrame(self.scrollAreaWidgetContents)
        self.frame_477.setObjectName(u"frame_477")
        self.frame_477.setMinimumSize(QSize(0, 24))
        self.frame_477.setMaximumSize(QSize(16777215, 24))
        self.frame_477.setStyleSheet(u"")
        self.horizontalLayout_295 = QHBoxLayout(self.frame_477)
        self.horizontalLayout_295.setSpacing(6)
        self.horizontalLayout_295.setObjectName(u"horizontalLayout_295")
        self.horizontalLayout_295.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_269 = QLineEdit(self.frame_477)
        self.lineEdit_269.setObjectName(u"lineEdit_269")
        sizePolicy2.setHeightForWidth(self.lineEdit_269.sizePolicy().hasHeightForWidth())
        self.lineEdit_269.setSizePolicy(sizePolicy2)
        self.lineEdit_269.setMinimumSize(QSize(50, 24))
        self.lineEdit_269.setMaximumSize(QSize(50, 24))
        self.lineEdit_269.setSizeIncrement(QSize(0, 0))
        self.lineEdit_269.setBaseSize(QSize(0, 18))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_269.setPalette(palette19)
        self.lineEdit_269.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_269.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_295.addWidget(self.lineEdit_269)

        self.lineEdit_270 = QLineEdit(self.frame_477)
        self.lineEdit_270.setObjectName(u"lineEdit_270")
        sizePolicy2.setHeightForWidth(self.lineEdit_270.sizePolicy().hasHeightForWidth())
        self.lineEdit_270.setSizePolicy(sizePolicy2)
        self.lineEdit_270.setMinimumSize(QSize(50, 24))
        self.lineEdit_270.setMaximumSize(QSize(50, 24))
        self.lineEdit_270.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_295.addWidget(self.lineEdit_270)

        self.lineEdit_271 = QLineEdit(self.frame_477)
        self.lineEdit_271.setObjectName(u"lineEdit_271")
        sizePolicy2.setHeightForWidth(self.lineEdit_271.sizePolicy().hasHeightForWidth())
        self.lineEdit_271.setSizePolicy(sizePolicy2)
        self.lineEdit_271.setMinimumSize(QSize(50, 24))
        self.lineEdit_271.setMaximumSize(QSize(50, 24))
        self.lineEdit_271.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_295.addWidget(self.lineEdit_271)

        self.lineEdit_272 = QLineEdit(self.frame_477)
        self.lineEdit_272.setObjectName(u"lineEdit_272")
        sizePolicy2.setHeightForWidth(self.lineEdit_272.sizePolicy().hasHeightForWidth())
        self.lineEdit_272.setSizePolicy(sizePolicy2)
        self.lineEdit_272.setMinimumSize(QSize(50, 24))
        self.lineEdit_272.setMaximumSize(QSize(50, 24))
        self.lineEdit_272.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_295.addWidget(self.lineEdit_272)

        self.frame_478 = QFrame(self.frame_477)
        self.frame_478.setObjectName(u"frame_478")
        sizePolicy3.setHeightForWidth(self.frame_478.sizePolicy().hasHeightForWidth())
        self.frame_478.setSizePolicy(sizePolicy3)
        self.frame_478.setMinimumSize(QSize(0, 24))
        self.frame_478.setMaximumSize(QSize(16777215, 24))
        self.frame_478.setFont(font)
        self.frame_478.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_478.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_295.addWidget(self.frame_478)


        self.verticalLayout_2.addWidget(self.frame_477)

        self.frame_471 = QFrame(self.scrollAreaWidgetContents)
        self.frame_471.setObjectName(u"frame_471")
        self.frame_471.setMinimumSize(QSize(0, 20))
        self.frame_471.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_292 = QHBoxLayout(self.frame_471)
        self.horizontalLayout_292.setSpacing(5)
        self.horizontalLayout_292.setObjectName(u"horizontalLayout_292")
        self.horizontalLayout_292.setContentsMargins(32, 0, 0, 0)
        self.label_177 = QLabel(self.frame_471)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setMinimumSize(QSize(195, 0))
        self.label_177.setMaximumSize(QSize(195, 24))
        self.label_177.setStyleSheet(u"")

        self.horizontalLayout_292.addWidget(self.label_177)

        self.checkBox_22 = QCheckBox(self.frame_471)
        self.checkBox_22.setObjectName(u"checkBox_22")
        self.checkBox_22.setMaximumSize(QSize(16777215, 24))
        self.checkBox_22.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.checkBox_22.setIconSize(QSize(18, 18))
        self.checkBox_22.setChecked(False)
        self.checkBox_22.setTristate(False)

        self.horizontalLayout_292.addWidget(self.checkBox_22)


        self.verticalLayout_2.addWidget(self.frame_471)

        self.frame_424 = QFrame(self.scrollAreaWidgetContents)
        self.frame_424.setObjectName(u"frame_424")
        self.frame_424.setMinimumSize(QSize(0, 24))
        self.frame_424.setMaximumSize(QSize(16777215, 24))
        self.frame_424.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_424.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_284 = QHBoxLayout(self.frame_424)
        self.horizontalLayout_284.setSpacing(0)
        self.horizontalLayout_284.setObjectName(u"horizontalLayout_284")
        self.horizontalLayout_284.setContentsMargins(32, 0, 0, 0)
        self.frame_428 = QFrame(self.frame_424)
        self.frame_428.setObjectName(u"frame_428")
        self.frame_428.setMaximumSize(QSize(0, 24))
        self.frame_428.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_428.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_428.setLineWidth(0)

        self.horizontalLayout_284.addWidget(self.frame_428)

        self.label_164 = QLabel(self.frame_424)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setMinimumSize(QSize(0, 24))
        self.label_164.setMaximumSize(QSize(16777215, 24))
        self.label_164.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_284.addWidget(self.label_164)


        self.verticalLayout_2.addWidget(self.frame_424)

        self.frame_441 = QFrame(self.scrollAreaWidgetContents)
        self.frame_441.setObjectName(u"frame_441")
        self.frame_441.setMinimumSize(QSize(0, 24))
        self.frame_441.setMaximumSize(QSize(16777215, 24))
        self.frame_441.setStyleSheet(u"")
        self.horizontalLayout_286 = QHBoxLayout(self.frame_441)
        self.horizontalLayout_286.setSpacing(6)
        self.horizontalLayout_286.setObjectName(u"horizontalLayout_286")
        self.horizontalLayout_286.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_263 = QLineEdit(self.frame_441)
        self.lineEdit_263.setObjectName(u"lineEdit_263")
        sizePolicy2.setHeightForWidth(self.lineEdit_263.sizePolicy().hasHeightForWidth())
        self.lineEdit_263.setSizePolicy(sizePolicy2)
        self.lineEdit_263.setMinimumSize(QSize(50, 24))
        self.lineEdit_263.setMaximumSize(QSize(50, 24))
        self.lineEdit_263.setSizeIncrement(QSize(0, 0))
        self.lineEdit_263.setBaseSize(QSize(0, 18))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_263.setPalette(palette20)
        self.lineEdit_263.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_263.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_286.addWidget(self.lineEdit_263)

        self.lineEdit_264 = QLineEdit(self.frame_441)
        self.lineEdit_264.setObjectName(u"lineEdit_264")
        sizePolicy2.setHeightForWidth(self.lineEdit_264.sizePolicy().hasHeightForWidth())
        self.lineEdit_264.setSizePolicy(sizePolicy2)
        self.lineEdit_264.setMinimumSize(QSize(50, 24))
        self.lineEdit_264.setMaximumSize(QSize(50, 24))
        self.lineEdit_264.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_286.addWidget(self.lineEdit_264)

        self.lineEdit_265 = QLineEdit(self.frame_441)
        self.lineEdit_265.setObjectName(u"lineEdit_265")
        sizePolicy2.setHeightForWidth(self.lineEdit_265.sizePolicy().hasHeightForWidth())
        self.lineEdit_265.setSizePolicy(sizePolicy2)
        self.lineEdit_265.setMinimumSize(QSize(50, 24))
        self.lineEdit_265.setMaximumSize(QSize(50, 24))
        self.lineEdit_265.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_286.addWidget(self.lineEdit_265)

        self.frame_445 = QFrame(self.frame_441)
        self.frame_445.setObjectName(u"frame_445")
        sizePolicy3.setHeightForWidth(self.frame_445.sizePolicy().hasHeightForWidth())
        self.frame_445.setSizePolicy(sizePolicy3)
        self.frame_445.setMinimumSize(QSize(0, 24))
        self.frame_445.setMaximumSize(QSize(16777215, 24))
        self.frame_445.setFont(font)
        self.frame_445.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_445.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_286.addWidget(self.frame_445)


        self.verticalLayout_2.addWidget(self.frame_441)

        self.frame_483 = QFrame(self.scrollAreaWidgetContents)
        self.frame_483.setObjectName(u"frame_483")
        self.frame_483.setMinimumSize(QSize(0, 24))
        self.frame_483.setMaximumSize(QSize(16777215, 24))
        self.frame_483.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_483.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_298 = QHBoxLayout(self.frame_483)
        self.horizontalLayout_298.setSpacing(0)
        self.horizontalLayout_298.setObjectName(u"horizontalLayout_298")
        self.horizontalLayout_298.setContentsMargins(32, 0, 0, 0)
        self.frame_484 = QFrame(self.frame_483)
        self.frame_484.setObjectName(u"frame_484")
        self.frame_484.setMaximumSize(QSize(0, 24))
        self.frame_484.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_484.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_484.setLineWidth(0)

        self.horizontalLayout_298.addWidget(self.frame_484)

        self.label_175 = QLabel(self.frame_483)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setMinimumSize(QSize(0, 24))
        self.label_175.setMaximumSize(QSize(16777215, 24))
        self.label_175.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_298.addWidget(self.label_175)


        self.verticalLayout_2.addWidget(self.frame_483)

        self.frame_464 = QFrame(self.scrollAreaWidgetContents)
        self.frame_464.setObjectName(u"frame_464")
        self.frame_464.setMinimumSize(QSize(0, 24))
        self.frame_464.setMaximumSize(QSize(16777215, 24))
        self.frame_464.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_464.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_290 = QHBoxLayout(self.frame_464)
        self.horizontalLayout_290.setSpacing(0)
        self.horizontalLayout_290.setObjectName(u"horizontalLayout_290")
        self.horizontalLayout_290.setContentsMargins(32, 0, 0, 0)
        self.frame_466 = QFrame(self.frame_464)
        self.frame_466.setObjectName(u"frame_466")
        self.frame_466.setMinimumSize(QSize(0, 24))
        self.frame_466.setMaximumSize(QSize(0, 24))
        self.frame_466.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_466.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_290.addWidget(self.frame_466)

        self.comboBox_29 = QComboBox(self.frame_464)
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.setObjectName(u"comboBox_29")
        self.comboBox_29.setMinimumSize(QSize(0, 24))
        self.comboBox_29.setMaximumSize(QSize(80, 24))
        self.comboBox_29.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_290.addWidget(self.comboBox_29)

        self.frame_468 = QFrame(self.frame_464)
        self.frame_468.setObjectName(u"frame_468")
        self.frame_468.setMinimumSize(QSize(0, 24))
        self.frame_468.setMaximumSize(QSize(16777215, 24))
        self.frame_468.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_468.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_290.addWidget(self.frame_468)


        self.verticalLayout_2.addWidget(self.frame_464)

        self.frame_481 = QFrame(self.scrollAreaWidgetContents)
        self.frame_481.setObjectName(u"frame_481")
        self.frame_481.setMinimumSize(QSize(0, 24))
        self.frame_481.setMaximumSize(QSize(16777215, 24))
        self.frame_481.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_481.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_297 = QHBoxLayout(self.frame_481)
        self.horizontalLayout_297.setSpacing(0)
        self.horizontalLayout_297.setObjectName(u"horizontalLayout_297")
        self.horizontalLayout_297.setContentsMargins(32, 0, 0, 0)
        self.frame_482 = QFrame(self.frame_481)
        self.frame_482.setObjectName(u"frame_482")
        self.frame_482.setMaximumSize(QSize(0, 24))
        self.frame_482.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_482.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_482.setLineWidth(0)

        self.horizontalLayout_297.addWidget(self.frame_482)

        self.label_179 = QLabel(self.frame_481)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setMinimumSize(QSize(0, 24))
        self.label_179.setMaximumSize(QSize(16777215, 24))
        self.label_179.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_297.addWidget(self.label_179)


        self.verticalLayout_2.addWidget(self.frame_481)

        self.frame_479 = QFrame(self.scrollAreaWidgetContents)
        self.frame_479.setObjectName(u"frame_479")
        self.frame_479.setMinimumSize(QSize(0, 24))
        self.frame_479.setMaximumSize(QSize(16777215, 24))
        self.frame_479.setStyleSheet(u"")
        self.horizontalLayout_296 = QHBoxLayout(self.frame_479)
        self.horizontalLayout_296.setSpacing(6)
        self.horizontalLayout_296.setObjectName(u"horizontalLayout_296")
        self.horizontalLayout_296.setContentsMargins(32, 0, 0, 0)
        self.lineEdit_273 = QLineEdit(self.frame_479)
        self.lineEdit_273.setObjectName(u"lineEdit_273")
        sizePolicy2.setHeightForWidth(self.lineEdit_273.sizePolicy().hasHeightForWidth())
        self.lineEdit_273.setSizePolicy(sizePolicy2)
        self.lineEdit_273.setMinimumSize(QSize(50, 24))
        self.lineEdit_273.setMaximumSize(QSize(50, 24))
        self.lineEdit_273.setSizeIncrement(QSize(0, 0))
        self.lineEdit_273.setBaseSize(QSize(0, 18))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_273.setPalette(palette21)
        self.lineEdit_273.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_273.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_296.addWidget(self.lineEdit_273)

        self.lineEdit_274 = QLineEdit(self.frame_479)
        self.lineEdit_274.setObjectName(u"lineEdit_274")
        sizePolicy2.setHeightForWidth(self.lineEdit_274.sizePolicy().hasHeightForWidth())
        self.lineEdit_274.setSizePolicy(sizePolicy2)
        self.lineEdit_274.setMinimumSize(QSize(50, 24))
        self.lineEdit_274.setMaximumSize(QSize(50, 24))
        self.lineEdit_274.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_296.addWidget(self.lineEdit_274)

        self.lineEdit_275 = QLineEdit(self.frame_479)
        self.lineEdit_275.setObjectName(u"lineEdit_275")
        sizePolicy2.setHeightForWidth(self.lineEdit_275.sizePolicy().hasHeightForWidth())
        self.lineEdit_275.setSizePolicy(sizePolicy2)
        self.lineEdit_275.setMinimumSize(QSize(50, 24))
        self.lineEdit_275.setMaximumSize(QSize(50, 24))
        self.lineEdit_275.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_296.addWidget(self.lineEdit_275)

        self.lineEdit_276 = QLineEdit(self.frame_479)
        self.lineEdit_276.setObjectName(u"lineEdit_276")
        sizePolicy2.setHeightForWidth(self.lineEdit_276.sizePolicy().hasHeightForWidth())
        self.lineEdit_276.setSizePolicy(sizePolicy2)
        self.lineEdit_276.setMinimumSize(QSize(50, 24))
        self.lineEdit_276.setMaximumSize(QSize(50, 24))
        self.lineEdit_276.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_296.addWidget(self.lineEdit_276)

        self.frame_480 = QFrame(self.frame_479)
        self.frame_480.setObjectName(u"frame_480")
        sizePolicy3.setHeightForWidth(self.frame_480.sizePolicy().hasHeightForWidth())
        self.frame_480.setSizePolicy(sizePolicy3)
        self.frame_480.setMinimumSize(QSize(0, 24))
        self.frame_480.setMaximumSize(QSize(16777215, 24))
        self.frame_480.setFont(font)
        self.frame_480.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_480.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_296.addWidget(self.frame_480)


        self.verticalLayout_2.addWidget(self.frame_479)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setMinimumSize(QSize(0, 0))
        self.tab_2.setMaximumSize(QSize(16777215, 16777215))
        self.tab_2.setStyleSheet(u"background: rgb(42, 42, 42);")
        self.horizontalLayout_205 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_205.setSpacing(0)
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.horizontalLayout_205.setContentsMargins(2, 6, 0, 0)
        self.textBrowser_2 = QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy5)
        self.textBrowser_2.setStyleSheet(u"border: none;")

        self.horizontalLayout_205.addWidget(self.textBrowser_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_13.addWidget(self.tabWidget)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy5.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy5)
        self.textBrowser.setStyleSheet(u"border-left: 2px solid white;\n"
"margin-left: 2px")

        self.horizontalLayout_13.addWidget(self.textBrowser)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u043d:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430", None))
        self.checkBox_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u0442\u0440\u0435\u043a\u0430:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043e\u0431\u043b\u043e\u0436\u043a\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u043b\u043e\u0436\u043a\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043e\u0431\u043b\u043e\u0436\u043a\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0442\u0440\u0435\u043a\u0430:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"right", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"left", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"up", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"down", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0442\u0440\u0435\u043a\u0430 1:", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.checkBox_3.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u">", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"<", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u">=", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"<=", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"==", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0442\u0440\u0435\u043a\u0430 2:", None))
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u0435\u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439:", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"right", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"left", None))
        self.comboBox_20.setItemText(2, QCoreApplication.translate("MainWindow", u"up", None))
        self.comboBox_20.setItemText(3, QCoreApplication.translate("MainWindow", u"down", None))

        self.label_102.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.lineEdit_151.setPlaceholderText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.lineEdit_152.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_153.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439:", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439 1:", None))
        self.lineEdit_157.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_158.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_159.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_160.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.checkBox_13.setText("")
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.lineEdit_154.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_155.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_156.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox_19.setItemText(0, QCoreApplication.translate("MainWindow", u">", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("MainWindow", u"<", None))
        self.comboBox_19.setItemText(2, QCoreApplication.translate("MainWindow", u">=", None))
        self.comboBox_19.setItemText(3, QCoreApplication.translate("MainWindow", u"<=", None))
        self.comboBox_19.setItemText(4, QCoreApplication.translate("MainWindow", u"==", None))

        self.label_113.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439 2:", None))
        self.lineEdit_161.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_162.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_163.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_164.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440 \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044f:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0431\u0430\u0440\u0430", None))
        self.lineEdit_165.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_166.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0431\u0430\u0440\u0430", None))
        self.lineEdit_167.setPlaceholderText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0431\u0430\u0440\u0430", None))
        self.lineEdit_183.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_184.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043f\u0435\u0440\u0432\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0431\u0430\u0440\u0430:", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043f\u0435\u0440\u0432\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 1:", None))
        self.lineEdit_175.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_176.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_177.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_178.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.checkBox_14.setText("")
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.lineEdit_172.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_173.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_174.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u">", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("MainWindow", u"<", None))
        self.comboBox_21.setItemText(2, QCoreApplication.translate("MainWindow", u">=", None))
        self.comboBox_21.setItemText(3, QCoreApplication.translate("MainWindow", u"<=", None))
        self.comboBox_21.setItemText(4, QCoreApplication.translate("MainWindow", u"==", None))

        self.label_119.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043f\u0435\u0440\u0432\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 2:", None))
        self.lineEdit_168.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_169.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_170.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_171.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0432\u0442\u043e\u0440\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430:", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0432\u0442\u043e\u0440\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 1:", None))
        self.lineEdit_179.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_180.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_181.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_182.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.checkBox_16.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.lineEdit_190.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_191.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_192.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox_23.setItemText(0, QCoreApplication.translate("MainWindow", u">", None))
        self.comboBox_23.setItemText(1, QCoreApplication.translate("MainWindow", u"<", None))
        self.comboBox_23.setItemText(2, QCoreApplication.translate("MainWindow", u">=", None))
        self.comboBox_23.setItemText(3, QCoreApplication.translate("MainWindow", u"<=", None))
        self.comboBox_23.setItemText(4, QCoreApplication.translate("MainWindow", u"==", None))

        self.label_126.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0432\u0442\u043e\u0440\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 2:", None))
        self.lineEdit_186.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_187.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_188.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_189.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0435\u043d\u0434\u043b\u0435\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430:", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0445\u0435\u043d\u0434\u043b\u0435\u0440\u0430 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430", None))
        self.lineEdit_194.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_195.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0445\u0435\u043d\u0434\u043b\u0435\u0440\u0430 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430", None))
        self.lineEdit_223.setPlaceholderText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0445\u0435\u043d\u0434\u043b\u0435\u0440\u0430 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0432\u0442\u043e\u0440\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 1:", None))
        self.lineEdit_210.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_211.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_212.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_213.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.checkBox_18.setText("")
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.lineEdit_214.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_215.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_216.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox_25.setItemText(0, QCoreApplication.translate("MainWindow", u">", None))
        self.comboBox_25.setItemText(1, QCoreApplication.translate("MainWindow", u"<", None))
        self.comboBox_25.setItemText(2, QCoreApplication.translate("MainWindow", u">=", None))
        self.comboBox_25.setItemText(3, QCoreApplication.translate("MainWindow", u"<=", None))
        self.comboBox_25.setItemText(4, QCoreApplication.translate("MainWindow", u"==", None))

        self.label_143.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0432\u0442\u043e\u0440\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 2:", None))
        self.lineEdit_217.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_218.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_219.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_220.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u0442\u0440\u0435\u043a\u0430:", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430", None))
        self.lineEdit_196.setPlaceholderText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430", None))
        self.lineEdit_221.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_222.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430:", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430 1:", None))
        self.lineEdit_224.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_225.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_226.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_227.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.checkBox_19.setText("")
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.lineEdit_228.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_229.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_230.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox_26.setItemText(0, QCoreApplication.translate("MainWindow", u">", None))
        self.comboBox_26.setItemText(1, QCoreApplication.translate("MainWindow", u"<", None))
        self.comboBox_26.setItemText(2, QCoreApplication.translate("MainWindow", u">=", None))
        self.comboBox_26.setItemText(3, QCoreApplication.translate("MainWindow", u"<=", None))
        self.comboBox_26.setItemText(4, QCoreApplication.translate("MainWindow", u"==", None))

        self.label_152.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430 2:", None))
        self.lineEdit_231.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_232.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_233.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_234.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0440\u0435\u043a\u0430:", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.lineEdit_268.setPlaceholderText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.lineEdit_266.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_267.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430:", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430 1:", None))
        self.lineEdit_269.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_270.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_271.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_272.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.checkBox_22.setText("")
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.lineEdit_263.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_264.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_265.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox_29.setItemText(0, QCoreApplication.translate("MainWindow", u">", None))
        self.comboBox_29.setItemText(1, QCoreApplication.translate("MainWindow", u"<", None))
        self.comboBox_29.setItemText(2, QCoreApplication.translate("MainWindow", u">=", None))
        self.comboBox_29.setItemText(3, QCoreApplication.translate("MainWindow", u"<=", None))
        self.comboBox_29.setItemText(4, QCoreApplication.translate("MainWindow", u"==", None))

        self.label_179.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430 2:", None))
        self.lineEdit_273.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lineEdit_274.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lineEdit_275.setPlaceholderText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_276.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0432\u0438\u0434\u0436\u0435\u0442\u044b", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:700;\">\u0412 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u0417\u0434\u0435\u0441\u044c \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u044b\u0445 \u0430\u0434\u0434\u043e\u043d\u043e\u0432(\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u0432\u0438\u0434\u0436\u0435\u0442\u044b \u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b)</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0434\u043e\u043d\u044b", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:700;\">\u0412 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u042d\u0442\u043e \u043f\u043e\u043b\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438(\u0431\u0443\u0434\u0435\u0442 \u0433\u043e\u0442\u043e\u0432\u043e \u0432 \u0431\u0435\u0442\u0435)</span></p></body></html>", None))
    # retranslateUi

if __name__ == "__main__":
    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())