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
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDialog, QFrame, QHBoxLayout, QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)
from clickableWidgets import ClickableLabel, ClickableLineEdit
from markdownToHtml import markdownToHtml

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(965, 773)
        Dialog.setMinimumSize(QSize(750, 0))
        Dialog.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        Dialog.setStyleSheet(u"background-color: rgb(18, 18, 18);\n"
"color: white;\n"
"font-size: 14px;")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 6)
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_26.setSpacing(2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_5)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
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
        self.base_widgets = QWidget()
        self.base_widgets.setObjectName(u"base_widgets")
        self.base_widgets.setMinimumSize(QSize(0, 0))
        self.base_widgets.setMaximumSize(QSize(16777215, 16777215))
        self.base_widgets.setStyleSheet(u"background: rgb(42, 42, 42);")
        self.horizontalLayout_3 = QHBoxLayout(self.base_widgets)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.baseWidgets_srollArea = QScrollArea(self.base_widgets)
        self.baseWidgets_srollArea.setObjectName(u"baseWidgets_srollArea")
        self.baseWidgets_srollArea.setStyleSheet(u"border: none;")
        self.baseWidgets_srollArea.setLineWidth(0)
        self.baseWidgets_srollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.baseWidgets_srollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.baseWidgets_srollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.baseWidgets_srollArea.setWidgetResizable(True)
        self.baseWidgets = QWidget()
        self.baseWidgets.setObjectName(u"baseWidgets")
        self.baseWidgets.setGeometry(QRect(0, -1272, 388, 3653))
        self.verticalLayout_2 = QVBoxLayout(self.baseWidgets)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 9, 0, 12)
        self.background = ClickableLabel(self.baseWidgets)
        self.background.setObjectName(u"background")
        self.background.setMinimumSize(QSize(0, 40))
        self.background.setMaximumSize(QSize(16777215, 40))
        self.background.setStyleSheet(u"font-size: 26px;")
        self.background.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.background)

        self.fixedColor_background = QFrame(self.baseWidgets)
        self.fixedColor_background.setObjectName(u"fixedColor_background")
        self.fixedColor_background.setMinimumSize(QSize(0, 20))
        self.fixedColor_background.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_4 = QHBoxLayout(self.fixedColor_background)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(16, 0, 0, 0)
        self.fixedColorBackground = ClickableLabel(self.fixedColor_background)
        self.fixedColorBackground.setObjectName(u"fixedColorBackground")
        self.fixedColorBackground.setMinimumSize(QSize(195, 0))
        self.fixedColorBackground.setMaximumSize(QSize(195, 24))
        self.fixedColorBackground.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.fixedColorBackground)

        self.fixedColorBackgroundCheckBox = QCheckBox(self.fixedColor_background)
        self.fixedColorBackgroundCheckBox.setObjectName(u"fixedColorBackgroundCheckBox")
        self.fixedColorBackgroundCheckBox.setMaximumSize(QSize(16777215, 24))
        self.fixedColorBackgroundCheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.fixedColorBackgroundCheckBox.setIconSize(QSize(18, 18))
        self.fixedColorBackgroundCheckBox.setChecked(False)
        self.fixedColorBackgroundCheckBox.setTristate(False)

        self.horizontalLayout_4.addWidget(self.fixedColorBackgroundCheckBox)


        self.verticalLayout_2.addWidget(self.fixedColor_background)

        self.background_color = QFrame(self.baseWidgets)
        self.background_color.setObjectName(u"background_color")
        self.background_color.setMinimumSize(QSize(0, 24))
        self.background_color.setMaximumSize(QSize(16777215, 24))
        self.background_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.background_color.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.background_color)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(16, 0, 0, 0)
        self.frame_4 = QFrame(self.background_color)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(0, 24))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(0)

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.backgroundColor = ClickableLabel(self.background_color)
        self.backgroundColor.setObjectName(u"backgroundColor")
        self.backgroundColor.setMinimumSize(QSize(0, 24))
        self.backgroundColor.setMaximumSize(QSize(16777215, 24))
        self.backgroundColor.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_5.addWidget(self.backgroundColor)


        self.verticalLayout_2.addWidget(self.background_color)

        self.background_rgb = QFrame(self.baseWidgets)
        self.background_rgb.setObjectName(u"background_rgb")
        self.background_rgb.setMinimumSize(QSize(0, 24))
        self.background_rgb.setMaximumSize(QSize(16777215, 24))
        self.background_rgb.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.background_rgb)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 0, 0, 0)
        self.backgroundR = ClickableLineEdit(self.background_rgb)
        self.backgroundR.setObjectName(u"backgroundR")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backgroundR.sizePolicy().hasHeightForWidth())
        self.backgroundR.setSizePolicy(sizePolicy1)
        self.backgroundR.setMinimumSize(QSize(50, 24))
        self.backgroundR.setMaximumSize(QSize(50, 24))
        self.backgroundR.setSizeIncrement(QSize(0, 0))
        self.backgroundR.setBaseSize(QSize(0, 18))
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
        self.backgroundR.setPalette(palette)
        self.backgroundR.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.backgroundR.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_2.addWidget(self.backgroundR)

        self.backgroundG = ClickableLineEdit(self.background_rgb)
        self.backgroundG.setObjectName(u"backgroundG")
        sizePolicy1.setHeightForWidth(self.backgroundG.sizePolicy().hasHeightForWidth())
        self.backgroundG.setSizePolicy(sizePolicy1)
        self.backgroundG.setMinimumSize(QSize(50, 24))
        self.backgroundG.setMaximumSize(QSize(50, 24))
        self.backgroundG.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_2.addWidget(self.backgroundG)

        self.backgroundB = ClickableLineEdit(self.background_rgb)
        self.backgroundB.setObjectName(u"backgroundB")
        sizePolicy1.setHeightForWidth(self.backgroundB.sizePolicy().hasHeightForWidth())
        self.backgroundB.setSizePolicy(sizePolicy1)
        self.backgroundB.setMinimumSize(QSize(50, 24))
        self.backgroundB.setMaximumSize(QSize(50, 24))
        self.backgroundB.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_2.addWidget(self.backgroundB)

        self.frame_2 = QFrame(self.background_rgb)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(99)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(0, 24))
        self.frame_2.setMaximumSize(QSize(16777215, 24))
        font = QFont()
        font.setBold(False)
        font.setKerning(True)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.background_rgb)

        self.albumImg = ClickableLabel(self.baseWidgets)
        self.albumImg.setObjectName(u"albumImg")
        self.albumImg.setMinimumSize(QSize(0, 40))
        self.albumImg.setMaximumSize(QSize(16777215, 40))
        self.albumImg.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.albumImg)

        self.albumImg_size = QFrame(self.baseWidgets)
        self.albumImg_size.setObjectName(u"albumImg_size")
        self.albumImg_size.setMinimumSize(QSize(0, 24))
        self.albumImg_size.setMaximumSize(QSize(16777215, 24))
        self.albumImg_size.setFrameShape(QFrame.Shape.StyledPanel)
        self.albumImg_size.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.albumImg_size)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 0, 0, 0)
        self.frame_6 = QFrame(self.albumImg_size)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(0, 24))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_6.addWidget(self.frame_6)

        self.albumImgSize = ClickableLabel(self.albumImg_size)
        self.albumImgSize.setObjectName(u"albumImgSize")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(24)
        sizePolicy3.setHeightForWidth(self.albumImgSize.sizePolicy().hasHeightForWidth())
        self.albumImgSize.setSizePolicy(sizePolicy3)
        self.albumImgSize.setMinimumSize(QSize(0, 24))
        self.albumImgSize.setMaximumSize(QSize(16777215, 24))
        self.albumImgSize.setStyleSheet(u"")
        self.albumImgSize.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_6.addWidget(self.albumImgSize)


        self.verticalLayout_2.addWidget(self.albumImg_size)

        self.albumImg_sizePx = QFrame(self.baseWidgets)
        self.albumImg_sizePx.setObjectName(u"albumImg_sizePx")
        self.albumImg_sizePx.setMinimumSize(QSize(0, 24))
        self.albumImg_sizePx.setMaximumSize(QSize(16777215, 24))
        self.albumImg_sizePx.setFrameShape(QFrame.Shape.StyledPanel)
        self.albumImg_sizePx.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.albumImg_sizePx)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(16, 0, 0, 0)
        self.frame_11 = QFrame(self.albumImg_sizePx)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 24))
        self.frame_11.setMaximumSize(QSize(0, 24))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.frame_11)

        self.albumImgSizePx = ClickableLineEdit(self.albumImg_sizePx)
        self.albumImgSizePx.setObjectName(u"albumImgSizePx")
        self.albumImgSizePx.setEnabled(True)
        self.albumImgSizePx.setMinimumSize(QSize(80, 24))
        self.albumImgSizePx.setMaximumSize(QSize(80, 24))
        self.albumImgSizePx.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_7.addWidget(self.albumImgSizePx)

        self.frame_12 = QFrame(self.albumImg_sizePx)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.albumImg_sizePx)

        self.albumImg_radius = QFrame(self.baseWidgets)
        self.albumImg_radius.setObjectName(u"albumImg_radius")
        self.albumImg_radius.setMinimumSize(QSize(0, 24))
        self.albumImg_radius.setMaximumSize(QSize(16777215, 24))
        self.albumImg_radius.setFrameShape(QFrame.Shape.StyledPanel)
        self.albumImg_radius.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.albumImg_radius)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 0, 0, 0)
        self.frame_1 = QFrame(self.albumImg_radius)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMinimumSize(QSize(0, 24))
        self.frame_1.setMaximumSize(QSize(0, 24))
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_8.addWidget(self.frame_1)

        self.albumImgRadius = ClickableLabel(self.albumImg_radius)
        self.albumImgRadius.setObjectName(u"albumImgRadius")
        sizePolicy3.setHeightForWidth(self.albumImgRadius.sizePolicy().hasHeightForWidth())
        self.albumImgRadius.setSizePolicy(sizePolicy3)
        self.albumImgRadius.setMinimumSize(QSize(0, 24))
        self.albumImgRadius.setMaximumSize(QSize(16777215, 24))
        self.albumImgRadius.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_8.addWidget(self.albumImgRadius)


        self.verticalLayout_2.addWidget(self.albumImg_radius)

        self.albumImg_radiusPx = QFrame(self.baseWidgets)
        self.albumImg_radiusPx.setObjectName(u"albumImg_radiusPx")
        self.albumImg_radiusPx.setMinimumSize(QSize(0, 24))
        self.albumImg_radiusPx.setMaximumSize(QSize(16777215, 24))
        self.albumImg_radiusPx.setFrameShape(QFrame.Shape.StyledPanel)
        self.albumImg_radiusPx.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.albumImg_radiusPx)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(16, 0, 0, -1)
        self.frame_17 = QFrame(self.albumImg_radiusPx)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 24))
        self.frame_17.setMaximumSize(QSize(0, 24))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_10.addWidget(self.frame_17)

        self.albumImgRadiusPx = ClickableLineEdit(self.albumImg_radiusPx)
        self.albumImgRadiusPx.setObjectName(u"albumImgRadiusPx")
        self.albumImgRadiusPx.setMinimumSize(QSize(80, 24))
        self.albumImgRadiusPx.setMaximumSize(QSize(80, 24))
        self.albumImgRadiusPx.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_10.addWidget(self.albumImgRadiusPx)

        self.frame_18 = QFrame(self.albumImg_radiusPx)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_10.addWidget(self.frame_18)


        self.verticalLayout_2.addWidget(self.albumImg_radiusPx)

        self.albumImg_position = QFrame(self.baseWidgets)
        self.albumImg_position.setObjectName(u"albumImg_position")
        self.albumImg_position.setMinimumSize(QSize(0, 24))
        self.albumImg_position.setMaximumSize(QSize(16777215, 24))
        self.albumImg_position.setFrameShape(QFrame.Shape.StyledPanel)
        self.albumImg_position.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.albumImg_position)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, 0, 0, 0)
        self.frame_19 = QFrame(self.albumImg_position)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(0, 24))
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_9.addWidget(self.frame_19)

        self.albumImgPosition = ClickableLabel(self.albumImg_position)
        self.albumImgPosition.setObjectName(u"albumImgPosition")
        sizePolicy3.setHeightForWidth(self.albumImgPosition.sizePolicy().hasHeightForWidth())
        self.albumImgPosition.setSizePolicy(sizePolicy3)
        self.albumImgPosition.setMinimumSize(QSize(0, 24))
        self.albumImgPosition.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_9.addWidget(self.albumImgPosition)


        self.verticalLayout_2.addWidget(self.albumImg_position)

        self.albumImg_positionXY = QFrame(self.baseWidgets)
        self.albumImg_positionXY.setObjectName(u"albumImg_positionXY")
        self.albumImg_positionXY.setMinimumSize(QSize(0, 24))
        self.albumImg_positionXY.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_11 = QHBoxLayout(self.albumImg_positionXY)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(16, 0, 0, 0)
        self.albumImgPositionX = ClickableLineEdit(self.albumImg_positionXY)
        self.albumImgPositionX.setObjectName(u"albumImgPositionX")
        self.albumImgPositionX.setMinimumSize(QSize(70, 24))
        self.albumImgPositionX.setMaximumSize(QSize(70, 24))
        self.albumImgPositionX.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_11.addWidget(self.albumImgPositionX)

        self.albumImgPositionY = ClickableLineEdit(self.albumImg_positionXY)
        self.albumImgPositionY.setObjectName(u"albumImgPositionY")
        self.albumImgPositionY.setMinimumSize(QSize(70, 24))
        self.albumImgPositionY.setMaximumSize(QSize(70, 24))
        self.albumImgPositionY.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_11.addWidget(self.albumImgPositionY)

        self.frame_9 = QFrame(self.albumImg_positionXY)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_11.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.albumImg_positionXY)

        self.trackName = ClickableLabel(self.baseWidgets)
        self.trackName.setObjectName(u"trackName")
        self.trackName.setMinimumSize(QSize(0, 40))
        self.trackName.setMaximumSize(QSize(16777215, 40))
        self.trackName.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.trackName)

        self.trackName_mode = QFrame(self.baseWidgets)
        self.trackName_mode.setObjectName(u"trackName_mode")
        self.trackName_mode.setMinimumSize(QSize(0, 24))
        self.trackName_mode.setMaximumSize(QSize(16777215, 24))
        self.trackName_mode.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_mode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.trackName_mode)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(16, 0, 0, 0)
        self.trackNameMode = ClickableLabel(self.trackName_mode)
        self.trackNameMode.setObjectName(u"trackNameMode")

        self.horizontalLayout_12.addWidget(self.trackNameMode)

        self.frame_23 = QFrame(self.trackName_mode)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 24))
        self.frame_23.setMaximumSize(QSize(0, 24))
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_12.addWidget(self.frame_23)


        self.verticalLayout_2.addWidget(self.trackName_mode)

        self.trackName_modeComboBox = QFrame(self.baseWidgets)
        self.trackName_modeComboBox.setObjectName(u"trackName_modeComboBox")
        self.trackName_modeComboBox.setMinimumSize(QSize(0, 24))
        self.trackName_modeComboBox.setMaximumSize(QSize(16777215, 24))
        self.trackName_modeComboBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_modeComboBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.trackName_modeComboBox)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(16, 0, 0, 0)
        self.frame_24 = QFrame(self.trackName_modeComboBox)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 24))
        self.frame_24.setMaximumSize(QSize(0, 24))
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_13.addWidget(self.frame_24)

        self.trackNameModeComboBox = QComboBox(self.trackName_modeComboBox)
        self.trackNameModeComboBox.addItem("")
        self.trackNameModeComboBox.addItem("")
        self.trackNameModeComboBox.addItem("")
        self.trackNameModeComboBox.addItem("")
        self.trackNameModeComboBox.setObjectName(u"trackNameModeComboBox")
        self.trackNameModeComboBox.setMinimumSize(QSize(0, 24))
        self.trackNameModeComboBox.setMaximumSize(QSize(80, 24))
        self.trackNameModeComboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_13.addWidget(self.trackNameModeComboBox)

        self.frame_25 = QFrame(self.trackName_modeComboBox)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 24))
        self.frame_25.setMaximumSize(QSize(16777215, 24))
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_13.addWidget(self.frame_25)


        self.verticalLayout_2.addWidget(self.trackName_modeComboBox)

        self.trackName_size = QFrame(self.baseWidgets)
        self.trackName_size.setObjectName(u"trackName_size")
        self.trackName_size.setMinimumSize(QSize(0, 24))
        self.trackName_size.setMaximumSize(QSize(16777215, 24))
        self.trackName_size.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_size.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.trackName_size)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(16, 0, 0, 0)
        self.trackNameSize = ClickableLabel(self.trackName_size)
        self.trackNameSize.setObjectName(u"trackNameSize")

        self.horizontalLayout_14.addWidget(self.trackNameSize)

        self.frame_29 = QFrame(self.trackName_size)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 24))
        self.frame_29.setMaximumSize(QSize(0, 24))
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_14.addWidget(self.frame_29)


        self.verticalLayout_2.addWidget(self.trackName_size)

        self.trackName_sizePx = QFrame(self.baseWidgets)
        self.trackName_sizePx.setObjectName(u"trackName_sizePx")
        self.trackName_sizePx.setMinimumSize(QSize(0, 24))
        self.trackName_sizePx.setMaximumSize(QSize(16777215, 24))
        self.trackName_sizePx.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_sizePx.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.trackName_sizePx)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(16, 0, 0, -1)
        self.frame_31 = QFrame(self.trackName_sizePx)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 24))
        self.frame_31.setMaximumSize(QSize(0, 24))
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_15.addWidget(self.frame_31)

        self.trackNameSizePx = ClickableLineEdit(self.trackName_sizePx)
        self.trackNameSizePx.setObjectName(u"trackNameSizePx")
        self.trackNameSizePx.setMinimumSize(QSize(80, 24))
        self.trackNameSizePx.setMaximumSize(QSize(80, 24))
        self.trackNameSizePx.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_15.addWidget(self.trackNameSizePx)

        self.frame_32 = QFrame(self.trackName_sizePx)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_15.addWidget(self.frame_32)


        self.verticalLayout_2.addWidget(self.trackName_sizePx)

        self.trackName_position = QFrame(self.baseWidgets)
        self.trackName_position.setObjectName(u"trackName_position")
        self.trackName_position.setMinimumSize(QSize(0, 24))
        self.trackName_position.setMaximumSize(QSize(16777215, 24))
        self.trackName_position.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_position.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.trackName_position)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(16, 0, 0, 0)
        self.trackNamePosition = ClickableLabel(self.trackName_position)
        self.trackNamePosition.setObjectName(u"trackNamePosition")

        self.horizontalLayout_16.addWidget(self.trackNamePosition)

        self.frame_34 = QFrame(self.trackName_position)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 24))
        self.frame_34.setMaximumSize(QSize(0, 24))
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_16.addWidget(self.frame_34)


        self.verticalLayout_2.addWidget(self.trackName_position)

        self.trackName_positionXY = QFrame(self.baseWidgets)
        self.trackName_positionXY.setObjectName(u"trackName_positionXY")
        self.trackName_positionXY.setMinimumSize(QSize(0, 24))
        self.trackName_positionXY.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_17 = QHBoxLayout(self.trackName_positionXY)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(16, 0, 0, 0)
        self.trackNamePositionX = ClickableLineEdit(self.trackName_positionXY)
        self.trackNamePositionX.setObjectName(u"trackNamePositionX")
        self.trackNamePositionX.setMinimumSize(QSize(70, 24))
        self.trackNamePositionX.setMaximumSize(QSize(70, 24))
        self.trackNamePositionX.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_17.addWidget(self.trackNamePositionX)

        self.trackNamePositionY = ClickableLineEdit(self.trackName_positionXY)
        self.trackNamePositionY.setObjectName(u"trackNamePositionY")
        self.trackNamePositionY.setMinimumSize(QSize(70, 24))
        self.trackNamePositionY.setMaximumSize(QSize(70, 24))
        self.trackNamePositionY.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_17.addWidget(self.trackNamePositionY)

        self.frame_36 = QFrame(self.trackName_positionXY)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_17.addWidget(self.frame_36)


        self.verticalLayout_2.addWidget(self.trackName_positionXY)

        self.trackName_color = QFrame(self.baseWidgets)
        self.trackName_color.setObjectName(u"trackName_color")
        self.trackName_color.setMinimumSize(QSize(0, 30))
        self.trackName_color.setMaximumSize(QSize(16777215, 30))
        self.trackName_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_color.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.trackName_color)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(16, 0, 0, 0)
        self.frame_38 = QFrame(self.trackName_color)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 30))
        self.frame_38.setMaximumSize(QSize(0, 30))
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_18.addWidget(self.frame_38)

        self.trackNameColor = ClickableLabel(self.trackName_color)
        self.trackNameColor.setObjectName(u"trackNameColor")
        self.trackNameColor.setMinimumSize(QSize(0, 30))
        self.trackNameColor.setMaximumSize(QSize(16777215, 30))
        self.trackNameColor.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_18.addWidget(self.trackNameColor)


        self.verticalLayout_2.addWidget(self.trackName_color)

        self.trackName_color1 = QFrame(self.baseWidgets)
        self.trackName_color1.setObjectName(u"trackName_color1")
        self.trackName_color1.setMinimumSize(QSize(0, 24))
        self.trackName_color1.setMaximumSize(QSize(16777215, 24))
        self.trackName_color1.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_color1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.trackName_color1)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(32, 0, 0, 0)
        self.frame_40 = QFrame(self.trackName_color1)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(0, 24))
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_40.setLineWidth(0)

        self.horizontalLayout_20.addWidget(self.frame_40)

        self.trackNameColor1 = ClickableLabel(self.trackName_color1)
        self.trackNameColor1.setObjectName(u"trackNameColor1")
        self.trackNameColor1.setMinimumSize(QSize(0, 24))
        self.trackNameColor1.setMaximumSize(QSize(16777215, 24))
        self.trackNameColor1.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_20.addWidget(self.trackNameColor1)


        self.verticalLayout_2.addWidget(self.trackName_color1)

        self.trackName_color1RGBA = QFrame(self.baseWidgets)
        self.trackName_color1RGBA.setObjectName(u"trackName_color1RGBA")
        self.trackName_color1RGBA.setMinimumSize(QSize(0, 24))
        self.trackName_color1RGBA.setMaximumSize(QSize(16777215, 24))
        self.trackName_color1RGBA.setStyleSheet(u"")
        self.horizontalLayout_21 = QHBoxLayout(self.trackName_color1RGBA)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(32, 0, 0, 0)
        self.trackNameColor1R = ClickableLineEdit(self.trackName_color1RGBA)
        self.trackNameColor1R.setObjectName(u"trackNameColor1R")
        sizePolicy1.setHeightForWidth(self.trackNameColor1R.sizePolicy().hasHeightForWidth())
        self.trackNameColor1R.setSizePolicy(sizePolicy1)
        self.trackNameColor1R.setMinimumSize(QSize(50, 24))
        self.trackNameColor1R.setMaximumSize(QSize(50, 24))
        self.trackNameColor1R.setSizeIncrement(QSize(0, 0))
        self.trackNameColor1R.setBaseSize(QSize(0, 18))
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
        self.trackNameColor1R.setPalette(palette1)
        self.trackNameColor1R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.trackNameColor1R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_21.addWidget(self.trackNameColor1R)

        self.trackNameColor1G = ClickableLineEdit(self.trackName_color1RGBA)
        self.trackNameColor1G.setObjectName(u"trackNameColor1G")
        sizePolicy1.setHeightForWidth(self.trackNameColor1G.sizePolicy().hasHeightForWidth())
        self.trackNameColor1G.setSizePolicy(sizePolicy1)
        self.trackNameColor1G.setMinimumSize(QSize(50, 24))
        self.trackNameColor1G.setMaximumSize(QSize(50, 24))
        self.trackNameColor1G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_21.addWidget(self.trackNameColor1G)

        self.trackNameColor1B = ClickableLineEdit(self.trackName_color1RGBA)
        self.trackNameColor1B.setObjectName(u"trackNameColor1B")
        sizePolicy1.setHeightForWidth(self.trackNameColor1B.sizePolicy().hasHeightForWidth())
        self.trackNameColor1B.setSizePolicy(sizePolicy1)
        self.trackNameColor1B.setMinimumSize(QSize(50, 24))
        self.trackNameColor1B.setMaximumSize(QSize(50, 24))
        self.trackNameColor1B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_21.addWidget(self.trackNameColor1B)

        self.trackNameColor1A = ClickableLineEdit(self.trackName_color1RGBA)
        self.trackNameColor1A.setObjectName(u"trackNameColor1A")
        sizePolicy1.setHeightForWidth(self.trackNameColor1A.sizePolicy().hasHeightForWidth())
        self.trackNameColor1A.setSizePolicy(sizePolicy1)
        self.trackNameColor1A.setMinimumSize(QSize(50, 24))
        self.trackNameColor1A.setMaximumSize(QSize(50, 24))
        self.trackNameColor1A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_21.addWidget(self.trackNameColor1A)

        self.frame_42 = QFrame(self.trackName_color1RGBA)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy2.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy2)
        self.frame_42.setMinimumSize(QSize(0, 24))
        self.frame_42.setMaximumSize(QSize(16777215, 24))
        self.frame_42.setFont(font)
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_21.addWidget(self.frame_42)


        self.verticalLayout_2.addWidget(self.trackName_color1RGBA)

        self.fixedColor_trackName = QFrame(self.baseWidgets)
        self.fixedColor_trackName.setObjectName(u"fixedColor_trackName")
        self.fixedColor_trackName.setMinimumSize(QSize(0, 20))
        self.fixedColor_trackName.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_22 = QHBoxLayout(self.fixedColor_trackName)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(32, 0, 0, 0)
        self.fixedColorTrackName = ClickableLabel(self.fixedColor_trackName)
        self.fixedColorTrackName.setObjectName(u"fixedColorTrackName")
        self.fixedColorTrackName.setMinimumSize(QSize(195, 0))
        self.fixedColorTrackName.setMaximumSize(QSize(195, 24))
        self.fixedColorTrackName.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.fixedColorTrackName)

        self.fixedColorTrackNameCheckBox = QCheckBox(self.fixedColor_trackName)
        self.fixedColorTrackNameCheckBox.setObjectName(u"fixedColorTrackNameCheckBox")
        self.fixedColorTrackNameCheckBox.setMaximumSize(QSize(16777215, 24))
        self.fixedColorTrackNameCheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.fixedColorTrackNameCheckBox.setIconSize(QSize(18, 18))
        self.fixedColorTrackNameCheckBox.setChecked(False)
        self.fixedColorTrackNameCheckBox.setTristate(False)

        self.horizontalLayout_22.addWidget(self.fixedColorTrackNameCheckBox)


        self.verticalLayout_2.addWidget(self.fixedColor_trackName)

        self.trackName_threshold = QFrame(self.baseWidgets)
        self.trackName_threshold.setObjectName(u"trackName_threshold")
        self.trackName_threshold.setMinimumSize(QSize(0, 24))
        self.trackName_threshold.setMaximumSize(QSize(16777215, 24))
        self.trackName_threshold.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_threshold.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.trackName_threshold)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(32, 0, 0, 0)
        self.frame_45 = QFrame(self.trackName_threshold)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(0, 24))
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_45.setLineWidth(0)

        self.horizontalLayout_23.addWidget(self.frame_45)

        self.trackNameThreshold = ClickableLabel(self.trackName_threshold)
        self.trackNameThreshold.setObjectName(u"trackNameThreshold")
        self.trackNameThreshold.setMinimumSize(QSize(0, 24))
        self.trackNameThreshold.setMaximumSize(QSize(16777215, 24))
        self.trackNameThreshold.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_23.addWidget(self.trackNameThreshold)


        self.verticalLayout_2.addWidget(self.trackName_threshold)

        self.trackName_thresholdRGB = QFrame(self.baseWidgets)
        self.trackName_thresholdRGB.setObjectName(u"trackName_thresholdRGB")
        self.trackName_thresholdRGB.setMinimumSize(QSize(0, 24))
        self.trackName_thresholdRGB.setMaximumSize(QSize(16777215, 24))
        self.trackName_thresholdRGB.setStyleSheet(u"")
        self.horizontalLayout_24 = QHBoxLayout(self.trackName_thresholdRGB)
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(32, 0, 0, 0)
        self.trackNameThresholdR = ClickableLineEdit(self.trackName_thresholdRGB)
        self.trackNameThresholdR.setObjectName(u"trackNameThresholdR")
        sizePolicy1.setHeightForWidth(self.trackNameThresholdR.sizePolicy().hasHeightForWidth())
        self.trackNameThresholdR.setSizePolicy(sizePolicy1)
        self.trackNameThresholdR.setMinimumSize(QSize(50, 24))
        self.trackNameThresholdR.setMaximumSize(QSize(50, 24))
        self.trackNameThresholdR.setSizeIncrement(QSize(0, 0))
        self.trackNameThresholdR.setBaseSize(QSize(0, 18))
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
        self.trackNameThresholdR.setPalette(palette2)
        self.trackNameThresholdR.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.trackNameThresholdR.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_24.addWidget(self.trackNameThresholdR)

        self.trackNameThresholdG = ClickableLineEdit(self.trackName_thresholdRGB)
        self.trackNameThresholdG.setObjectName(u"trackNameThresholdG")
        sizePolicy1.setHeightForWidth(self.trackNameThresholdG.sizePolicy().hasHeightForWidth())
        self.trackNameThresholdG.setSizePolicy(sizePolicy1)
        self.trackNameThresholdG.setMinimumSize(QSize(50, 24))
        self.trackNameThresholdG.setMaximumSize(QSize(50, 24))
        self.trackNameThresholdG.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_24.addWidget(self.trackNameThresholdG)

        self.trackNameThresholdB = ClickableLineEdit(self.trackName_thresholdRGB)
        self.trackNameThresholdB.setObjectName(u"trackNameThresholdB")
        sizePolicy1.setHeightForWidth(self.trackNameThresholdB.sizePolicy().hasHeightForWidth())
        self.trackNameThresholdB.setSizePolicy(sizePolicy1)
        self.trackNameThresholdB.setMinimumSize(QSize(50, 24))
        self.trackNameThresholdB.setMaximumSize(QSize(50, 24))
        self.trackNameThresholdB.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_24.addWidget(self.trackNameThresholdB)

        self.frame_47 = QFrame(self.trackName_thresholdRGB)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy2.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy2)
        self.frame_47.setMinimumSize(QSize(0, 24))
        self.frame_47.setMaximumSize(QSize(16777215, 24))
        self.frame_47.setFont(font)
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_24.addWidget(self.frame_47)


        self.verticalLayout_2.addWidget(self.trackName_thresholdRGB)

        self.trackName_thresholdMode = QFrame(self.baseWidgets)
        self.trackName_thresholdMode.setObjectName(u"trackName_thresholdMode")
        self.trackName_thresholdMode.setMinimumSize(QSize(0, 24))
        self.trackName_thresholdMode.setMaximumSize(QSize(16777215, 24))
        self.trackName_thresholdMode.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_thresholdMode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.trackName_thresholdMode)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(32, 0, 0, 0)
        self.frame_49 = QFrame(self.trackName_thresholdMode)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(0, 24))
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_49.setLineWidth(0)

        self.horizontalLayout_25.addWidget(self.frame_49)

        self.trackNameThresholdMode = ClickableLabel(self.trackName_thresholdMode)
        self.trackNameThresholdMode.setObjectName(u"trackNameThresholdMode")
        self.trackNameThresholdMode.setMinimumSize(QSize(0, 24))
        self.trackNameThresholdMode.setMaximumSize(QSize(16777215, 24))
        self.trackNameThresholdMode.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_25.addWidget(self.trackNameThresholdMode)


        self.verticalLayout_2.addWidget(self.trackName_thresholdMode)

        self.trackName_thresholdModeComboBox = QFrame(self.baseWidgets)
        self.trackName_thresholdModeComboBox.setObjectName(u"trackName_thresholdModeComboBox")
        self.trackName_thresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.trackName_thresholdModeComboBox.setMaximumSize(QSize(16777215, 24))
        self.trackName_thresholdModeComboBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_thresholdModeComboBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.trackName_thresholdModeComboBox)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(32, 0, 0, 0)
        self.frame_53 = QFrame(self.trackName_thresholdModeComboBox)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(0, 24))
        self.frame_53.setMaximumSize(QSize(0, 24))
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_27.addWidget(self.frame_53)

        self.trackNameThresholdModeComboBox = QComboBox(self.trackName_thresholdModeComboBox)
        self.trackNameThresholdModeComboBox.addItem("")
        self.trackNameThresholdModeComboBox.addItem("")
        self.trackNameThresholdModeComboBox.addItem("")
        self.trackNameThresholdModeComboBox.addItem("")
        self.trackNameThresholdModeComboBox.addItem("")
        self.trackNameThresholdModeComboBox.setObjectName(u"trackNameThresholdModeComboBox")
        self.trackNameThresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.trackNameThresholdModeComboBox.setMaximumSize(QSize(80, 24))
        self.trackNameThresholdModeComboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_27.addWidget(self.trackNameThresholdModeComboBox)

        self.frame_54 = QFrame(self.trackName_thresholdModeComboBox)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 24))
        self.frame_54.setMaximumSize(QSize(16777215, 24))
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_27.addWidget(self.frame_54)


        self.verticalLayout_2.addWidget(self.trackName_thresholdModeComboBox)

        self.trackName_color2 = QFrame(self.baseWidgets)
        self.trackName_color2.setObjectName(u"trackName_color2")
        self.trackName_color2.setMinimumSize(QSize(0, 24))
        self.trackName_color2.setMaximumSize(QSize(16777215, 24))
        self.trackName_color2.setFrameShape(QFrame.Shape.StyledPanel)
        self.trackName_color2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.trackName_color2)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(32, 0, 0, 0)
        self.frame_56 = QFrame(self.trackName_color2)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMaximumSize(QSize(0, 24))
        self.frame_56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_56.setLineWidth(0)

        self.horizontalLayout_28.addWidget(self.frame_56)

        self.trackNameColor2 = ClickableLabel(self.trackName_color2)
        self.trackNameColor2.setObjectName(u"trackNameColor2")
        self.trackNameColor2.setMinimumSize(QSize(0, 24))
        self.trackNameColor2.setMaximumSize(QSize(16777215, 24))
        self.trackNameColor2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_28.addWidget(self.trackNameColor2)


        self.verticalLayout_2.addWidget(self.trackName_color2)

        self.trackName_color2RGBA = QFrame(self.baseWidgets)
        self.trackName_color2RGBA.setObjectName(u"trackName_color2RGBA")
        self.trackName_color2RGBA.setMinimumSize(QSize(0, 24))
        self.trackName_color2RGBA.setMaximumSize(QSize(16777215, 24))
        self.trackName_color2RGBA.setStyleSheet(u"")
        self.horizontalLayout_29 = QHBoxLayout(self.trackName_color2RGBA)
        self.horizontalLayout_29.setSpacing(6)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(32, 0, 0, 0)
        self.trackNameColor2R = ClickableLineEdit(self.trackName_color2RGBA)
        self.trackNameColor2R.setObjectName(u"trackNameColor2R")
        sizePolicy1.setHeightForWidth(self.trackNameColor2R.sizePolicy().hasHeightForWidth())
        self.trackNameColor2R.setSizePolicy(sizePolicy1)
        self.trackNameColor2R.setMinimumSize(QSize(50, 24))
        self.trackNameColor2R.setMaximumSize(QSize(50, 24))
        self.trackNameColor2R.setSizeIncrement(QSize(0, 0))
        self.trackNameColor2R.setBaseSize(QSize(0, 18))
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
        self.trackNameColor2R.setPalette(palette3)
        self.trackNameColor2R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.trackNameColor2R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_29.addWidget(self.trackNameColor2R)

        self.trackNameColor2G = ClickableLineEdit(self.trackName_color2RGBA)
        self.trackNameColor2G.setObjectName(u"trackNameColor2G")
        sizePolicy1.setHeightForWidth(self.trackNameColor2G.sizePolicy().hasHeightForWidth())
        self.trackNameColor2G.setSizePolicy(sizePolicy1)
        self.trackNameColor2G.setMinimumSize(QSize(50, 24))
        self.trackNameColor2G.setMaximumSize(QSize(50, 24))
        self.trackNameColor2G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_29.addWidget(self.trackNameColor2G)

        self.trackNameColor2B = ClickableLineEdit(self.trackName_color2RGBA)
        self.trackNameColor2B.setObjectName(u"trackNameColor2B")
        sizePolicy1.setHeightForWidth(self.trackNameColor2B.sizePolicy().hasHeightForWidth())
        self.trackNameColor2B.setSizePolicy(sizePolicy1)
        self.trackNameColor2B.setMinimumSize(QSize(50, 24))
        self.trackNameColor2B.setMaximumSize(QSize(50, 24))
        self.trackNameColor2B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_29.addWidget(self.trackNameColor2B)

        self.trackNameColor2A = ClickableLineEdit(self.trackName_color2RGBA)
        self.trackNameColor2A.setObjectName(u"trackNameColor2A")
        sizePolicy1.setHeightForWidth(self.trackNameColor2A.sizePolicy().hasHeightForWidth())
        self.trackNameColor2A.setSizePolicy(sizePolicy1)
        self.trackNameColor2A.setMinimumSize(QSize(50, 24))
        self.trackNameColor2A.setMaximumSize(QSize(50, 24))
        self.trackNameColor2A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_29.addWidget(self.trackNameColor2A)

        self.frame_58 = QFrame(self.trackName_color2RGBA)
        self.frame_58.setObjectName(u"frame_58")
        sizePolicy2.setHeightForWidth(self.frame_58.sizePolicy().hasHeightForWidth())
        self.frame_58.setSizePolicy(sizePolicy2)
        self.frame_58.setMinimumSize(QSize(0, 24))
        self.frame_58.setMaximumSize(QSize(16777215, 24))
        self.frame_58.setFont(font)
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_29.addWidget(self.frame_58)


        self.verticalLayout_2.addWidget(self.trackName_color2RGBA)

        self.artists = ClickableLabel(self.baseWidgets)
        self.artists.setObjectName(u"artists")
        self.artists.setMinimumSize(QSize(0, 40))
        self.artists.setMaximumSize(QSize(16777215, 40))
        self.artists.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.artists)

        self.artists_mode = QFrame(self.baseWidgets)
        self.artists_mode.setObjectName(u"artists_mode")
        self.artists_mode.setMinimumSize(QSize(0, 24))
        self.artists_mode.setMaximumSize(QSize(16777215, 24))
        self.artists_mode.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_mode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_182 = QHBoxLayout(self.artists_mode)
        self.horizontalLayout_182.setSpacing(0)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(16, 0, 0, 0)
        self.artistsMode = ClickableLabel(self.artists_mode)
        self.artistsMode.setObjectName(u"artistsMode")

        self.horizontalLayout_182.addWidget(self.artistsMode)

        self.frame_285 = QFrame(self.artists_mode)
        self.frame_285.setObjectName(u"frame_285")
        self.frame_285.setMinimumSize(QSize(0, 24))
        self.frame_285.setMaximumSize(QSize(0, 24))
        self.frame_285.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_285.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_182.addWidget(self.frame_285)


        self.verticalLayout_2.addWidget(self.artists_mode)

        self.artists_modeComboBox = QFrame(self.baseWidgets)
        self.artists_modeComboBox.setObjectName(u"artists_modeComboBox")
        self.artists_modeComboBox.setMinimumSize(QSize(0, 24))
        self.artists_modeComboBox.setMaximumSize(QSize(16777215, 24))
        self.artists_modeComboBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_modeComboBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_183 = QHBoxLayout(self.artists_modeComboBox)
        self.horizontalLayout_183.setSpacing(0)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.horizontalLayout_183.setContentsMargins(16, 0, 0, 0)
        self.frame_287 = QFrame(self.artists_modeComboBox)
        self.frame_287.setObjectName(u"frame_287")
        self.frame_287.setMinimumSize(QSize(0, 24))
        self.frame_287.setMaximumSize(QSize(0, 24))
        self.frame_287.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_287.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_183.addWidget(self.frame_287)

        self.artistsModeComboBox = QComboBox(self.artists_modeComboBox)
        self.artistsModeComboBox.addItem("")
        self.artistsModeComboBox.addItem("")
        self.artistsModeComboBox.addItem("")
        self.artistsModeComboBox.addItem("")
        self.artistsModeComboBox.setObjectName(u"artistsModeComboBox")
        self.artistsModeComboBox.setMinimumSize(QSize(0, 24))
        self.artistsModeComboBox.setMaximumSize(QSize(80, 24))
        self.artistsModeComboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_183.addWidget(self.artistsModeComboBox)

        self.frame_288 = QFrame(self.artists_modeComboBox)
        self.frame_288.setObjectName(u"frame_288")
        self.frame_288.setMinimumSize(QSize(0, 24))
        self.frame_288.setMaximumSize(QSize(16777215, 24))
        self.frame_288.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_288.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_183.addWidget(self.frame_288)


        self.verticalLayout_2.addWidget(self.artists_modeComboBox)

        self.artists_size = QFrame(self.baseWidgets)
        self.artists_size.setObjectName(u"artists_size")
        self.artists_size.setMinimumSize(QSize(0, 24))
        self.artists_size.setMaximumSize(QSize(16777215, 24))
        self.artists_size.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_size.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_172 = QHBoxLayout(self.artists_size)
        self.horizontalLayout_172.setSpacing(0)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.horizontalLayout_172.setContentsMargins(16, 0, 0, 0)
        self.artistsSize = ClickableLabel(self.artists_size)
        self.artistsSize.setObjectName(u"artistsSize")

        self.horizontalLayout_172.addWidget(self.artistsSize)

        self.frame_119 = QFrame(self.artists_size)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMinimumSize(QSize(0, 24))
        self.frame_119.setMaximumSize(QSize(0, 24))
        self.frame_119.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_172.addWidget(self.frame_119)


        self.verticalLayout_2.addWidget(self.artists_size)

        self.artists_sizePx = QFrame(self.baseWidgets)
        self.artists_sizePx.setObjectName(u"artists_sizePx")
        self.artists_sizePx.setMinimumSize(QSize(0, 24))
        self.artists_sizePx.setMaximumSize(QSize(16777215, 24))
        self.artists_sizePx.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_sizePx.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_174 = QHBoxLayout(self.artists_sizePx)
        self.horizontalLayout_174.setSpacing(0)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_174.setContentsMargins(16, 0, 0, -1)
        self.frame_250 = QFrame(self.artists_sizePx)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setMinimumSize(QSize(0, 24))
        self.frame_250.setMaximumSize(QSize(0, 24))
        self.frame_250.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_174.addWidget(self.frame_250)

        self.artistsSizePx = ClickableLineEdit(self.artists_sizePx)
        self.artistsSizePx.setObjectName(u"artistsSizePx")
        self.artistsSizePx.setMinimumSize(QSize(80, 24))
        self.artistsSizePx.setMaximumSize(QSize(80, 24))
        self.artistsSizePx.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_174.addWidget(self.artistsSizePx)

        self.frame_255 = QFrame(self.artists_sizePx)
        self.frame_255.setObjectName(u"frame_255")
        self.frame_255.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_174.addWidget(self.frame_255)


        self.verticalLayout_2.addWidget(self.artists_sizePx)

        self.artists_position = QFrame(self.baseWidgets)
        self.artists_position.setObjectName(u"artists_position")
        self.artists_position.setMinimumSize(QSize(0, 24))
        self.artists_position.setMaximumSize(QSize(16777215, 24))
        self.artists_position.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_position.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_173 = QHBoxLayout(self.artists_position)
        self.horizontalLayout_173.setSpacing(0)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalLayout_173.setContentsMargins(16, 0, 0, 0)
        self.artistsPosition = ClickableLabel(self.artists_position)
        self.artistsPosition.setObjectName(u"artistsPosition")

        self.horizontalLayout_173.addWidget(self.artistsPosition)

        self.frame_242 = QFrame(self.artists_position)
        self.frame_242.setObjectName(u"frame_242")
        self.frame_242.setMinimumSize(QSize(0, 24))
        self.frame_242.setMaximumSize(QSize(0, 24))
        self.frame_242.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_173.addWidget(self.frame_242)


        self.verticalLayout_2.addWidget(self.artists_position)

        self.artists_positionPx = QFrame(self.baseWidgets)
        self.artists_positionPx.setObjectName(u"artists_positionPx")
        self.artists_positionPx.setMinimumSize(QSize(0, 24))
        self.artists_positionPx.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_175 = QHBoxLayout(self.artists_positionPx)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(16, 0, 0, 0)
        self.artistsPositionPx = ClickableLineEdit(self.artists_positionPx)
        self.artistsPositionPx.setObjectName(u"artistsPositionPx")
        self.artistsPositionPx.setMinimumSize(QSize(70, 24))
        self.artistsPositionPx.setMaximumSize(QSize(70, 24))
        self.artistsPositionPx.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_175.addWidget(self.artistsPositionPx)

        self.frame_262 = QFrame(self.artists_positionPx)
        self.frame_262.setObjectName(u"frame_262")
        self.frame_262.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_262.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_175.addWidget(self.frame_262)


        self.verticalLayout_2.addWidget(self.artists_positionPx)

        self.artists_color = QFrame(self.baseWidgets)
        self.artists_color.setObjectName(u"artists_color")
        self.artists_color.setMinimumSize(QSize(0, 30))
        self.artists_color.setMaximumSize(QSize(16777215, 30))
        self.artists_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_color.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_184 = QHBoxLayout(self.artists_color)
        self.horizontalLayout_184.setSpacing(0)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(16, 0, 0, 0)
        self.frame_290 = QFrame(self.artists_color)
        self.frame_290.setObjectName(u"frame_290")
        self.frame_290.setMinimumSize(QSize(0, 30))
        self.frame_290.setMaximumSize(QSize(0, 30))
        self.frame_290.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_290.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_184.addWidget(self.frame_290)

        self.artistsColor = ClickableLabel(self.artists_color)
        self.artistsColor.setObjectName(u"artistsColor")
        self.artistsColor.setMinimumSize(QSize(0, 30))
        self.artistsColor.setMaximumSize(QSize(16777215, 30))
        self.artistsColor.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_184.addWidget(self.artistsColor)


        self.verticalLayout_2.addWidget(self.artists_color)

        self.artists_color1 = QFrame(self.baseWidgets)
        self.artists_color1.setObjectName(u"artists_color1")
        self.artists_color1.setMinimumSize(QSize(0, 24))
        self.artists_color1.setMaximumSize(QSize(16777215, 24))
        self.artists_color1.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_color1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_181 = QHBoxLayout(self.artists_color1)
        self.horizontalLayout_181.setSpacing(0)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(32, 0, 0, 0)
        self.frame_283 = QFrame(self.artists_color1)
        self.frame_283.setObjectName(u"frame_283")
        self.frame_283.setMaximumSize(QSize(0, 24))
        self.frame_283.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_283.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_283.setLineWidth(0)

        self.horizontalLayout_181.addWidget(self.frame_283)

        self.artistsColor1 = ClickableLabel(self.artists_color1)
        self.artistsColor1.setObjectName(u"artistsColor1")
        self.artistsColor1.setMinimumSize(QSize(0, 24))
        self.artistsColor1.setMaximumSize(QSize(16777215, 24))
        self.artistsColor1.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_181.addWidget(self.artistsColor1)


        self.verticalLayout_2.addWidget(self.artists_color1)

        self.artists_color1RGBA = QFrame(self.baseWidgets)
        self.artists_color1RGBA.setObjectName(u"artists_color1RGBA")
        self.artists_color1RGBA.setMinimumSize(QSize(0, 24))
        self.artists_color1RGBA.setMaximumSize(QSize(16777215, 24))
        self.artists_color1RGBA.setStyleSheet(u"")
        self.horizontalLayout_180 = QHBoxLayout(self.artists_color1RGBA)
        self.horizontalLayout_180.setSpacing(6)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(32, 0, 0, 0)
        self.artistsColor1R = ClickableLineEdit(self.artists_color1RGBA)
        self.artistsColor1R.setObjectName(u"artistsColor1R")
        sizePolicy1.setHeightForWidth(self.artistsColor1R.sizePolicy().hasHeightForWidth())
        self.artistsColor1R.setSizePolicy(sizePolicy1)
        self.artistsColor1R.setMinimumSize(QSize(50, 24))
        self.artistsColor1R.setMaximumSize(QSize(50, 24))
        self.artistsColor1R.setSizeIncrement(QSize(0, 0))
        self.artistsColor1R.setBaseSize(QSize(0, 18))
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
        self.artistsColor1R.setPalette(palette4)
        self.artistsColor1R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.artistsColor1R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_180.addWidget(self.artistsColor1R)

        self.artistsColor1G = ClickableLineEdit(self.artists_color1RGBA)
        self.artistsColor1G.setObjectName(u"artistsColor1G")
        sizePolicy1.setHeightForWidth(self.artistsColor1G.sizePolicy().hasHeightForWidth())
        self.artistsColor1G.setSizePolicy(sizePolicy1)
        self.artistsColor1G.setMinimumSize(QSize(50, 24))
        self.artistsColor1G.setMaximumSize(QSize(50, 24))
        self.artistsColor1G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_180.addWidget(self.artistsColor1G)

        self.artistsColor1B = ClickableLineEdit(self.artists_color1RGBA)
        self.artistsColor1B.setObjectName(u"artistsColor1B")
        sizePolicy1.setHeightForWidth(self.artistsColor1B.sizePolicy().hasHeightForWidth())
        self.artistsColor1B.setSizePolicy(sizePolicy1)
        self.artistsColor1B.setMinimumSize(QSize(50, 24))
        self.artistsColor1B.setMaximumSize(QSize(50, 24))
        self.artistsColor1B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_180.addWidget(self.artistsColor1B)

        self.artistsColor1A = ClickableLineEdit(self.artists_color1RGBA)
        self.artistsColor1A.setObjectName(u"artistsColor1A")
        sizePolicy1.setHeightForWidth(self.artistsColor1A.sizePolicy().hasHeightForWidth())
        self.artistsColor1A.setSizePolicy(sizePolicy1)
        self.artistsColor1A.setMinimumSize(QSize(50, 24))
        self.artistsColor1A.setMaximumSize(QSize(50, 24))
        self.artistsColor1A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_180.addWidget(self.artistsColor1A)

        self.frame_281 = QFrame(self.artists_color1RGBA)
        self.frame_281.setObjectName(u"frame_281")
        sizePolicy2.setHeightForWidth(self.frame_281.sizePolicy().hasHeightForWidth())
        self.frame_281.setSizePolicy(sizePolicy2)
        self.frame_281.setMinimumSize(QSize(0, 24))
        self.frame_281.setMaximumSize(QSize(16777215, 24))
        self.frame_281.setFont(font)
        self.frame_281.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_281.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_180.addWidget(self.frame_281)


        self.verticalLayout_2.addWidget(self.artists_color1RGBA)

        self.fixedColor_artists = QFrame(self.baseWidgets)
        self.fixedColor_artists.setObjectName(u"fixedColor_artists")
        self.fixedColor_artists.setMinimumSize(QSize(0, 20))
        self.fixedColor_artists.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_185 = QHBoxLayout(self.fixedColor_artists)
        self.horizontalLayout_185.setSpacing(5)
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.horizontalLayout_185.setContentsMargins(32, 0, 0, 0)
        self.fixedColorArtists = ClickableLabel(self.fixedColor_artists)
        self.fixedColorArtists.setObjectName(u"fixedColorArtists")
        self.fixedColorArtists.setMinimumSize(QSize(195, 0))
        self.fixedColorArtists.setMaximumSize(QSize(195, 24))
        self.fixedColorArtists.setStyleSheet(u"")

        self.horizontalLayout_185.addWidget(self.fixedColorArtists)

        self.fixedColorArtistsCheckBox = QCheckBox(self.fixedColor_artists)
        self.fixedColorArtistsCheckBox.setObjectName(u"fixedColorArtistsCheckBox")
        self.fixedColorArtistsCheckBox.setMaximumSize(QSize(16777215, 24))
        self.fixedColorArtistsCheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.fixedColorArtistsCheckBox.setIconSize(QSize(18, 18))
        self.fixedColorArtistsCheckBox.setChecked(False)
        self.fixedColorArtistsCheckBox.setTristate(False)

        self.horizontalLayout_185.addWidget(self.fixedColorArtistsCheckBox)


        self.verticalLayout_2.addWidget(self.fixedColor_artists)

        self.artists_threshold = QFrame(self.baseWidgets)
        self.artists_threshold.setObjectName(u"artists_threshold")
        self.artists_threshold.setMinimumSize(QSize(0, 24))
        self.artists_threshold.setMaximumSize(QSize(16777215, 24))
        self.artists_threshold.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_threshold.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_176 = QHBoxLayout(self.artists_threshold)
        self.horizontalLayout_176.setSpacing(0)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(32, 0, 0, 0)
        self.frame_266 = QFrame(self.artists_threshold)
        self.frame_266.setObjectName(u"frame_266")
        self.frame_266.setMaximumSize(QSize(0, 24))
        self.frame_266.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_266.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_266.setLineWidth(0)

        self.horizontalLayout_176.addWidget(self.frame_266)

        self.artistsThreshold = ClickableLabel(self.artists_threshold)
        self.artistsThreshold.setObjectName(u"artistsThreshold")
        self.artistsThreshold.setMinimumSize(QSize(0, 24))
        self.artistsThreshold.setMaximumSize(QSize(16777215, 24))
        self.artistsThreshold.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_176.addWidget(self.artistsThreshold)


        self.verticalLayout_2.addWidget(self.artists_threshold)

        self.artists_thresholdRGB = QFrame(self.baseWidgets)
        self.artists_thresholdRGB.setObjectName(u"artists_thresholdRGB")
        self.artists_thresholdRGB.setMinimumSize(QSize(0, 24))
        self.artists_thresholdRGB.setMaximumSize(QSize(16777215, 24))
        self.artists_thresholdRGB.setStyleSheet(u"")
        self.horizontalLayout_179 = QHBoxLayout(self.artists_thresholdRGB)
        self.horizontalLayout_179.setSpacing(6)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(32, 0, 0, 0)
        self.artistsThresholdR = ClickableLineEdit(self.artists_thresholdRGB)
        self.artistsThresholdR.setObjectName(u"artistsThresholdR")
        sizePolicy1.setHeightForWidth(self.artistsThresholdR.sizePolicy().hasHeightForWidth())
        self.artistsThresholdR.setSizePolicy(sizePolicy1)
        self.artistsThresholdR.setMinimumSize(QSize(50, 24))
        self.artistsThresholdR.setMaximumSize(QSize(50, 24))
        self.artistsThresholdR.setSizeIncrement(QSize(0, 0))
        self.artistsThresholdR.setBaseSize(QSize(0, 18))
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
        self.artistsThresholdR.setPalette(palette5)
        self.artistsThresholdR.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.artistsThresholdR.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_179.addWidget(self.artistsThresholdR)

        self.artistsThresholdG = ClickableLineEdit(self.artists_thresholdRGB)
        self.artistsThresholdG.setObjectName(u"artistsThresholdG")
        sizePolicy1.setHeightForWidth(self.artistsThresholdG.sizePolicy().hasHeightForWidth())
        self.artistsThresholdG.setSizePolicy(sizePolicy1)
        self.artistsThresholdG.setMinimumSize(QSize(50, 24))
        self.artistsThresholdG.setMaximumSize(QSize(50, 24))
        self.artistsThresholdG.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_179.addWidget(self.artistsThresholdG)

        self.artistsThresholdB = ClickableLineEdit(self.artists_thresholdRGB)
        self.artistsThresholdB.setObjectName(u"artistsThresholdB")
        sizePolicy1.setHeightForWidth(self.artistsThresholdB.sizePolicy().hasHeightForWidth())
        self.artistsThresholdB.setSizePolicy(sizePolicy1)
        self.artistsThresholdB.setMinimumSize(QSize(50, 24))
        self.artistsThresholdB.setMaximumSize(QSize(50, 24))
        self.artistsThresholdB.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_179.addWidget(self.artistsThresholdB)

        self.frame_279 = QFrame(self.artists_thresholdRGB)
        self.frame_279.setObjectName(u"frame_279")
        sizePolicy2.setHeightForWidth(self.frame_279.sizePolicy().hasHeightForWidth())
        self.frame_279.setSizePolicy(sizePolicy2)
        self.frame_279.setMinimumSize(QSize(0, 24))
        self.frame_279.setMaximumSize(QSize(16777215, 24))
        self.frame_279.setFont(font)
        self.frame_279.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_279.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_179.addWidget(self.frame_279)


        self.verticalLayout_2.addWidget(self.artists_thresholdRGB)

        self.artists_thresholdMode = QFrame(self.baseWidgets)
        self.artists_thresholdMode.setObjectName(u"artists_thresholdMode")
        self.artists_thresholdMode.setMinimumSize(QSize(0, 24))
        self.artists_thresholdMode.setMaximumSize(QSize(16777215, 24))
        self.artists_thresholdMode.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_thresholdMode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_177 = QHBoxLayout(self.artists_thresholdMode)
        self.horizontalLayout_177.setSpacing(0)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(32, 0, 0, 0)
        self.frame_271 = QFrame(self.artists_thresholdMode)
        self.frame_271.setObjectName(u"frame_271")
        self.frame_271.setMaximumSize(QSize(0, 24))
        self.frame_271.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_271.setLineWidth(0)

        self.horizontalLayout_177.addWidget(self.frame_271)

        self.artistsThresholdMode = ClickableLabel(self.artists_thresholdMode)
        self.artistsThresholdMode.setObjectName(u"artistsThresholdMode")
        self.artistsThresholdMode.setMinimumSize(QSize(0, 24))
        self.artistsThresholdMode.setMaximumSize(QSize(16777215, 24))
        self.artistsThresholdMode.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_177.addWidget(self.artistsThresholdMode)


        self.verticalLayout_2.addWidget(self.artists_thresholdMode)

        self.artists_thresholdModeComboBox = QFrame(self.baseWidgets)
        self.artists_thresholdModeComboBox.setObjectName(u"artists_thresholdModeComboBox")
        self.artists_thresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.artists_thresholdModeComboBox.setMaximumSize(QSize(16777215, 24))
        self.artists_thresholdModeComboBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_thresholdModeComboBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_178 = QHBoxLayout(self.artists_thresholdModeComboBox)
        self.horizontalLayout_178.setSpacing(0)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalLayout_178.setContentsMargins(32, 0, 0, 0)
        self.frame_274 = QFrame(self.artists_thresholdModeComboBox)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setMinimumSize(QSize(0, 24))
        self.frame_274.setMaximumSize(QSize(0, 24))
        self.frame_274.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_178.addWidget(self.frame_274)

        self.artistsThresholdModeComboBox = QComboBox(self.artists_thresholdModeComboBox)
        self.artistsThresholdModeComboBox.addItem("")
        self.artistsThresholdModeComboBox.addItem("")
        self.artistsThresholdModeComboBox.addItem("")
        self.artistsThresholdModeComboBox.addItem("")
        self.artistsThresholdModeComboBox.addItem("")
        self.artistsThresholdModeComboBox.setObjectName(u"artistsThresholdModeComboBox")
        self.artistsThresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.artistsThresholdModeComboBox.setMaximumSize(QSize(80, 24))
        self.artistsThresholdModeComboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_178.addWidget(self.artistsThresholdModeComboBox)

        self.frame_276 = QFrame(self.artists_thresholdModeComboBox)
        self.frame_276.setObjectName(u"frame_276")
        self.frame_276.setMinimumSize(QSize(0, 24))
        self.frame_276.setMaximumSize(QSize(16777215, 24))
        self.frame_276.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_276.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_178.addWidget(self.frame_276)


        self.verticalLayout_2.addWidget(self.artists_thresholdModeComboBox)

        self.artists_color2 = QFrame(self.baseWidgets)
        self.artists_color2.setObjectName(u"artists_color2")
        self.artists_color2.setMinimumSize(QSize(0, 24))
        self.artists_color2.setMaximumSize(QSize(16777215, 24))
        self.artists_color2.setFrameShape(QFrame.Shape.StyledPanel)
        self.artists_color2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_186 = QHBoxLayout(self.artists_color2)
        self.horizontalLayout_186.setSpacing(0)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(32, 0, 0, 0)
        self.frame_293 = QFrame(self.artists_color2)
        self.frame_293.setObjectName(u"frame_293")
        self.frame_293.setMaximumSize(QSize(0, 24))
        self.frame_293.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_293.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_293.setLineWidth(0)

        self.horizontalLayout_186.addWidget(self.frame_293)

        self.artistsColor2 = ClickableLabel(self.artists_color2)
        self.artistsColor2.setObjectName(u"artistsColor2")
        self.artistsColor2.setMinimumSize(QSize(0, 24))
        self.artistsColor2.setMaximumSize(QSize(16777215, 24))
        self.artistsColor2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_186.addWidget(self.artistsColor2)


        self.verticalLayout_2.addWidget(self.artists_color2)

        self.artists_color2RGBA = QFrame(self.baseWidgets)
        self.artists_color2RGBA.setObjectName(u"artists_color2RGBA")
        self.artists_color2RGBA.setMinimumSize(QSize(0, 24))
        self.artists_color2RGBA.setMaximumSize(QSize(16777215, 24))
        self.artists_color2RGBA.setStyleSheet(u"")
        self.horizontalLayout_187 = QHBoxLayout(self.artists_color2RGBA)
        self.horizontalLayout_187.setSpacing(6)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_187.setContentsMargins(32, 0, 0, 0)
        self.artistsColor2R = ClickableLineEdit(self.artists_color2RGBA)
        self.artistsColor2R.setObjectName(u"artistsColor2R")
        sizePolicy1.setHeightForWidth(self.artistsColor2R.sizePolicy().hasHeightForWidth())
        self.artistsColor2R.setSizePolicy(sizePolicy1)
        self.artistsColor2R.setMinimumSize(QSize(50, 24))
        self.artistsColor2R.setMaximumSize(QSize(50, 24))
        self.artistsColor2R.setSizeIncrement(QSize(0, 0))
        self.artistsColor2R.setBaseSize(QSize(0, 18))
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
        self.artistsColor2R.setPalette(palette6)
        self.artistsColor2R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.artistsColor2R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_187.addWidget(self.artistsColor2R)

        self.artistsColor2G = ClickableLineEdit(self.artists_color2RGBA)
        self.artistsColor2G.setObjectName(u"artistsColor2G")
        sizePolicy1.setHeightForWidth(self.artistsColor2G.sizePolicy().hasHeightForWidth())
        self.artistsColor2G.setSizePolicy(sizePolicy1)
        self.artistsColor2G.setMinimumSize(QSize(50, 24))
        self.artistsColor2G.setMaximumSize(QSize(50, 24))
        self.artistsColor2G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_187.addWidget(self.artistsColor2G)

        self.artistsColor2B = ClickableLineEdit(self.artists_color2RGBA)
        self.artistsColor2B.setObjectName(u"artistsColor2B")
        sizePolicy1.setHeightForWidth(self.artistsColor2B.sizePolicy().hasHeightForWidth())
        self.artistsColor2B.setSizePolicy(sizePolicy1)
        self.artistsColor2B.setMinimumSize(QSize(50, 24))
        self.artistsColor2B.setMaximumSize(QSize(50, 24))
        self.artistsColor2B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_187.addWidget(self.artistsColor2B)

        self.artistsColor2A = ClickableLineEdit(self.artists_color2RGBA)
        self.artistsColor2A.setObjectName(u"artistsColor2A")
        sizePolicy1.setHeightForWidth(self.artistsColor2A.sizePolicy().hasHeightForWidth())
        self.artistsColor2A.setSizePolicy(sizePolicy1)
        self.artistsColor2A.setMinimumSize(QSize(50, 24))
        self.artistsColor2A.setMaximumSize(QSize(50, 24))
        self.artistsColor2A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_187.addWidget(self.artistsColor2A)

        self.frame_295 = QFrame(self.artists_color2RGBA)
        self.frame_295.setObjectName(u"frame_295")
        sizePolicy2.setHeightForWidth(self.frame_295.sizePolicy().hasHeightForWidth())
        self.frame_295.setSizePolicy(sizePolicy2)
        self.frame_295.setMinimumSize(QSize(0, 24))
        self.frame_295.setMaximumSize(QSize(16777215, 24))
        self.frame_295.setFont(font)
        self.frame_295.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_295.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_187.addWidget(self.frame_295)


        self.verticalLayout_2.addWidget(self.artists_color2RGBA)

        self.progressbar = ClickableLabel(self.baseWidgets)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setMinimumSize(QSize(0, 40))
        self.progressbar.setMaximumSize(QSize(16777215, 40))
        self.progressbar.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.progressbar)

        self.progressbar_size = QFrame(self.baseWidgets)
        self.progressbar_size.setObjectName(u"progressbar_size")
        self.progressbar_size.setMinimumSize(QSize(0, 24))
        self.progressbar_size.setMaximumSize(QSize(16777215, 24))
        self.progressbar_size.setFrameShape(QFrame.Shape.StyledPanel)
        self.progressbar_size.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_189 = QHBoxLayout(self.progressbar_size)
        self.horizontalLayout_189.setSpacing(0)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_189.setContentsMargins(16, 0, 0, 0)
        self.frame_299 = QFrame(self.progressbar_size)
        self.frame_299.setObjectName(u"frame_299")
        self.frame_299.setMaximumSize(QSize(0, 24))
        self.frame_299.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_299.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_299.setLineWidth(0)

        self.horizontalLayout_189.addWidget(self.frame_299)

        self.progressbarSize = ClickableLabel(self.progressbar_size)
        self.progressbarSize.setObjectName(u"progressbarSize")
        self.progressbarSize.setMinimumSize(QSize(0, 24))
        self.progressbarSize.setMaximumSize(QSize(16777215, 24))
        self.progressbarSize.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_189.addWidget(self.progressbarSize)


        self.verticalLayout_2.addWidget(self.progressbar_size)

        self.progressbar_sizeXY = QFrame(self.baseWidgets)
        self.progressbar_sizeXY.setObjectName(u"progressbar_sizeXY")
        self.progressbar_sizeXY.setMinimumSize(QSize(0, 24))
        self.progressbar_sizeXY.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_188 = QHBoxLayout(self.progressbar_sizeXY)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_188.setContentsMargins(16, 0, 0, 0)
        self.progressbarSizeX = ClickableLineEdit(self.progressbar_sizeXY)
        self.progressbarSizeX.setObjectName(u"progressbarSizeX")
        self.progressbarSizeX.setMinimumSize(QSize(70, 24))
        self.progressbarSizeX.setMaximumSize(QSize(70, 24))
        self.progressbarSizeX.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_188.addWidget(self.progressbarSizeX)

        self.progressbarSizeY = ClickableLineEdit(self.progressbar_sizeXY)
        self.progressbarSizeY.setObjectName(u"progressbarSizeY")
        self.progressbarSizeY.setMinimumSize(QSize(70, 24))
        self.progressbarSizeY.setMaximumSize(QSize(70, 24))
        self.progressbarSizeY.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_188.addWidget(self.progressbarSizeY)

        self.frame_297 = QFrame(self.progressbar_sizeXY)
        self.frame_297.setObjectName(u"frame_297")
        self.frame_297.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_297.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_188.addWidget(self.frame_297)


        self.verticalLayout_2.addWidget(self.progressbar_sizeXY)

        self.progresbar_radius = QFrame(self.baseWidgets)
        self.progresbar_radius.setObjectName(u"progresbar_radius")
        self.progresbar_radius.setMinimumSize(QSize(0, 24))
        self.progresbar_radius.setMaximumSize(QSize(16777215, 24))
        self.progresbar_radius.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbar_radius.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_190 = QHBoxLayout(self.progresbar_radius)
        self.horizontalLayout_190.setSpacing(0)
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(16, 0, 0, 0)
        self.frame_301 = QFrame(self.progresbar_radius)
        self.frame_301.setObjectName(u"frame_301")
        self.frame_301.setMaximumSize(QSize(0, 24))
        self.frame_301.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_301.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_301.setLineWidth(0)

        self.horizontalLayout_190.addWidget(self.frame_301)

        self.progresbarRadius = ClickableLabel(self.progresbar_radius)
        self.progresbarRadius.setObjectName(u"progresbarRadius")
        self.progresbarRadius.setMinimumSize(QSize(0, 24))
        self.progresbarRadius.setMaximumSize(QSize(16777215, 24))
        self.progresbarRadius.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_190.addWidget(self.progresbarRadius)


        self.verticalLayout_2.addWidget(self.progresbar_radius)

        self.progresbar_radiusPx = QFrame(self.baseWidgets)
        self.progresbar_radiusPx.setObjectName(u"progresbar_radiusPx")
        self.progresbar_radiusPx.setMinimumSize(QSize(0, 24))
        self.progresbar_radiusPx.setMaximumSize(QSize(16777215, 24))
        self.progresbar_radiusPx.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbar_radiusPx.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.progresbar_radiusPx)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(16, 0, 0, 0)
        self.frame_251 = QFrame(self.progresbar_radiusPx)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMinimumSize(QSize(0, 24))
        self.frame_251.setMaximumSize(QSize(0, 24))
        self.frame_251.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_19.addWidget(self.frame_251)

        self.progresbarRadiusPx = ClickableLineEdit(self.progresbar_radiusPx)
        self.progresbarRadiusPx.setObjectName(u"progresbarRadiusPx")
        self.progresbarRadiusPx.setMinimumSize(QSize(80, 24))
        self.progresbarRadiusPx.setMaximumSize(QSize(80, 24))
        self.progresbarRadiusPx.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_19.addWidget(self.progresbarRadiusPx)

        self.frame_256 = QFrame(self.progresbar_radiusPx)
        self.frame_256.setObjectName(u"frame_256")
        self.frame_256.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_19.addWidget(self.frame_256)


        self.verticalLayout_2.addWidget(self.progresbar_radiusPx)

        self.progresbar_position = QFrame(self.baseWidgets)
        self.progresbar_position.setObjectName(u"progresbar_position")
        self.progresbar_position.setMinimumSize(QSize(0, 24))
        self.progresbar_position.setMaximumSize(QSize(16777215, 24))
        self.progresbar_position.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbar_position.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_203 = QHBoxLayout(self.progresbar_position)
        self.horizontalLayout_203.setSpacing(0)
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.horizontalLayout_203.setContentsMargins(16, 0, 0, 0)
        self.frame_330 = QFrame(self.progresbar_position)
        self.frame_330.setObjectName(u"frame_330")
        self.frame_330.setMaximumSize(QSize(0, 24))
        self.frame_330.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_330.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_330.setLineWidth(0)

        self.horizontalLayout_203.addWidget(self.frame_330)

        self.progresbarPosition = ClickableLabel(self.progresbar_position)
        self.progresbarPosition.setObjectName(u"progresbarPosition")
        self.progresbarPosition.setMinimumSize(QSize(0, 24))
        self.progresbarPosition.setMaximumSize(QSize(16777215, 24))
        self.progresbarPosition.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_203.addWidget(self.progresbarPosition)


        self.verticalLayout_2.addWidget(self.progresbar_position)

        self.progresbar_positionXY = QFrame(self.baseWidgets)
        self.progresbar_positionXY.setObjectName(u"progresbar_positionXY")
        self.progresbar_positionXY.setMinimumSize(QSize(0, 24))
        self.progresbar_positionXY.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_197 = QHBoxLayout(self.progresbar_positionXY)
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.horizontalLayout_197.setContentsMargins(16, 0, 0, 0)
        self.progresbarPositionX = ClickableLineEdit(self.progresbar_positionXY)
        self.progresbarPositionX.setObjectName(u"progresbarPositionX")
        self.progresbarPositionX.setMinimumSize(QSize(70, 24))
        self.progresbarPositionX.setMaximumSize(QSize(70, 24))
        self.progresbarPositionX.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_197.addWidget(self.progresbarPositionX)

        self.progresbarPositionY = ClickableLineEdit(self.progresbar_positionXY)
        self.progresbarPositionY.setObjectName(u"progresbarPositionY")
        self.progresbarPositionY.setMinimumSize(QSize(70, 24))
        self.progresbarPositionY.setMaximumSize(QSize(70, 24))
        self.progresbarPositionY.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_197.addWidget(self.progresbarPositionY)

        self.frame_316 = QFrame(self.progresbar_positionXY)
        self.frame_316.setObjectName(u"frame_316")
        self.frame_316.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_316.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_197.addWidget(self.frame_316)


        self.verticalLayout_2.addWidget(self.progresbar_positionXY)

        self.progresbarAdd_color = QFrame(self.baseWidgets)
        self.progresbarAdd_color.setObjectName(u"progresbarAdd_color")
        self.progresbarAdd_color.setMinimumSize(QSize(0, 30))
        self.progresbarAdd_color.setMaximumSize(QSize(16777215, 30))
        self.progresbarAdd_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarAdd_color.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_209 = QHBoxLayout(self.progresbarAdd_color)
        self.horizontalLayout_209.setSpacing(0)
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.horizontalLayout_209.setContentsMargins(16, 0, 0, 0)
        self.progresbarAddColor = ClickableLabel(self.progresbarAdd_color)
        self.progresbarAddColor.setObjectName(u"progresbarAddColor")
        self.progresbarAddColor.setMinimumSize(QSize(0, 30))
        self.progresbarAddColor.setMaximumSize(QSize(16777215, 30))
        self.progresbarAddColor.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_209.addWidget(self.progresbarAddColor)

        self.frame_342 = QFrame(self.progresbarAdd_color)
        self.frame_342.setObjectName(u"frame_342")
        self.frame_342.setMinimumSize(QSize(0, 30))
        self.frame_342.setMaximumSize(QSize(0, 30))
        self.frame_342.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_342.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_209.addWidget(self.frame_342)


        self.verticalLayout_2.addWidget(self.progresbarAdd_color)

        self.progresbarAdd_color1 = QFrame(self.baseWidgets)
        self.progresbarAdd_color1.setObjectName(u"progresbarAdd_color1")
        self.progresbarAdd_color1.setMinimumSize(QSize(0, 24))
        self.progresbarAdd_color1.setMaximumSize(QSize(16777215, 24))
        self.progresbarAdd_color1.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarAdd_color1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_208 = QHBoxLayout(self.progresbarAdd_color1)
        self.horizontalLayout_208.setSpacing(0)
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.horizontalLayout_208.setContentsMargins(32, 0, 0, 0)
        self.frame_340 = QFrame(self.progresbarAdd_color1)
        self.frame_340.setObjectName(u"frame_340")
        self.frame_340.setMaximumSize(QSize(0, 24))
        self.frame_340.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_340.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_340.setLineWidth(0)

        self.horizontalLayout_208.addWidget(self.frame_340)

        self.progresbarAddColor1 = ClickableLabel(self.progresbarAdd_color1)
        self.progresbarAddColor1.setObjectName(u"progresbarAddColor1")
        self.progresbarAddColor1.setMinimumSize(QSize(0, 24))
        self.progresbarAddColor1.setMaximumSize(QSize(16777215, 24))
        self.progresbarAddColor1.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_208.addWidget(self.progresbarAddColor1)


        self.verticalLayout_2.addWidget(self.progresbarAdd_color1)

        self.progressbarAdd_color1RGBA = QFrame(self.baseWidgets)
        self.progressbarAdd_color1RGBA.setObjectName(u"progressbarAdd_color1RGBA")
        self.progressbarAdd_color1RGBA.setMinimumSize(QSize(0, 24))
        self.progressbarAdd_color1RGBA.setMaximumSize(QSize(16777215, 24))
        self.progressbarAdd_color1RGBA.setStyleSheet(u"")
        self.horizontalLayout_201 = QHBoxLayout(self.progressbarAdd_color1RGBA)
        self.horizontalLayout_201.setSpacing(6)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(32, 0, 0, 0)
        self.progressbarAddColor1R = ClickableLineEdit(self.progressbarAdd_color1RGBA)
        self.progressbarAddColor1R.setObjectName(u"progressbarAddColor1R")
        sizePolicy1.setHeightForWidth(self.progressbarAddColor1R.sizePolicy().hasHeightForWidth())
        self.progressbarAddColor1R.setSizePolicy(sizePolicy1)
        self.progressbarAddColor1R.setMinimumSize(QSize(50, 24))
        self.progressbarAddColor1R.setMaximumSize(QSize(50, 24))
        self.progressbarAddColor1R.setSizeIncrement(QSize(0, 0))
        self.progressbarAddColor1R.setBaseSize(QSize(0, 18))
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
        self.progressbarAddColor1R.setPalette(palette7)
        self.progressbarAddColor1R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressbarAddColor1R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_201.addWidget(self.progressbarAddColor1R)

        self.progressbarAddColor1G = ClickableLineEdit(self.progressbarAdd_color1RGBA)
        self.progressbarAddColor1G.setObjectName(u"progressbarAddColor1G")
        sizePolicy1.setHeightForWidth(self.progressbarAddColor1G.sizePolicy().hasHeightForWidth())
        self.progressbarAddColor1G.setSizePolicy(sizePolicy1)
        self.progressbarAddColor1G.setMinimumSize(QSize(50, 24))
        self.progressbarAddColor1G.setMaximumSize(QSize(50, 24))
        self.progressbarAddColor1G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_201.addWidget(self.progressbarAddColor1G)

        self.progressbarAddColor1B = ClickableLineEdit(self.progressbarAdd_color1RGBA)
        self.progressbarAddColor1B.setObjectName(u"progressbarAddColor1B")
        sizePolicy1.setHeightForWidth(self.progressbarAddColor1B.sizePolicy().hasHeightForWidth())
        self.progressbarAddColor1B.setSizePolicy(sizePolicy1)
        self.progressbarAddColor1B.setMinimumSize(QSize(50, 24))
        self.progressbarAddColor1B.setMaximumSize(QSize(50, 24))
        self.progressbarAddColor1B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_201.addWidget(self.progressbarAddColor1B)

        self.progressbarAddColor1A = ClickableLineEdit(self.progressbarAdd_color1RGBA)
        self.progressbarAddColor1A.setObjectName(u"progressbarAddColor1A")
        sizePolicy1.setHeightForWidth(self.progressbarAddColor1A.sizePolicy().hasHeightForWidth())
        self.progressbarAddColor1A.setSizePolicy(sizePolicy1)
        self.progressbarAddColor1A.setMinimumSize(QSize(50, 24))
        self.progressbarAddColor1A.setMaximumSize(QSize(50, 24))
        self.progressbarAddColor1A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_201.addWidget(self.progressbarAddColor1A)

        self.frame_324 = QFrame(self.progressbarAdd_color1RGBA)
        self.frame_324.setObjectName(u"frame_324")
        sizePolicy2.setHeightForWidth(self.frame_324.sizePolicy().hasHeightForWidth())
        self.frame_324.setSizePolicy(sizePolicy2)
        self.frame_324.setMinimumSize(QSize(0, 24))
        self.frame_324.setMaximumSize(QSize(16777215, 24))
        self.frame_324.setFont(font)
        self.frame_324.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_324.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_201.addWidget(self.frame_324)


        self.verticalLayout_2.addWidget(self.progressbarAdd_color1RGBA)

        self.fixedColor_progrsbarAdd = QFrame(self.baseWidgets)
        self.fixedColor_progrsbarAdd.setObjectName(u"fixedColor_progrsbarAdd")
        self.fixedColor_progrsbarAdd.setMinimumSize(QSize(0, 20))
        self.fixedColor_progrsbarAdd.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_200 = QHBoxLayout(self.fixedColor_progrsbarAdd)
        self.horizontalLayout_200.setSpacing(5)
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalLayout_200.setContentsMargins(32, 0, 0, 0)
        self.fixedColorProgrsbarAdd = ClickableLabel(self.fixedColor_progrsbarAdd)
        self.fixedColorProgrsbarAdd.setObjectName(u"fixedColorProgrsbarAdd")
        self.fixedColorProgrsbarAdd.setMinimumSize(QSize(195, 0))
        self.fixedColorProgrsbarAdd.setMaximumSize(QSize(195, 24))
        self.fixedColorProgrsbarAdd.setStyleSheet(u"")

        self.horizontalLayout_200.addWidget(self.fixedColorProgrsbarAdd)

        self.fixedColorProgrsbarAddCheckBox = QCheckBox(self.fixedColor_progrsbarAdd)
        self.fixedColorProgrsbarAddCheckBox.setObjectName(u"fixedColorProgrsbarAddCheckBox")
        self.fixedColorProgrsbarAddCheckBox.setMaximumSize(QSize(16777215, 24))
        self.fixedColorProgrsbarAddCheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.fixedColorProgrsbarAddCheckBox.setIconSize(QSize(18, 18))
        self.fixedColorProgrsbarAddCheckBox.setChecked(False)
        self.fixedColorProgrsbarAddCheckBox.setTristate(False)

        self.horizontalLayout_200.addWidget(self.fixedColorProgrsbarAddCheckBox)


        self.verticalLayout_2.addWidget(self.fixedColor_progrsbarAdd)

        self.progressbarAdd_threshold = QFrame(self.baseWidgets)
        self.progressbarAdd_threshold.setObjectName(u"progressbarAdd_threshold")
        self.progressbarAdd_threshold.setMinimumSize(QSize(0, 24))
        self.progressbarAdd_threshold.setMaximumSize(QSize(16777215, 24))
        self.progressbarAdd_threshold.setFrameShape(QFrame.Shape.StyledPanel)
        self.progressbarAdd_threshold.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_202 = QHBoxLayout(self.progressbarAdd_threshold)
        self.horizontalLayout_202.setSpacing(0)
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.horizontalLayout_202.setContentsMargins(32, 0, 0, 0)
        self.frame_326 = QFrame(self.progressbarAdd_threshold)
        self.frame_326.setObjectName(u"frame_326")
        self.frame_326.setMaximumSize(QSize(0, 24))
        self.frame_326.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_326.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_326.setLineWidth(0)

        self.horizontalLayout_202.addWidget(self.frame_326)

        self.progressbarAddThreshold = ClickableLabel(self.progressbarAdd_threshold)
        self.progressbarAddThreshold.setObjectName(u"progressbarAddThreshold")
        self.progressbarAddThreshold.setMinimumSize(QSize(0, 24))
        self.progressbarAddThreshold.setMaximumSize(QSize(16777215, 24))
        self.progressbarAddThreshold.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_202.addWidget(self.progressbarAddThreshold)


        self.verticalLayout_2.addWidget(self.progressbarAdd_threshold)

        self.progresbarAdd_thresholdRGB = QFrame(self.baseWidgets)
        self.progresbarAdd_thresholdRGB.setObjectName(u"progresbarAdd_thresholdRGB")
        self.progresbarAdd_thresholdRGB.setMinimumSize(QSize(0, 24))
        self.progresbarAdd_thresholdRGB.setMaximumSize(QSize(16777215, 24))
        self.progresbarAdd_thresholdRGB.setStyleSheet(u"")
        self.horizontalLayout_196 = QHBoxLayout(self.progresbarAdd_thresholdRGB)
        self.horizontalLayout_196.setSpacing(6)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_196.setContentsMargins(32, 0, 0, 0)
        self.progresbarAddThresholdR = ClickableLineEdit(self.progresbarAdd_thresholdRGB)
        self.progresbarAddThresholdR.setObjectName(u"progresbarAddThresholdR")
        sizePolicy1.setHeightForWidth(self.progresbarAddThresholdR.sizePolicy().hasHeightForWidth())
        self.progresbarAddThresholdR.setSizePolicy(sizePolicy1)
        self.progresbarAddThresholdR.setMinimumSize(QSize(50, 24))
        self.progresbarAddThresholdR.setMaximumSize(QSize(50, 24))
        self.progresbarAddThresholdR.setSizeIncrement(QSize(0, 0))
        self.progresbarAddThresholdR.setBaseSize(QSize(0, 18))
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
        self.progresbarAddThresholdR.setPalette(palette8)
        self.progresbarAddThresholdR.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progresbarAddThresholdR.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_196.addWidget(self.progresbarAddThresholdR)

        self.progresbarAddThresholdG = ClickableLineEdit(self.progresbarAdd_thresholdRGB)
        self.progresbarAddThresholdG.setObjectName(u"progresbarAddThresholdG")
        sizePolicy1.setHeightForWidth(self.progresbarAddThresholdG.sizePolicy().hasHeightForWidth())
        self.progresbarAddThresholdG.setSizePolicy(sizePolicy1)
        self.progresbarAddThresholdG.setMinimumSize(QSize(50, 24))
        self.progresbarAddThresholdG.setMaximumSize(QSize(50, 24))
        self.progresbarAddThresholdG.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_196.addWidget(self.progresbarAddThresholdG)

        self.progresbarAddThresholdB = ClickableLineEdit(self.progresbarAdd_thresholdRGB)
        self.progresbarAddThresholdB.setObjectName(u"progresbarAddThresholdB")
        sizePolicy1.setHeightForWidth(self.progresbarAddThresholdB.sizePolicy().hasHeightForWidth())
        self.progresbarAddThresholdB.setSizePolicy(sizePolicy1)
        self.progresbarAddThresholdB.setMinimumSize(QSize(50, 24))
        self.progresbarAddThresholdB.setMaximumSize(QSize(50, 24))
        self.progresbarAddThresholdB.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_196.addWidget(self.progresbarAddThresholdB)

        self.frame_314 = QFrame(self.progresbarAdd_thresholdRGB)
        self.frame_314.setObjectName(u"frame_314")
        sizePolicy2.setHeightForWidth(self.frame_314.sizePolicy().hasHeightForWidth())
        self.frame_314.setSizePolicy(sizePolicy2)
        self.frame_314.setMinimumSize(QSize(0, 24))
        self.frame_314.setMaximumSize(QSize(16777215, 24))
        self.frame_314.setFont(font)
        self.frame_314.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_314.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_196.addWidget(self.frame_314)


        self.verticalLayout_2.addWidget(self.progresbarAdd_thresholdRGB)

        self.progresbarAdd_thresholdMode = QFrame(self.baseWidgets)
        self.progresbarAdd_thresholdMode.setObjectName(u"progresbarAdd_thresholdMode")
        self.progresbarAdd_thresholdMode.setMinimumSize(QSize(0, 24))
        self.progresbarAdd_thresholdMode.setMaximumSize(QSize(16777215, 24))
        self.progresbarAdd_thresholdMode.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarAdd_thresholdMode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_192 = QHBoxLayout(self.progresbarAdd_thresholdMode)
        self.horizontalLayout_192.setSpacing(0)
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.horizontalLayout_192.setContentsMargins(32, 0, 0, 0)
        self.frame_306 = QFrame(self.progresbarAdd_thresholdMode)
        self.frame_306.setObjectName(u"frame_306")
        self.frame_306.setMaximumSize(QSize(0, 24))
        self.frame_306.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_306.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_306.setLineWidth(0)

        self.horizontalLayout_192.addWidget(self.frame_306)

        self.progresbarAddThresholdMode = ClickableLabel(self.progresbarAdd_thresholdMode)
        self.progresbarAddThresholdMode.setObjectName(u"progresbarAddThresholdMode")
        self.progresbarAddThresholdMode.setMinimumSize(QSize(0, 24))
        self.progresbarAddThresholdMode.setMaximumSize(QSize(16777215, 24))
        self.progresbarAddThresholdMode.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_192.addWidget(self.progresbarAddThresholdMode)


        self.verticalLayout_2.addWidget(self.progresbarAdd_thresholdMode)

        self.progresbarAdd_thresholdModeComboBox = QFrame(self.baseWidgets)
        self.progresbarAdd_thresholdModeComboBox.setObjectName(u"progresbarAdd_thresholdModeComboBox")
        self.progresbarAdd_thresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.progresbarAdd_thresholdModeComboBox.setMaximumSize(QSize(16777215, 24))
        self.progresbarAdd_thresholdModeComboBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarAdd_thresholdModeComboBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_199 = QHBoxLayout(self.progresbarAdd_thresholdModeComboBox)
        self.horizontalLayout_199.setSpacing(0)
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.horizontalLayout_199.setContentsMargins(32, 0, 0, 0)
        self.frame_320 = QFrame(self.progresbarAdd_thresholdModeComboBox)
        self.frame_320.setObjectName(u"frame_320")
        self.frame_320.setMinimumSize(QSize(0, 24))
        self.frame_320.setMaximumSize(QSize(0, 24))
        self.frame_320.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_320.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_199.addWidget(self.frame_320)

        self.progresbarAddThresholdModeComboBox = QComboBox(self.progresbarAdd_thresholdModeComboBox)
        self.progresbarAddThresholdModeComboBox.addItem("")
        self.progresbarAddThresholdModeComboBox.addItem("")
        self.progresbarAddThresholdModeComboBox.addItem("")
        self.progresbarAddThresholdModeComboBox.addItem("")
        self.progresbarAddThresholdModeComboBox.addItem("")
        self.progresbarAddThresholdModeComboBox.setObjectName(u"progresbarAddThresholdModeComboBox")
        self.progresbarAddThresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.progresbarAddThresholdModeComboBox.setMaximumSize(QSize(80, 24))
        self.progresbarAddThresholdModeComboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_199.addWidget(self.progresbarAddThresholdModeComboBox)

        self.frame_321 = QFrame(self.progresbarAdd_thresholdModeComboBox)
        self.frame_321.setObjectName(u"frame_321")
        self.frame_321.setMinimumSize(QSize(0, 24))
        self.frame_321.setMaximumSize(QSize(16777215, 24))
        self.frame_321.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_321.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_199.addWidget(self.frame_321)


        self.verticalLayout_2.addWidget(self.progresbarAdd_thresholdModeComboBox)

        self.progresbarAdd_color2 = QFrame(self.baseWidgets)
        self.progresbarAdd_color2.setObjectName(u"progresbarAdd_color2")
        self.progresbarAdd_color2.setMinimumSize(QSize(0, 24))
        self.progresbarAdd_color2.setMaximumSize(QSize(16777215, 24))
        self.progresbarAdd_color2.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarAdd_color2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_195 = QHBoxLayout(self.progresbarAdd_color2)
        self.horizontalLayout_195.setSpacing(0)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(32, 0, 0, 0)
        self.frame_312 = QFrame(self.progresbarAdd_color2)
        self.frame_312.setObjectName(u"frame_312")
        self.frame_312.setMaximumSize(QSize(0, 24))
        self.frame_312.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_312.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_312.setLineWidth(0)

        self.horizontalLayout_195.addWidget(self.frame_312)

        self.progresbarAddColor2 = ClickableLabel(self.progresbarAdd_color2)
        self.progresbarAddColor2.setObjectName(u"progresbarAddColor2")
        self.progresbarAddColor2.setMinimumSize(QSize(0, 24))
        self.progresbarAddColor2.setMaximumSize(QSize(16777215, 24))
        self.progresbarAddColor2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_195.addWidget(self.progresbarAddColor2)


        self.verticalLayout_2.addWidget(self.progresbarAdd_color2)

        self.progresbarAdd_color2RGBA = QFrame(self.baseWidgets)
        self.progresbarAdd_color2RGBA.setObjectName(u"progresbarAdd_color2RGBA")
        self.progresbarAdd_color2RGBA.setMinimumSize(QSize(0, 24))
        self.progresbarAdd_color2RGBA.setMaximumSize(QSize(16777215, 24))
        self.progresbarAdd_color2RGBA.setStyleSheet(u"")
        self.horizontalLayout_193 = QHBoxLayout(self.progresbarAdd_color2RGBA)
        self.horizontalLayout_193.setSpacing(6)
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(32, 0, 0, 0)
        self.progresbarAddColor2R = ClickableLineEdit(self.progresbarAdd_color2RGBA)
        self.progresbarAddColor2R.setObjectName(u"progresbarAddColor2R")
        sizePolicy1.setHeightForWidth(self.progresbarAddColor2R.sizePolicy().hasHeightForWidth())
        self.progresbarAddColor2R.setSizePolicy(sizePolicy1)
        self.progresbarAddColor2R.setMinimumSize(QSize(50, 24))
        self.progresbarAddColor2R.setMaximumSize(QSize(50, 24))
        self.progresbarAddColor2R.setSizeIncrement(QSize(0, 0))
        self.progresbarAddColor2R.setBaseSize(QSize(0, 18))
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
        self.progresbarAddColor2R.setPalette(palette9)
        self.progresbarAddColor2R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progresbarAddColor2R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_193.addWidget(self.progresbarAddColor2R)

        self.progresbarAddColor2G = ClickableLineEdit(self.progresbarAdd_color2RGBA)
        self.progresbarAddColor2G.setObjectName(u"progresbarAddColor2G")
        sizePolicy1.setHeightForWidth(self.progresbarAddColor2G.sizePolicy().hasHeightForWidth())
        self.progresbarAddColor2G.setSizePolicy(sizePolicy1)
        self.progresbarAddColor2G.setMinimumSize(QSize(50, 24))
        self.progresbarAddColor2G.setMaximumSize(QSize(50, 24))
        self.progresbarAddColor2G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_193.addWidget(self.progresbarAddColor2G)

        self.progresbarAddColor2B = ClickableLineEdit(self.progresbarAdd_color2RGBA)
        self.progresbarAddColor2B.setObjectName(u"progresbarAddColor2B")
        sizePolicy1.setHeightForWidth(self.progresbarAddColor2B.sizePolicy().hasHeightForWidth())
        self.progresbarAddColor2B.setSizePolicy(sizePolicy1)
        self.progresbarAddColor2B.setMinimumSize(QSize(50, 24))
        self.progresbarAddColor2B.setMaximumSize(QSize(50, 24))
        self.progresbarAddColor2B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_193.addWidget(self.progresbarAddColor2B)

        self.progresbarAddColor2A = ClickableLineEdit(self.progresbarAdd_color2RGBA)
        self.progresbarAddColor2A.setObjectName(u"progresbarAddColor2A")
        sizePolicy1.setHeightForWidth(self.progresbarAddColor2A.sizePolicy().hasHeightForWidth())
        self.progresbarAddColor2A.setSizePolicy(sizePolicy1)
        self.progresbarAddColor2A.setMinimumSize(QSize(50, 24))
        self.progresbarAddColor2A.setMaximumSize(QSize(50, 24))
        self.progresbarAddColor2A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_193.addWidget(self.progresbarAddColor2A)

        self.frame_308 = QFrame(self.progresbarAdd_color2RGBA)
        self.frame_308.setObjectName(u"frame_308")
        sizePolicy2.setHeightForWidth(self.frame_308.sizePolicy().hasHeightForWidth())
        self.frame_308.setSizePolicy(sizePolicy2)
        self.frame_308.setMinimumSize(QSize(0, 24))
        self.frame_308.setMaximumSize(QSize(16777215, 24))
        self.frame_308.setFont(font)
        self.frame_308.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_308.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_193.addWidget(self.frame_308)


        self.verticalLayout_2.addWidget(self.progresbarAdd_color2RGBA)

        self.progresbarSub_color = QFrame(self.baseWidgets)
        self.progresbarSub_color.setObjectName(u"progresbarSub_color")
        self.progresbarSub_color.setMinimumSize(QSize(0, 30))
        self.progresbarSub_color.setMaximumSize(QSize(16777215, 30))
        self.progresbarSub_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarSub_color.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_210 = QHBoxLayout(self.progresbarSub_color)
        self.horizontalLayout_210.setSpacing(0)
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.horizontalLayout_210.setContentsMargins(16, 0, 0, 0)
        self.progresbarSubColor = ClickableLabel(self.progresbarSub_color)
        self.progresbarSubColor.setObjectName(u"progresbarSubColor")
        self.progresbarSubColor.setMinimumSize(QSize(0, 30))
        self.progresbarSubColor.setMaximumSize(QSize(16777215, 30))
        self.progresbarSubColor.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_210.addWidget(self.progresbarSubColor)

        self.frame_344 = QFrame(self.progresbarSub_color)
        self.frame_344.setObjectName(u"frame_344")
        self.frame_344.setMinimumSize(QSize(0, 30))
        self.frame_344.setMaximumSize(QSize(0, 30))
        self.frame_344.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_344.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_210.addWidget(self.frame_344)


        self.verticalLayout_2.addWidget(self.progresbarSub_color)

        self.progresbarSub_color1 = QFrame(self.baseWidgets)
        self.progresbarSub_color1.setObjectName(u"progresbarSub_color1")
        self.progresbarSub_color1.setMinimumSize(QSize(0, 24))
        self.progresbarSub_color1.setMaximumSize(QSize(16777215, 24))
        self.progresbarSub_color1.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarSub_color1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_211 = QHBoxLayout(self.progresbarSub_color1)
        self.horizontalLayout_211.setSpacing(0)
        self.horizontalLayout_211.setObjectName(u"horizontalLayout_211")
        self.horizontalLayout_211.setContentsMargins(32, 0, 0, 0)
        self.frame_346 = QFrame(self.progresbarSub_color1)
        self.frame_346.setObjectName(u"frame_346")
        self.frame_346.setMaximumSize(QSize(0, 24))
        self.frame_346.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_346.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_346.setLineWidth(0)

        self.horizontalLayout_211.addWidget(self.frame_346)

        self.progresbarSubColor1 = ClickableLabel(self.progresbarSub_color1)
        self.progresbarSubColor1.setObjectName(u"progresbarSubColor1")
        self.progresbarSubColor1.setMinimumSize(QSize(0, 24))
        self.progresbarSubColor1.setMaximumSize(QSize(16777215, 24))
        self.progresbarSubColor1.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_211.addWidget(self.progresbarSubColor1)


        self.verticalLayout_2.addWidget(self.progresbarSub_color1)

        self.progressbarSub_color1RGBA = QFrame(self.baseWidgets)
        self.progressbarSub_color1RGBA.setObjectName(u"progressbarSub_color1RGBA")
        self.progressbarSub_color1RGBA.setMinimumSize(QSize(0, 24))
        self.progressbarSub_color1RGBA.setMaximumSize(QSize(16777215, 24))
        self.progressbarSub_color1RGBA.setStyleSheet(u"")
        self.horizontalLayout_204 = QHBoxLayout(self.progressbarSub_color1RGBA)
        self.horizontalLayout_204.setSpacing(6)
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.horizontalLayout_204.setContentsMargins(32, 0, 0, 0)
        self.progressbarSubColor1R = ClickableLineEdit(self.progressbarSub_color1RGBA)
        self.progressbarSubColor1R.setObjectName(u"progressbarSubColor1R")
        sizePolicy1.setHeightForWidth(self.progressbarSubColor1R.sizePolicy().hasHeightForWidth())
        self.progressbarSubColor1R.setSizePolicy(sizePolicy1)
        self.progressbarSubColor1R.setMinimumSize(QSize(50, 24))
        self.progressbarSubColor1R.setMaximumSize(QSize(50, 24))
        self.progressbarSubColor1R.setSizeIncrement(QSize(0, 0))
        self.progressbarSubColor1R.setBaseSize(QSize(0, 18))
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
        self.progressbarSubColor1R.setPalette(palette10)
        self.progressbarSubColor1R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressbarSubColor1R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_204.addWidget(self.progressbarSubColor1R)

        self.progressbarSubColor1G = ClickableLineEdit(self.progressbarSub_color1RGBA)
        self.progressbarSubColor1G.setObjectName(u"progressbarSubColor1G")
        sizePolicy1.setHeightForWidth(self.progressbarSubColor1G.sizePolicy().hasHeightForWidth())
        self.progressbarSubColor1G.setSizePolicy(sizePolicy1)
        self.progressbarSubColor1G.setMinimumSize(QSize(50, 24))
        self.progressbarSubColor1G.setMaximumSize(QSize(50, 24))
        self.progressbarSubColor1G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_204.addWidget(self.progressbarSubColor1G)

        self.progressbarSubColor1B = ClickableLineEdit(self.progressbarSub_color1RGBA)
        self.progressbarSubColor1B.setObjectName(u"progressbarSubColor1B")
        sizePolicy1.setHeightForWidth(self.progressbarSubColor1B.sizePolicy().hasHeightForWidth())
        self.progressbarSubColor1B.setSizePolicy(sizePolicy1)
        self.progressbarSubColor1B.setMinimumSize(QSize(50, 24))
        self.progressbarSubColor1B.setMaximumSize(QSize(50, 24))
        self.progressbarSubColor1B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_204.addWidget(self.progressbarSubColor1B)

        self.progressbarSubColor1A = ClickableLineEdit(self.progressbarSub_color1RGBA)
        self.progressbarSubColor1A.setObjectName(u"progressbarSubColor1A")
        sizePolicy1.setHeightForWidth(self.progressbarSubColor1A.sizePolicy().hasHeightForWidth())
        self.progressbarSubColor1A.setSizePolicy(sizePolicy1)
        self.progressbarSubColor1A.setMinimumSize(QSize(50, 24))
        self.progressbarSubColor1A.setMaximumSize(QSize(50, 24))
        self.progressbarSubColor1A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_204.addWidget(self.progressbarSubColor1A)

        self.frame_329 = QFrame(self.progressbarSub_color1RGBA)
        self.frame_329.setObjectName(u"frame_329")
        sizePolicy2.setHeightForWidth(self.frame_329.sizePolicy().hasHeightForWidth())
        self.frame_329.setSizePolicy(sizePolicy2)
        self.frame_329.setMinimumSize(QSize(0, 24))
        self.frame_329.setMaximumSize(QSize(16777215, 24))
        self.frame_329.setFont(font)
        self.frame_329.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_329.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_204.addWidget(self.frame_329)


        self.verticalLayout_2.addWidget(self.progressbarSub_color1RGBA)

        self.fixedColor_progresbarSub = QFrame(self.baseWidgets)
        self.fixedColor_progresbarSub.setObjectName(u"fixedColor_progresbarSub")
        self.fixedColor_progresbarSub.setMinimumSize(QSize(0, 20))
        self.fixedColor_progresbarSub.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_212 = QHBoxLayout(self.fixedColor_progresbarSub)
        self.horizontalLayout_212.setSpacing(5)
        self.horizontalLayout_212.setObjectName(u"horizontalLayout_212")
        self.horizontalLayout_212.setContentsMargins(32, 0, 0, 0)
        self.fixedColorProgresbarSub = ClickableLabel(self.fixedColor_progresbarSub)
        self.fixedColorProgresbarSub.setObjectName(u"fixedColorProgresbarSub")
        self.fixedColorProgresbarSub.setMinimumSize(QSize(195, 0))
        self.fixedColorProgresbarSub.setMaximumSize(QSize(195, 24))
        self.fixedColorProgresbarSub.setStyleSheet(u"")

        self.horizontalLayout_212.addWidget(self.fixedColorProgresbarSub)

        self.fixedColorProgresbarSubCheckBox = QCheckBox(self.fixedColor_progresbarSub)
        self.fixedColorProgresbarSubCheckBox.setObjectName(u"fixedColorProgresbarSubCheckBox")
        self.fixedColorProgresbarSubCheckBox.setMaximumSize(QSize(16777215, 24))
        self.fixedColorProgresbarSubCheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.fixedColorProgresbarSubCheckBox.setIconSize(QSize(18, 18))
        self.fixedColorProgresbarSubCheckBox.setChecked(False)
        self.fixedColorProgresbarSubCheckBox.setTristate(False)

        self.horizontalLayout_212.addWidget(self.fixedColorProgresbarSubCheckBox)


        self.verticalLayout_2.addWidget(self.fixedColor_progresbarSub)

        self.progresbarSub_threshold = QFrame(self.baseWidgets)
        self.progresbarSub_threshold.setObjectName(u"progresbarSub_threshold")
        self.progresbarSub_threshold.setMinimumSize(QSize(0, 24))
        self.progresbarSub_threshold.setMaximumSize(QSize(16777215, 24))
        self.progresbarSub_threshold.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarSub_threshold.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_213 = QHBoxLayout(self.progresbarSub_threshold)
        self.horizontalLayout_213.setSpacing(0)
        self.horizontalLayout_213.setObjectName(u"horizontalLayout_213")
        self.horizontalLayout_213.setContentsMargins(32, 0, 0, 0)
        self.frame_349 = QFrame(self.progresbarSub_threshold)
        self.frame_349.setObjectName(u"frame_349")
        self.frame_349.setMaximumSize(QSize(0, 24))
        self.frame_349.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_349.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_349.setLineWidth(0)

        self.horizontalLayout_213.addWidget(self.frame_349)

        self.progresbarSubThreshold = ClickableLabel(self.progresbarSub_threshold)
        self.progresbarSubThreshold.setObjectName(u"progresbarSubThreshold")
        self.progresbarSubThreshold.setMinimumSize(QSize(0, 24))
        self.progresbarSubThreshold.setMaximumSize(QSize(16777215, 24))
        self.progresbarSubThreshold.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_213.addWidget(self.progresbarSubThreshold)


        self.verticalLayout_2.addWidget(self.progresbarSub_threshold)

        self.progresbarSub_thresholdRGB = QFrame(self.baseWidgets)
        self.progresbarSub_thresholdRGB.setObjectName(u"progresbarSub_thresholdRGB")
        self.progresbarSub_thresholdRGB.setMinimumSize(QSize(0, 24))
        self.progresbarSub_thresholdRGB.setMaximumSize(QSize(16777215, 24))
        self.progresbarSub_thresholdRGB.setStyleSheet(u"")
        self.horizontalLayout_214 = QHBoxLayout(self.progresbarSub_thresholdRGB)
        self.horizontalLayout_214.setSpacing(6)
        self.horizontalLayout_214.setObjectName(u"horizontalLayout_214")
        self.horizontalLayout_214.setContentsMargins(32, 0, 0, 0)
        self.progresbarSubThresholdR = ClickableLineEdit(self.progresbarSub_thresholdRGB)
        self.progresbarSubThresholdR.setObjectName(u"progresbarSubThresholdR")
        sizePolicy1.setHeightForWidth(self.progresbarSubThresholdR.sizePolicy().hasHeightForWidth())
        self.progresbarSubThresholdR.setSizePolicy(sizePolicy1)
        self.progresbarSubThresholdR.setMinimumSize(QSize(50, 24))
        self.progresbarSubThresholdR.setMaximumSize(QSize(50, 24))
        self.progresbarSubThresholdR.setSizeIncrement(QSize(0, 0))
        self.progresbarSubThresholdR.setBaseSize(QSize(0, 18))
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
        self.progresbarSubThresholdR.setPalette(palette11)
        self.progresbarSubThresholdR.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progresbarSubThresholdR.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_214.addWidget(self.progresbarSubThresholdR)

        self.progresbarSubThresholdG = ClickableLineEdit(self.progresbarSub_thresholdRGB)
        self.progresbarSubThresholdG.setObjectName(u"progresbarSubThresholdG")
        sizePolicy1.setHeightForWidth(self.progresbarSubThresholdG.sizePolicy().hasHeightForWidth())
        self.progresbarSubThresholdG.setSizePolicy(sizePolicy1)
        self.progresbarSubThresholdG.setMinimumSize(QSize(50, 24))
        self.progresbarSubThresholdG.setMaximumSize(QSize(50, 24))
        self.progresbarSubThresholdG.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_214.addWidget(self.progresbarSubThresholdG)

        self.progresbarSubThresholdB = ClickableLineEdit(self.progresbarSub_thresholdRGB)
        self.progresbarSubThresholdB.setObjectName(u"progresbarSubThresholdB")
        sizePolicy1.setHeightForWidth(self.progresbarSubThresholdB.sizePolicy().hasHeightForWidth())
        self.progresbarSubThresholdB.setSizePolicy(sizePolicy1)
        self.progresbarSubThresholdB.setMinimumSize(QSize(50, 24))
        self.progresbarSubThresholdB.setMaximumSize(QSize(50, 24))
        self.progresbarSubThresholdB.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_214.addWidget(self.progresbarSubThresholdB)

        self.frame_351 = QFrame(self.progresbarSub_thresholdRGB)
        self.frame_351.setObjectName(u"frame_351")
        sizePolicy2.setHeightForWidth(self.frame_351.sizePolicy().hasHeightForWidth())
        self.frame_351.setSizePolicy(sizePolicy2)
        self.frame_351.setMinimumSize(QSize(0, 24))
        self.frame_351.setMaximumSize(QSize(16777215, 24))
        self.frame_351.setFont(font)
        self.frame_351.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_351.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_214.addWidget(self.frame_351)


        self.verticalLayout_2.addWidget(self.progresbarSub_thresholdRGB)

        self.progresbarSub_thresholdMode = QFrame(self.baseWidgets)
        self.progresbarSub_thresholdMode.setObjectName(u"progresbarSub_thresholdMode")
        self.progresbarSub_thresholdMode.setMinimumSize(QSize(0, 24))
        self.progresbarSub_thresholdMode.setMaximumSize(QSize(16777215, 24))
        self.progresbarSub_thresholdMode.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarSub_thresholdMode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_194 = QHBoxLayout(self.progresbarSub_thresholdMode)
        self.horizontalLayout_194.setSpacing(0)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(32, 0, 0, 0)
        self.frame_334 = QFrame(self.progresbarSub_thresholdMode)
        self.frame_334.setObjectName(u"frame_334")
        self.frame_334.setMaximumSize(QSize(0, 24))
        self.frame_334.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_334.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_334.setLineWidth(0)

        self.horizontalLayout_194.addWidget(self.frame_334)

        self.progresbarSubThresholdMode = ClickableLabel(self.progresbarSub_thresholdMode)
        self.progresbarSubThresholdMode.setObjectName(u"progresbarSubThresholdMode")
        self.progresbarSubThresholdMode.setMinimumSize(QSize(0, 24))
        self.progresbarSubThresholdMode.setMaximumSize(QSize(16777215, 24))
        self.progresbarSubThresholdMode.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_194.addWidget(self.progresbarSubThresholdMode)


        self.verticalLayout_2.addWidget(self.progresbarSub_thresholdMode)

        self.progresbarSub_thresholdModeComboBox = QFrame(self.baseWidgets)
        self.progresbarSub_thresholdModeComboBox.setObjectName(u"progresbarSub_thresholdModeComboBox")
        self.progresbarSub_thresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.progresbarSub_thresholdModeComboBox.setMaximumSize(QSize(16777215, 24))
        self.progresbarSub_thresholdModeComboBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarSub_thresholdModeComboBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_215 = QHBoxLayout(self.progresbarSub_thresholdModeComboBox)
        self.horizontalLayout_215.setSpacing(0)
        self.horizontalLayout_215.setObjectName(u"horizontalLayout_215")
        self.horizontalLayout_215.setContentsMargins(32, 0, 0, 0)
        self.frame_353 = QFrame(self.progresbarSub_thresholdModeComboBox)
        self.frame_353.setObjectName(u"frame_353")
        self.frame_353.setMinimumSize(QSize(0, 24))
        self.frame_353.setMaximumSize(QSize(0, 24))
        self.frame_353.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_353.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_215.addWidget(self.frame_353)

        self.progresbarSubThresholdModeComboBox = QComboBox(self.progresbarSub_thresholdModeComboBox)
        self.progresbarSubThresholdModeComboBox.addItem("")
        self.progresbarSubThresholdModeComboBox.addItem("")
        self.progresbarSubThresholdModeComboBox.addItem("")
        self.progresbarSubThresholdModeComboBox.addItem("")
        self.progresbarSubThresholdModeComboBox.addItem("")
        self.progresbarSubThresholdModeComboBox.setObjectName(u"progresbarSubThresholdModeComboBox")
        self.progresbarSubThresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.progresbarSubThresholdModeComboBox.setMaximumSize(QSize(80, 24))
        self.progresbarSubThresholdModeComboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_215.addWidget(self.progresbarSubThresholdModeComboBox)

        self.frame_354 = QFrame(self.progresbarSub_thresholdModeComboBox)
        self.frame_354.setObjectName(u"frame_354")
        self.frame_354.setMinimumSize(QSize(0, 24))
        self.frame_354.setMaximumSize(QSize(16777215, 24))
        self.frame_354.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_354.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_215.addWidget(self.frame_354)


        self.verticalLayout_2.addWidget(self.progresbarSub_thresholdModeComboBox)

        self.progresbarSub_color2 = QFrame(self.baseWidgets)
        self.progresbarSub_color2.setObjectName(u"progresbarSub_color2")
        self.progresbarSub_color2.setMinimumSize(QSize(0, 24))
        self.progresbarSub_color2.setMaximumSize(QSize(16777215, 24))
        self.progresbarSub_color2.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarSub_color2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_198 = QHBoxLayout(self.progresbarSub_color2)
        self.horizontalLayout_198.setSpacing(0)
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.horizontalLayout_198.setContentsMargins(32, 0, 0, 0)
        self.frame_318 = QFrame(self.progresbarSub_color2)
        self.frame_318.setObjectName(u"frame_318")
        self.frame_318.setMaximumSize(QSize(0, 24))
        self.frame_318.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_318.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_318.setLineWidth(0)

        self.horizontalLayout_198.addWidget(self.frame_318)

        self.progresbarSubColor2 = ClickableLabel(self.progresbarSub_color2)
        self.progresbarSubColor2.setObjectName(u"progresbarSubColor2")
        self.progresbarSubColor2.setMinimumSize(QSize(0, 24))
        self.progresbarSubColor2.setMaximumSize(QSize(16777215, 24))
        self.progresbarSubColor2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_198.addWidget(self.progresbarSubColor2)


        self.verticalLayout_2.addWidget(self.progresbarSub_color2)

        self.progresbarSub_color2RGBA = QFrame(self.baseWidgets)
        self.progresbarSub_color2RGBA.setObjectName(u"progresbarSub_color2RGBA")
        self.progresbarSub_color2RGBA.setMinimumSize(QSize(0, 24))
        self.progresbarSub_color2RGBA.setMaximumSize(QSize(16777215, 24))
        self.progresbarSub_color2RGBA.setStyleSheet(u"")
        self.horizontalLayout_206 = QHBoxLayout(self.progresbarSub_color2RGBA)
        self.horizontalLayout_206.setSpacing(6)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_206.setContentsMargins(32, 0, 0, 0)
        self.progresbarSubColor2R = ClickableLineEdit(self.progresbarSub_color2RGBA)
        self.progresbarSubColor2R.setObjectName(u"progresbarSubColor2R")
        sizePolicy1.setHeightForWidth(self.progresbarSubColor2R.sizePolicy().hasHeightForWidth())
        self.progresbarSubColor2R.setSizePolicy(sizePolicy1)
        self.progresbarSubColor2R.setMinimumSize(QSize(50, 24))
        self.progresbarSubColor2R.setMaximumSize(QSize(50, 24))
        self.progresbarSubColor2R.setSizeIncrement(QSize(0, 0))
        self.progresbarSubColor2R.setBaseSize(QSize(0, 18))
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
        self.progresbarSubColor2R.setPalette(palette12)
        self.progresbarSubColor2R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progresbarSubColor2R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_206.addWidget(self.progresbarSubColor2R)

        self.progresbarSubColor2G = ClickableLineEdit(self.progresbarSub_color2RGBA)
        self.progresbarSubColor2G.setObjectName(u"progresbarSubColor2G")
        sizePolicy1.setHeightForWidth(self.progresbarSubColor2G.sizePolicy().hasHeightForWidth())
        self.progresbarSubColor2G.setSizePolicy(sizePolicy1)
        self.progresbarSubColor2G.setMinimumSize(QSize(50, 24))
        self.progresbarSubColor2G.setMaximumSize(QSize(50, 24))
        self.progresbarSubColor2G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_206.addWidget(self.progresbarSubColor2G)

        self.progresbarSubColor2B = ClickableLineEdit(self.progresbarSub_color2RGBA)
        self.progresbarSubColor2B.setObjectName(u"progresbarSubColor2B")
        sizePolicy1.setHeightForWidth(self.progresbarSubColor2B.sizePolicy().hasHeightForWidth())
        self.progresbarSubColor2B.setSizePolicy(sizePolicy1)
        self.progresbarSubColor2B.setMinimumSize(QSize(50, 24))
        self.progresbarSubColor2B.setMaximumSize(QSize(50, 24))
        self.progresbarSubColor2B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_206.addWidget(self.progresbarSubColor2B)

        self.progresbarSubColor2A = ClickableLineEdit(self.progresbarSub_color2RGBA)
        self.progresbarSubColor2A.setObjectName(u"progresbarSubColor2A")
        sizePolicy1.setHeightForWidth(self.progresbarSubColor2A.sizePolicy().hasHeightForWidth())
        self.progresbarSubColor2A.setSizePolicy(sizePolicy1)
        self.progresbarSubColor2A.setMinimumSize(QSize(50, 24))
        self.progresbarSubColor2A.setMaximumSize(QSize(50, 24))
        self.progresbarSubColor2A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_206.addWidget(self.progresbarSubColor2A)

        self.frame_336 = QFrame(self.progresbarSub_color2RGBA)
        self.frame_336.setObjectName(u"frame_336")
        sizePolicy2.setHeightForWidth(self.frame_336.sizePolicy().hasHeightForWidth())
        self.frame_336.setSizePolicy(sizePolicy2)
        self.frame_336.setMinimumSize(QSize(0, 24))
        self.frame_336.setMaximumSize(QSize(16777215, 24))
        self.frame_336.setFont(font)
        self.frame_336.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_336.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_206.addWidget(self.frame_336)


        self.verticalLayout_2.addWidget(self.progresbarSub_color2RGBA)

        self.progresbarHandler_label = QFrame(self.baseWidgets)
        self.progresbarHandler_label.setObjectName(u"progresbarHandler_label")
        self.progresbarHandler_label.setMinimumSize(QSize(0, 30))
        self.progresbarHandler_label.setMaximumSize(QSize(16777215, 30))
        self.progresbarHandler_label.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_label.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_216 = QHBoxLayout(self.progresbarHandler_label)
        self.horizontalLayout_216.setSpacing(0)
        self.horizontalLayout_216.setObjectName(u"horizontalLayout_216")
        self.horizontalLayout_216.setContentsMargins(16, 0, 0, 0)
        self.progresbarHandlerLabel = ClickableLabel(self.progresbarHandler_label)
        self.progresbarHandlerLabel.setObjectName(u"progresbarHandlerLabel")
        self.progresbarHandlerLabel.setMinimumSize(QSize(0, 30))
        self.progresbarHandlerLabel.setMaximumSize(QSize(16777215, 30))
        self.progresbarHandlerLabel.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_216.addWidget(self.progresbarHandlerLabel)

        self.frame_356 = QFrame(self.progresbarHandler_label)
        self.frame_356.setObjectName(u"frame_356")
        self.frame_356.setMinimumSize(QSize(0, 30))
        self.frame_356.setMaximumSize(QSize(0, 30))
        self.frame_356.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_356.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_216.addWidget(self.frame_356)


        self.verticalLayout_2.addWidget(self.progresbarHandler_label)

        self.progresbarHandler_size = QFrame(self.baseWidgets)
        self.progresbarHandler_size.setObjectName(u"progresbarHandler_size")
        self.progresbarHandler_size.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_size.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_size.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_size.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_218 = QHBoxLayout(self.progresbarHandler_size)
        self.horizontalLayout_218.setSpacing(0)
        self.horizontalLayout_218.setObjectName(u"horizontalLayout_218")
        self.horizontalLayout_218.setContentsMargins(32, 0, 0, 0)
        self.frame_358 = QFrame(self.progresbarHandler_size)
        self.frame_358.setObjectName(u"frame_358")
        self.frame_358.setMaximumSize(QSize(0, 24))
        self.frame_358.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_358.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_358.setLineWidth(0)

        self.horizontalLayout_218.addWidget(self.frame_358)

        self.progresbarHandlerSize = ClickableLabel(self.progresbarHandler_size)
        self.progresbarHandlerSize.setObjectName(u"progresbarHandlerSize")
        self.progresbarHandlerSize.setMinimumSize(QSize(0, 24))
        self.progresbarHandlerSize.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandlerSize.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_218.addWidget(self.progresbarHandlerSize)


        self.verticalLayout_2.addWidget(self.progresbarHandler_size)

        self.progresbarHandler_sizeXY = QFrame(self.baseWidgets)
        self.progresbarHandler_sizeXY.setObjectName(u"progresbarHandler_sizeXY")
        self.progresbarHandler_sizeXY.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_sizeXY.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_217 = QHBoxLayout(self.progresbarHandler_sizeXY)
        self.horizontalLayout_217.setObjectName(u"horizontalLayout_217")
        self.horizontalLayout_217.setContentsMargins(32, 0, 0, 0)
        self.progresbarHandlerSizeX = ClickableLineEdit(self.progresbarHandler_sizeXY)
        self.progresbarHandlerSizeX.setObjectName(u"progresbarHandlerSizeX")
        self.progresbarHandlerSizeX.setMinimumSize(QSize(70, 24))
        self.progresbarHandlerSizeX.setMaximumSize(QSize(70, 24))
        self.progresbarHandlerSizeX.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_217.addWidget(self.progresbarHandlerSizeX)

        self.progresbarHandlerSizeY = ClickableLineEdit(self.progresbarHandler_sizeXY)
        self.progresbarHandlerSizeY.setObjectName(u"progresbarHandlerSizeY")
        self.progresbarHandlerSizeY.setMinimumSize(QSize(70, 24))
        self.progresbarHandlerSizeY.setMaximumSize(QSize(70, 24))
        self.progresbarHandlerSizeY.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_217.addWidget(self.progresbarHandlerSizeY)

        self.frame_338 = QFrame(self.progresbarHandler_sizeXY)
        self.frame_338.setObjectName(u"frame_338")
        self.frame_338.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_338.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_217.addWidget(self.frame_338)


        self.verticalLayout_2.addWidget(self.progresbarHandler_sizeXY)

        self.progresbarHandler_radius = QFrame(self.baseWidgets)
        self.progresbarHandler_radius.setObjectName(u"progresbarHandler_radius")
        self.progresbarHandler_radius.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_radius.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_radius.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_radius.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_219 = QHBoxLayout(self.progresbarHandler_radius)
        self.horizontalLayout_219.setSpacing(0)
        self.horizontalLayout_219.setObjectName(u"horizontalLayout_219")
        self.horizontalLayout_219.setContentsMargins(32, 0, 0, 0)
        self.frame_360 = QFrame(self.progresbarHandler_radius)
        self.frame_360.setObjectName(u"frame_360")
        self.frame_360.setMaximumSize(QSize(0, 24))
        self.frame_360.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_360.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_360.setLineWidth(0)

        self.horizontalLayout_219.addWidget(self.frame_360)

        self.progresbarHandlerRadius = ClickableLabel(self.progresbarHandler_radius)
        self.progresbarHandlerRadius.setObjectName(u"progresbarHandlerRadius")
        self.progresbarHandlerRadius.setMinimumSize(QSize(0, 24))
        self.progresbarHandlerRadius.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandlerRadius.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_219.addWidget(self.progresbarHandlerRadius)


        self.verticalLayout_2.addWidget(self.progresbarHandler_radius)

        self.progresbarHandler_radiusPx = QFrame(self.baseWidgets)
        self.progresbarHandler_radiusPx.setObjectName(u"progresbarHandler_radiusPx")
        self.progresbarHandler_radiusPx.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_radiusPx.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_radiusPx.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_radiusPx.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_244 = QHBoxLayout(self.progresbarHandler_radiusPx)
        self.horizontalLayout_244.setSpacing(0)
        self.horizontalLayout_244.setObjectName(u"horizontalLayout_244")
        self.horizontalLayout_244.setContentsMargins(32, 0, 0, -1)
        self.frame_400 = QFrame(self.progresbarHandler_radiusPx)
        self.frame_400.setObjectName(u"frame_400")
        self.frame_400.setMinimumSize(QSize(0, 24))
        self.frame_400.setMaximumSize(QSize(0, 24))
        self.frame_400.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_400.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_244.addWidget(self.frame_400)

        self.progresbarHandlerRadiusPx = ClickableLineEdit(self.progresbarHandler_radiusPx)
        self.progresbarHandlerRadiusPx.setObjectName(u"progresbarHandlerRadiusPx")
        self.progresbarHandlerRadiusPx.setMinimumSize(QSize(80, 24))
        self.progresbarHandlerRadiusPx.setMaximumSize(QSize(80, 24))
        self.progresbarHandlerRadiusPx.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_244.addWidget(self.progresbarHandlerRadiusPx)

        self.frame_401 = QFrame(self.progresbarHandler_radiusPx)
        self.frame_401.setObjectName(u"frame_401")
        self.frame_401.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_401.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_244.addWidget(self.frame_401)


        self.verticalLayout_2.addWidget(self.progresbarHandler_radiusPx)

        self.progresbarHandler_color = QFrame(self.baseWidgets)
        self.progresbarHandler_color.setObjectName(u"progresbarHandler_color")
        self.progresbarHandler_color.setMinimumSize(QSize(0, 30))
        self.progresbarHandler_color.setMaximumSize(QSize(16777215, 30))
        self.progresbarHandler_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_color.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_234 = QHBoxLayout(self.progresbarHandler_color)
        self.horizontalLayout_234.setSpacing(0)
        self.horizontalLayout_234.setObjectName(u"horizontalLayout_234")
        self.horizontalLayout_234.setContentsMargins(32, 0, 0, 0)
        self.progresbarHandlerColor = ClickableLabel(self.progresbarHandler_color)
        self.progresbarHandlerColor.setObjectName(u"progresbarHandlerColor")
        self.progresbarHandlerColor.setMinimumSize(QSize(0, 30))
        self.progresbarHandlerColor.setMaximumSize(QSize(16777215, 30))
        self.progresbarHandlerColor.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_234.addWidget(self.progresbarHandlerColor)

        self.frame_373 = QFrame(self.progresbarHandler_color)
        self.frame_373.setObjectName(u"frame_373")
        self.frame_373.setMinimumSize(QSize(0, 30))
        self.frame_373.setMaximumSize(QSize(0, 30))
        self.frame_373.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_373.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_234.addWidget(self.frame_373)


        self.verticalLayout_2.addWidget(self.progresbarHandler_color)

        self.progresbarHandler_color1 = QFrame(self.baseWidgets)
        self.progresbarHandler_color1.setObjectName(u"progresbarHandler_color1")
        self.progresbarHandler_color1.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_color1.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_color1.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_color1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_236 = QHBoxLayout(self.progresbarHandler_color1)
        self.horizontalLayout_236.setSpacing(0)
        self.horizontalLayout_236.setObjectName(u"horizontalLayout_236")
        self.horizontalLayout_236.setContentsMargins(48, 0, 0, 0)
        self.frame_380 = QFrame(self.progresbarHandler_color1)
        self.frame_380.setObjectName(u"frame_380")
        self.frame_380.setMaximumSize(QSize(0, 24))
        self.frame_380.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_380.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_380.setLineWidth(0)

        self.horizontalLayout_236.addWidget(self.frame_380)

        self.progresbarHandlerColor1 = ClickableLabel(self.progresbarHandler_color1)
        self.progresbarHandlerColor1.setObjectName(u"progresbarHandlerColor1")
        self.progresbarHandlerColor1.setMinimumSize(QSize(0, 24))
        self.progresbarHandlerColor1.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandlerColor1.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_236.addWidget(self.progresbarHandlerColor1)


        self.verticalLayout_2.addWidget(self.progresbarHandler_color1)

        self.progresbarSub_color1RGBA = QFrame(self.baseWidgets)
        self.progresbarSub_color1RGBA.setObjectName(u"progresbarSub_color1RGBA")
        self.progresbarSub_color1RGBA.setMinimumSize(QSize(0, 24))
        self.progresbarSub_color1RGBA.setMaximumSize(QSize(16777215, 24))
        self.progresbarSub_color1RGBA.setStyleSheet(u"")
        self.horizontalLayout_232 = QHBoxLayout(self.progresbarSub_color1RGBA)
        self.horizontalLayout_232.setSpacing(6)
        self.horizontalLayout_232.setObjectName(u"horizontalLayout_232")
        self.horizontalLayout_232.setContentsMargins(48, 0, 0, 0)
        self.progresbarHandlerColor1R = ClickableLineEdit(self.progresbarSub_color1RGBA)
        self.progresbarHandlerColor1R.setObjectName(u"progresbarHandlerColor1R")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerColor1R.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerColor1R.setSizePolicy(sizePolicy1)
        self.progresbarHandlerColor1R.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerColor1R.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerColor1R.setSizeIncrement(QSize(0, 0))
        self.progresbarHandlerColor1R.setBaseSize(QSize(0, 18))
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
        self.progresbarHandlerColor1R.setPalette(palette13)
        self.progresbarHandlerColor1R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progresbarHandlerColor1R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_232.addWidget(self.progresbarHandlerColor1R)

        self.progresbarHandlerColor1G = ClickableLineEdit(self.progresbarSub_color1RGBA)
        self.progresbarHandlerColor1G.setObjectName(u"progresbarHandlerColor1G")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerColor1G.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerColor1G.setSizePolicy(sizePolicy1)
        self.progresbarHandlerColor1G.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerColor1G.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerColor1G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_232.addWidget(self.progresbarHandlerColor1G)

        self.progresbarHandlerColor1B = ClickableLineEdit(self.progresbarSub_color1RGBA)
        self.progresbarHandlerColor1B.setObjectName(u"progresbarHandlerColor1B")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerColor1B.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerColor1B.setSizePolicy(sizePolicy1)
        self.progresbarHandlerColor1B.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerColor1B.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerColor1B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_232.addWidget(self.progresbarHandlerColor1B)

        self.progresbarHandlerColor1A = ClickableLineEdit(self.progresbarSub_color1RGBA)
        self.progresbarHandlerColor1A.setObjectName(u"progresbarHandlerColor1A")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerColor1A.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerColor1A.setSizePolicy(sizePolicy1)
        self.progresbarHandlerColor1A.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerColor1A.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerColor1A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_232.addWidget(self.progresbarHandlerColor1A)

        self.frame_366 = QFrame(self.progresbarSub_color1RGBA)
        self.frame_366.setObjectName(u"frame_366")
        sizePolicy2.setHeightForWidth(self.frame_366.sizePolicy().hasHeightForWidth())
        self.frame_366.setSizePolicy(sizePolicy2)
        self.frame_366.setMinimumSize(QSize(0, 24))
        self.frame_366.setMaximumSize(QSize(16777215, 24))
        self.frame_366.setFont(font)
        self.frame_366.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_366.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_232.addWidget(self.frame_366)


        self.verticalLayout_2.addWidget(self.progresbarSub_color1RGBA)

        self.fixedColor_progresbarHandler = QFrame(self.baseWidgets)
        self.fixedColor_progresbarHandler.setObjectName(u"fixedColor_progresbarHandler")
        self.fixedColor_progresbarHandler.setMinimumSize(QSize(0, 20))
        self.fixedColor_progresbarHandler.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_235 = QHBoxLayout(self.fixedColor_progresbarHandler)
        self.horizontalLayout_235.setSpacing(5)
        self.horizontalLayout_235.setObjectName(u"horizontalLayout_235")
        self.horizontalLayout_235.setContentsMargins(48, 0, 0, 0)
        self.fixedColorProgresbarHandler = ClickableLabel(self.fixedColor_progresbarHandler)
        self.fixedColorProgresbarHandler.setObjectName(u"fixedColorProgresbarHandler")
        self.fixedColorProgresbarHandler.setMinimumSize(QSize(195, 0))
        self.fixedColorProgresbarHandler.setMaximumSize(QSize(195, 24))
        self.fixedColorProgresbarHandler.setStyleSheet(u"")

        self.horizontalLayout_235.addWidget(self.fixedColorProgresbarHandler)

        self.fixedColorProgresbarHandlerCheckBox = QCheckBox(self.fixedColor_progresbarHandler)
        self.fixedColorProgresbarHandlerCheckBox.setObjectName(u"fixedColorProgresbarHandlerCheckBox")
        self.fixedColorProgresbarHandlerCheckBox.setMaximumSize(QSize(16777215, 24))
        self.fixedColorProgresbarHandlerCheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.fixedColorProgresbarHandlerCheckBox.setIconSize(QSize(18, 18))
        self.fixedColorProgresbarHandlerCheckBox.setChecked(False)
        self.fixedColorProgresbarHandlerCheckBox.setTristate(False)

        self.horizontalLayout_235.addWidget(self.fixedColorProgresbarHandlerCheckBox)


        self.verticalLayout_2.addWidget(self.fixedColor_progresbarHandler)

        self.progresbarHandler_threshold = QFrame(self.baseWidgets)
        self.progresbarHandler_threshold.setObjectName(u"progresbarHandler_threshold")
        self.progresbarHandler_threshold.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_threshold.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_threshold.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_threshold.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_233 = QHBoxLayout(self.progresbarHandler_threshold)
        self.horizontalLayout_233.setSpacing(0)
        self.horizontalLayout_233.setObjectName(u"horizontalLayout_233")
        self.horizontalLayout_233.setContentsMargins(48, 0, 0, 0)
        self.frame_370 = QFrame(self.progresbarHandler_threshold)
        self.frame_370.setObjectName(u"frame_370")
        self.frame_370.setMaximumSize(QSize(0, 24))
        self.frame_370.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_370.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_370.setLineWidth(0)

        self.horizontalLayout_233.addWidget(self.frame_370)

        self.progresbarHandlerThreshold = ClickableLabel(self.progresbarHandler_threshold)
        self.progresbarHandlerThreshold.setObjectName(u"progresbarHandlerThreshold")
        self.progresbarHandlerThreshold.setMinimumSize(QSize(0, 24))
        self.progresbarHandlerThreshold.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandlerThreshold.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_233.addWidget(self.progresbarHandlerThreshold)


        self.verticalLayout_2.addWidget(self.progresbarHandler_threshold)

        self.progresbarHandler_thresholdRGB = QFrame(self.baseWidgets)
        self.progresbarHandler_thresholdRGB.setObjectName(u"progresbarHandler_thresholdRGB")
        self.progresbarHandler_thresholdRGB.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_thresholdRGB.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_thresholdRGB.setStyleSheet(u"")
        self.horizontalLayout_240 = QHBoxLayout(self.progresbarHandler_thresholdRGB)
        self.horizontalLayout_240.setSpacing(6)
        self.horizontalLayout_240.setObjectName(u"horizontalLayout_240")
        self.horizontalLayout_240.setContentsMargins(48, 0, 0, 0)
        self.progresbarHandlerThresholdR = ClickableLineEdit(self.progresbarHandler_thresholdRGB)
        self.progresbarHandlerThresholdR.setObjectName(u"progresbarHandlerThresholdR")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerThresholdR.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerThresholdR.setSizePolicy(sizePolicy1)
        self.progresbarHandlerThresholdR.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerThresholdR.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerThresholdR.setSizeIncrement(QSize(0, 0))
        self.progresbarHandlerThresholdR.setBaseSize(QSize(0, 18))
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
        self.progresbarHandlerThresholdR.setPalette(palette14)
        self.progresbarHandlerThresholdR.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progresbarHandlerThresholdR.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_240.addWidget(self.progresbarHandlerThresholdR)

        self.progresbarHandlerThresholdG = ClickableLineEdit(self.progresbarHandler_thresholdRGB)
        self.progresbarHandlerThresholdG.setObjectName(u"progresbarHandlerThresholdG")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerThresholdG.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerThresholdG.setSizePolicy(sizePolicy1)
        self.progresbarHandlerThresholdG.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerThresholdG.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerThresholdG.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_240.addWidget(self.progresbarHandlerThresholdG)

        self.progresbarHandlerThresholdB = ClickableLineEdit(self.progresbarHandler_thresholdRGB)
        self.progresbarHandlerThresholdB.setObjectName(u"progresbarHandlerThresholdB")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerThresholdB.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerThresholdB.setSizePolicy(sizePolicy1)
        self.progresbarHandlerThresholdB.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerThresholdB.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerThresholdB.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_240.addWidget(self.progresbarHandlerThresholdB)

        self.frame_392 = QFrame(self.progresbarHandler_thresholdRGB)
        self.frame_392.setObjectName(u"frame_392")
        sizePolicy2.setHeightForWidth(self.frame_392.sizePolicy().hasHeightForWidth())
        self.frame_392.setSizePolicy(sizePolicy2)
        self.frame_392.setMinimumSize(QSize(0, 24))
        self.frame_392.setMaximumSize(QSize(16777215, 24))
        self.frame_392.setFont(font)
        self.frame_392.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_392.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_240.addWidget(self.frame_392)


        self.verticalLayout_2.addWidget(self.progresbarHandler_thresholdRGB)

        self.progresbarHandler_thresholdMode = QFrame(self.baseWidgets)
        self.progresbarHandler_thresholdMode.setObjectName(u"progresbarHandler_thresholdMode")
        self.progresbarHandler_thresholdMode.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_thresholdMode.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_thresholdMode.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_thresholdMode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_239 = QHBoxLayout(self.progresbarHandler_thresholdMode)
        self.horizontalLayout_239.setSpacing(0)
        self.horizontalLayout_239.setObjectName(u"horizontalLayout_239")
        self.horizontalLayout_239.setContentsMargins(48, 0, 0, 0)
        self.frame_390 = QFrame(self.progresbarHandler_thresholdMode)
        self.frame_390.setObjectName(u"frame_390")
        self.frame_390.setMaximumSize(QSize(0, 24))
        self.frame_390.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_390.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_390.setLineWidth(0)

        self.horizontalLayout_239.addWidget(self.frame_390)

        self.progresbarHandlerThresholdMode = ClickableLabel(self.progresbarHandler_thresholdMode)
        self.progresbarHandlerThresholdMode.setObjectName(u"progresbarHandlerThresholdMode")
        self.progresbarHandlerThresholdMode.setMinimumSize(QSize(0, 24))
        self.progresbarHandlerThresholdMode.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandlerThresholdMode.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_239.addWidget(self.progresbarHandlerThresholdMode)


        self.verticalLayout_2.addWidget(self.progresbarHandler_thresholdMode)

        self.progresbarHandler_thresholdModeComboBox = QFrame(self.baseWidgets)
        self.progresbarHandler_thresholdModeComboBox.setObjectName(u"progresbarHandler_thresholdModeComboBox")
        self.progresbarHandler_thresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_thresholdModeComboBox.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_thresholdModeComboBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_thresholdModeComboBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_237 = QHBoxLayout(self.progresbarHandler_thresholdModeComboBox)
        self.horizontalLayout_237.setSpacing(0)
        self.horizontalLayout_237.setObjectName(u"horizontalLayout_237")
        self.horizontalLayout_237.setContentsMargins(48, 0, 0, 0)
        self.frame_384 = QFrame(self.progresbarHandler_thresholdModeComboBox)
        self.frame_384.setObjectName(u"frame_384")
        self.frame_384.setMinimumSize(QSize(0, 24))
        self.frame_384.setMaximumSize(QSize(0, 24))
        self.frame_384.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_384.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_237.addWidget(self.frame_384)

        self.progresbarHandlerThresholdModeComboBox = QComboBox(self.progresbarHandler_thresholdModeComboBox)
        self.progresbarHandlerThresholdModeComboBox.addItem("")
        self.progresbarHandlerThresholdModeComboBox.addItem("")
        self.progresbarHandlerThresholdModeComboBox.addItem("")
        self.progresbarHandlerThresholdModeComboBox.addItem("")
        self.progresbarHandlerThresholdModeComboBox.addItem("")
        self.progresbarHandlerThresholdModeComboBox.setObjectName(u"progresbarHandlerThresholdModeComboBox")
        self.progresbarHandlerThresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.progresbarHandlerThresholdModeComboBox.setMaximumSize(QSize(80, 24))
        self.progresbarHandlerThresholdModeComboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_237.addWidget(self.progresbarHandlerThresholdModeComboBox)

        self.frame_386 = QFrame(self.progresbarHandler_thresholdModeComboBox)
        self.frame_386.setObjectName(u"frame_386")
        self.frame_386.setMinimumSize(QSize(0, 24))
        self.frame_386.setMaximumSize(QSize(16777215, 24))
        self.frame_386.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_386.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_237.addWidget(self.frame_386)


        self.verticalLayout_2.addWidget(self.progresbarHandler_thresholdModeComboBox)

        self.progresbarHandler_color2 = QFrame(self.baseWidgets)
        self.progresbarHandler_color2.setObjectName(u"progresbarHandler_color2")
        self.progresbarHandler_color2.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_color2.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_color2.setFrameShape(QFrame.Shape.StyledPanel)
        self.progresbarHandler_color2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_238 = QHBoxLayout(self.progresbarHandler_color2)
        self.horizontalLayout_238.setSpacing(0)
        self.horizontalLayout_238.setObjectName(u"horizontalLayout_238")
        self.horizontalLayout_238.setContentsMargins(48, 0, 0, 0)
        self.frame_388 = QFrame(self.progresbarHandler_color2)
        self.frame_388.setObjectName(u"frame_388")
        self.frame_388.setMaximumSize(QSize(0, 24))
        self.frame_388.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_388.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_388.setLineWidth(0)

        self.horizontalLayout_238.addWidget(self.frame_388)

        self.progresbarHandlerColor2 = ClickableLabel(self.progresbarHandler_color2)
        self.progresbarHandlerColor2.setObjectName(u"progresbarHandlerColor2")
        self.progresbarHandlerColor2.setMinimumSize(QSize(0, 24))
        self.progresbarHandlerColor2.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandlerColor2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_238.addWidget(self.progresbarHandlerColor2)


        self.verticalLayout_2.addWidget(self.progresbarHandler_color2)

        self.progresbarHandler_color2RGBA = QFrame(self.baseWidgets)
        self.progresbarHandler_color2RGBA.setObjectName(u"progresbarHandler_color2RGBA")
        self.progresbarHandler_color2RGBA.setMinimumSize(QSize(0, 24))
        self.progresbarHandler_color2RGBA.setMaximumSize(QSize(16777215, 24))
        self.progresbarHandler_color2RGBA.setStyleSheet(u"")
        self.horizontalLayout_241 = QHBoxLayout(self.progresbarHandler_color2RGBA)
        self.horizontalLayout_241.setSpacing(6)
        self.horizontalLayout_241.setObjectName(u"horizontalLayout_241")
        self.horizontalLayout_241.setContentsMargins(48, 0, 0, 0)
        self.progresbarHandlerColor2R = ClickableLineEdit(self.progresbarHandler_color2RGBA)
        self.progresbarHandlerColor2R.setObjectName(u"progresbarHandlerColor2R")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerColor2R.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerColor2R.setSizePolicy(sizePolicy1)
        self.progresbarHandlerColor2R.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerColor2R.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerColor2R.setSizeIncrement(QSize(0, 0))
        self.progresbarHandlerColor2R.setBaseSize(QSize(0, 18))
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
        self.progresbarHandlerColor2R.setPalette(palette15)
        self.progresbarHandlerColor2R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progresbarHandlerColor2R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_241.addWidget(self.progresbarHandlerColor2R)

        self.progresbarHandlerColor2G = ClickableLineEdit(self.progresbarHandler_color2RGBA)
        self.progresbarHandlerColor2G.setObjectName(u"progresbarHandlerColor2G")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerColor2G.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerColor2G.setSizePolicy(sizePolicy1)
        self.progresbarHandlerColor2G.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerColor2G.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerColor2G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_241.addWidget(self.progresbarHandlerColor2G)

        self.progresbarHandlerColor2B = ClickableLineEdit(self.progresbarHandler_color2RGBA)
        self.progresbarHandlerColor2B.setObjectName(u"progresbarHandlerColor2B")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerColor2B.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerColor2B.setSizePolicy(sizePolicy1)
        self.progresbarHandlerColor2B.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerColor2B.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerColor2B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_241.addWidget(self.progresbarHandlerColor2B)

        self.progresbarHandlerColor2A = ClickableLineEdit(self.progresbarHandler_color2RGBA)
        self.progresbarHandlerColor2A.setObjectName(u"progresbarHandlerColor2A")
        sizePolicy1.setHeightForWidth(self.progresbarHandlerColor2A.sizePolicy().hasHeightForWidth())
        self.progresbarHandlerColor2A.setSizePolicy(sizePolicy1)
        self.progresbarHandlerColor2A.setMinimumSize(QSize(50, 24))
        self.progresbarHandlerColor2A.setMaximumSize(QSize(50, 24))
        self.progresbarHandlerColor2A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_241.addWidget(self.progresbarHandlerColor2A)

        self.frame_394 = QFrame(self.progresbarHandler_color2RGBA)
        self.frame_394.setObjectName(u"frame_394")
        sizePolicy2.setHeightForWidth(self.frame_394.sizePolicy().hasHeightForWidth())
        self.frame_394.setSizePolicy(sizePolicy2)
        self.frame_394.setMinimumSize(QSize(0, 24))
        self.frame_394.setMaximumSize(QSize(16777215, 24))
        self.frame_394.setFont(font)
        self.frame_394.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_394.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_241.addWidget(self.frame_394)


        self.verticalLayout_2.addWidget(self.progresbarHandler_color2RGBA)

        self.progress = ClickableLabel(self.baseWidgets)
        self.progress.setObjectName(u"progress")
        self.progress.setMinimumSize(QSize(0, 40))
        self.progress.setMaximumSize(QSize(16777215, 40))
        self.progress.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.progress)

        self.progress_sze = QFrame(self.baseWidgets)
        self.progress_sze.setObjectName(u"progress_sze")
        self.progress_sze.setMinimumSize(QSize(0, 24))
        self.progress_sze.setMaximumSize(QSize(16777215, 24))
        self.progress_sze.setFrameShape(QFrame.Shape.StyledPanel)
        self.progress_sze.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_243 = QHBoxLayout(self.progress_sze)
        self.horizontalLayout_243.setSpacing(0)
        self.horizontalLayout_243.setObjectName(u"horizontalLayout_243")
        self.horizontalLayout_243.setContentsMargins(32, 0, 0, 0)
        self.frame_398 = QFrame(self.progress_sze)
        self.frame_398.setObjectName(u"frame_398")
        self.frame_398.setMaximumSize(QSize(0, 24))
        self.frame_398.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_398.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_398.setLineWidth(0)

        self.horizontalLayout_243.addWidget(self.frame_398)

        self.progressSze = ClickableLabel(self.progress_sze)
        self.progressSze.setObjectName(u"progressSze")
        self.progressSze.setMinimumSize(QSize(0, 24))
        self.progressSze.setMaximumSize(QSize(16777215, 24))
        self.progressSze.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_243.addWidget(self.progressSze)


        self.verticalLayout_2.addWidget(self.progress_sze)

        self.progress_sizePx = QFrame(self.baseWidgets)
        self.progress_sizePx.setObjectName(u"progress_sizePx")
        self.progress_sizePx.setMinimumSize(QSize(0, 24))
        self.progress_sizePx.setMaximumSize(QSize(16777215, 24))
        self.progress_sizePx.setFrameShape(QFrame.Shape.StyledPanel)
        self.progress_sizePx.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_220 = QHBoxLayout(self.progress_sizePx)
        self.horizontalLayout_220.setSpacing(0)
        self.horizontalLayout_220.setObjectName(u"horizontalLayout_220")
        self.horizontalLayout_220.setContentsMargins(32, 0, 0, -1)
        self.frame_362 = QFrame(self.progress_sizePx)
        self.frame_362.setObjectName(u"frame_362")
        self.frame_362.setMinimumSize(QSize(0, 24))
        self.frame_362.setMaximumSize(QSize(0, 24))
        self.frame_362.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_362.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_220.addWidget(self.frame_362)

        self.progressSizePx = ClickableLineEdit(self.progress_sizePx)
        self.progressSizePx.setObjectName(u"progressSizePx")
        self.progressSizePx.setMinimumSize(QSize(80, 24))
        self.progressSizePx.setMaximumSize(QSize(80, 24))
        self.progressSizePx.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_220.addWidget(self.progressSizePx)

        self.frame_363 = QFrame(self.progress_sizePx)
        self.frame_363.setObjectName(u"frame_363")
        self.frame_363.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_363.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_220.addWidget(self.frame_363)


        self.verticalLayout_2.addWidget(self.progress_sizePx)

        self.progress_position = QFrame(self.baseWidgets)
        self.progress_position.setObjectName(u"progress_position")
        self.progress_position.setMinimumSize(QSize(0, 24))
        self.progress_position.setMaximumSize(QSize(16777215, 24))
        self.progress_position.setFrameShape(QFrame.Shape.StyledPanel)
        self.progress_position.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_245 = QHBoxLayout(self.progress_position)
        self.horizontalLayout_245.setSpacing(0)
        self.horizontalLayout_245.setObjectName(u"horizontalLayout_245")
        self.horizontalLayout_245.setContentsMargins(32, 0, 0, 0)
        self.frame_403 = QFrame(self.progress_position)
        self.frame_403.setObjectName(u"frame_403")
        self.frame_403.setMaximumSize(QSize(0, 24))
        self.frame_403.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_403.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_403.setLineWidth(0)

        self.horizontalLayout_245.addWidget(self.frame_403)

        self.progressPosition = ClickableLabel(self.progress_position)
        self.progressPosition.setObjectName(u"progressPosition")
        self.progressPosition.setMinimumSize(QSize(0, 24))
        self.progressPosition.setMaximumSize(QSize(16777215, 24))
        self.progressPosition.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_245.addWidget(self.progressPosition)


        self.verticalLayout_2.addWidget(self.progress_position)

        self.progress_positionXY = QFrame(self.baseWidgets)
        self.progress_positionXY.setObjectName(u"progress_positionXY")
        self.progress_positionXY.setMinimumSize(QSize(0, 24))
        self.progress_positionXY.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_242 = QHBoxLayout(self.progress_positionXY)
        self.horizontalLayout_242.setObjectName(u"horizontalLayout_242")
        self.horizontalLayout_242.setContentsMargins(32, 0, 0, 0)
        self.progressPositionX = ClickableLineEdit(self.progress_positionXY)
        self.progressPositionX.setObjectName(u"progressPositionX")
        self.progressPositionX.setMinimumSize(QSize(70, 24))
        self.progressPositionX.setMaximumSize(QSize(70, 24))
        self.progressPositionX.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_242.addWidget(self.progressPositionX)

        self.progressPositionY = ClickableLineEdit(self.progress_positionXY)
        self.progressPositionY.setObjectName(u"progressPositionY")
        self.progressPositionY.setMinimumSize(QSize(70, 24))
        self.progressPositionY.setMaximumSize(QSize(70, 24))
        self.progressPositionY.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_242.addWidget(self.progressPositionY)

        self.frame_396 = QFrame(self.progress_positionXY)
        self.frame_396.setObjectName(u"frame_396")
        self.frame_396.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_396.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_242.addWidget(self.frame_396)


        self.verticalLayout_2.addWidget(self.progress_positionXY)

        self.progress_color = QFrame(self.baseWidgets)
        self.progress_color.setObjectName(u"progress_color")
        self.progress_color.setMinimumSize(QSize(0, 30))
        self.progress_color.setMaximumSize(QSize(16777215, 30))
        self.progress_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.progress_color.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_248 = QHBoxLayout(self.progress_color)
        self.horizontalLayout_248.setSpacing(0)
        self.horizontalLayout_248.setObjectName(u"horizontalLayout_248")
        self.horizontalLayout_248.setContentsMargins(16, 0, 0, 0)
        self.progressColor = ClickableLabel(self.progress_color)
        self.progressColor.setObjectName(u"progressColor")
        self.progressColor.setMinimumSize(QSize(0, 30))
        self.progressColor.setMaximumSize(QSize(16777215, 30))
        self.progressColor.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_248.addWidget(self.progressColor)

        self.frame_409 = QFrame(self.progress_color)
        self.frame_409.setObjectName(u"frame_409")
        self.frame_409.setMinimumSize(QSize(0, 30))
        self.frame_409.setMaximumSize(QSize(0, 30))
        self.frame_409.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_409.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_248.addWidget(self.frame_409)


        self.verticalLayout_2.addWidget(self.progress_color)

        self.progress_color1 = QFrame(self.baseWidgets)
        self.progress_color1.setObjectName(u"progress_color1")
        self.progress_color1.setMinimumSize(QSize(0, 24))
        self.progress_color1.setMaximumSize(QSize(16777215, 24))
        self.progress_color1.setFrameShape(QFrame.Shape.StyledPanel)
        self.progress_color1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_250 = QHBoxLayout(self.progress_color1)
        self.horizontalLayout_250.setSpacing(0)
        self.horizontalLayout_250.setObjectName(u"horizontalLayout_250")
        self.horizontalLayout_250.setContentsMargins(32, 0, 0, 0)
        self.frame_412 = QFrame(self.progress_color1)
        self.frame_412.setObjectName(u"frame_412")
        self.frame_412.setMaximumSize(QSize(0, 24))
        self.frame_412.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_412.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_412.setLineWidth(0)

        self.horizontalLayout_250.addWidget(self.frame_412)

        self.progressColor1 = ClickableLabel(self.progress_color1)
        self.progressColor1.setObjectName(u"progressColor1")
        self.progressColor1.setMinimumSize(QSize(0, 24))
        self.progressColor1.setMaximumSize(QSize(16777215, 24))
        self.progressColor1.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_250.addWidget(self.progressColor1)


        self.verticalLayout_2.addWidget(self.progress_color1)

        self.progress_color1RGBA = QFrame(self.baseWidgets)
        self.progress_color1RGBA.setObjectName(u"progress_color1RGBA")
        self.progress_color1RGBA.setMinimumSize(QSize(0, 24))
        self.progress_color1RGBA.setMaximumSize(QSize(16777215, 24))
        self.progress_color1RGBA.setStyleSheet(u"")
        self.horizontalLayout_246 = QHBoxLayout(self.progress_color1RGBA)
        self.horizontalLayout_246.setSpacing(6)
        self.horizontalLayout_246.setObjectName(u"horizontalLayout_246")
        self.horizontalLayout_246.setContentsMargins(32, 0, 0, 0)
        self.progressColor1R = ClickableLineEdit(self.progress_color1RGBA)
        self.progressColor1R.setObjectName(u"progressColor1R")
        sizePolicy1.setHeightForWidth(self.progressColor1R.sizePolicy().hasHeightForWidth())
        self.progressColor1R.setSizePolicy(sizePolicy1)
        self.progressColor1R.setMinimumSize(QSize(50, 24))
        self.progressColor1R.setMaximumSize(QSize(50, 24))
        self.progressColor1R.setSizeIncrement(QSize(0, 0))
        self.progressColor1R.setBaseSize(QSize(0, 18))
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
        self.progressColor1R.setPalette(palette16)
        self.progressColor1R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressColor1R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_246.addWidget(self.progressColor1R)

        self.progressColor1G = ClickableLineEdit(self.progress_color1RGBA)
        self.progressColor1G.setObjectName(u"progressColor1G")
        sizePolicy1.setHeightForWidth(self.progressColor1G.sizePolicy().hasHeightForWidth())
        self.progressColor1G.setSizePolicy(sizePolicy1)
        self.progressColor1G.setMinimumSize(QSize(50, 24))
        self.progressColor1G.setMaximumSize(QSize(50, 24))
        self.progressColor1G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_246.addWidget(self.progressColor1G)

        self.progressColor1B = ClickableLineEdit(self.progress_color1RGBA)
        self.progressColor1B.setObjectName(u"progressColor1B")
        sizePolicy1.setHeightForWidth(self.progressColor1B.sizePolicy().hasHeightForWidth())
        self.progressColor1B.setSizePolicy(sizePolicy1)
        self.progressColor1B.setMinimumSize(QSize(50, 24))
        self.progressColor1B.setMaximumSize(QSize(50, 24))
        self.progressColor1B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_246.addWidget(self.progressColor1B)

        self.progressColor1A = ClickableLineEdit(self.progress_color1RGBA)
        self.progressColor1A.setObjectName(u"progressColor1A")
        sizePolicy1.setHeightForWidth(self.progressColor1A.sizePolicy().hasHeightForWidth())
        self.progressColor1A.setSizePolicy(sizePolicy1)
        self.progressColor1A.setMinimumSize(QSize(50, 24))
        self.progressColor1A.setMaximumSize(QSize(50, 24))
        self.progressColor1A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_246.addWidget(self.progressColor1A)

        self.frame_405 = QFrame(self.progress_color1RGBA)
        self.frame_405.setObjectName(u"frame_405")
        sizePolicy2.setHeightForWidth(self.frame_405.sizePolicy().hasHeightForWidth())
        self.frame_405.setSizePolicy(sizePolicy2)
        self.frame_405.setMinimumSize(QSize(0, 24))
        self.frame_405.setMaximumSize(QSize(16777215, 24))
        self.frame_405.setFont(font)
        self.frame_405.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_405.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_246.addWidget(self.frame_405)


        self.verticalLayout_2.addWidget(self.progress_color1RGBA)

        self.fixedColor_progress = QFrame(self.baseWidgets)
        self.fixedColor_progress.setObjectName(u"fixedColor_progress")
        self.fixedColor_progress.setMinimumSize(QSize(0, 20))
        self.fixedColor_progress.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_249 = QHBoxLayout(self.fixedColor_progress)
        self.horizontalLayout_249.setSpacing(5)
        self.horizontalLayout_249.setObjectName(u"horizontalLayout_249")
        self.horizontalLayout_249.setContentsMargins(32, 0, 0, 0)
        self.fixedColorProgress = ClickableLabel(self.fixedColor_progress)
        self.fixedColorProgress.setObjectName(u"fixedColorProgress")
        self.fixedColorProgress.setMinimumSize(QSize(195, 0))
        self.fixedColorProgress.setMaximumSize(QSize(195, 24))
        self.fixedColorProgress.setStyleSheet(u"")

        self.horizontalLayout_249.addWidget(self.fixedColorProgress)

        self.fixedColorProgressCheckBox = QCheckBox(self.fixedColor_progress)
        self.fixedColorProgressCheckBox.setObjectName(u"fixedColorProgressCheckBox")
        self.fixedColorProgressCheckBox.setMaximumSize(QSize(16777215, 24))
        self.fixedColorProgressCheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.fixedColorProgressCheckBox.setIconSize(QSize(18, 18))
        self.fixedColorProgressCheckBox.setChecked(False)
        self.fixedColorProgressCheckBox.setTristate(False)

        self.horizontalLayout_249.addWidget(self.fixedColorProgressCheckBox)


        self.verticalLayout_2.addWidget(self.fixedColor_progress)

        self.progress_threshold = QFrame(self.baseWidgets)
        self.progress_threshold.setObjectName(u"progress_threshold")
        self.progress_threshold.setMinimumSize(QSize(0, 24))
        self.progress_threshold.setMaximumSize(QSize(16777215, 24))
        self.progress_threshold.setFrameShape(QFrame.Shape.StyledPanel)
        self.progress_threshold.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_247 = QHBoxLayout(self.progress_threshold)
        self.horizontalLayout_247.setSpacing(0)
        self.horizontalLayout_247.setObjectName(u"horizontalLayout_247")
        self.horizontalLayout_247.setContentsMargins(32, 0, 0, 0)
        self.frame_407 = QFrame(self.progress_threshold)
        self.frame_407.setObjectName(u"frame_407")
        self.frame_407.setMaximumSize(QSize(0, 24))
        self.frame_407.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_407.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_407.setLineWidth(0)

        self.horizontalLayout_247.addWidget(self.frame_407)

        self.progressThreshold = ClickableLabel(self.progress_threshold)
        self.progressThreshold.setObjectName(u"progressThreshold")
        self.progressThreshold.setMinimumSize(QSize(0, 24))
        self.progressThreshold.setMaximumSize(QSize(16777215, 24))
        self.progressThreshold.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_247.addWidget(self.progressThreshold)


        self.verticalLayout_2.addWidget(self.progress_threshold)

        self.progress_thresholdRGB = QFrame(self.baseWidgets)
        self.progress_thresholdRGB.setObjectName(u"progress_thresholdRGB")
        self.progress_thresholdRGB.setMinimumSize(QSize(0, 24))
        self.progress_thresholdRGB.setMaximumSize(QSize(16777215, 24))
        self.progress_thresholdRGB.setStyleSheet(u"")
        self.horizontalLayout_254 = QHBoxLayout(self.progress_thresholdRGB)
        self.horizontalLayout_254.setSpacing(6)
        self.horizontalLayout_254.setObjectName(u"horizontalLayout_254")
        self.horizontalLayout_254.setContentsMargins(32, 0, 0, 0)
        self.progressThresholdR = ClickableLineEdit(self.progress_thresholdRGB)
        self.progressThresholdR.setObjectName(u"progressThresholdR")
        sizePolicy1.setHeightForWidth(self.progressThresholdR.sizePolicy().hasHeightForWidth())
        self.progressThresholdR.setSizePolicy(sizePolicy1)
        self.progressThresholdR.setMinimumSize(QSize(50, 24))
        self.progressThresholdR.setMaximumSize(QSize(50, 24))
        self.progressThresholdR.setSizeIncrement(QSize(0, 0))
        self.progressThresholdR.setBaseSize(QSize(0, 18))
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
        self.progressThresholdR.setPalette(palette17)
        self.progressThresholdR.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressThresholdR.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_254.addWidget(self.progressThresholdR)

        self.progressThresholdG = ClickableLineEdit(self.progress_thresholdRGB)
        self.progressThresholdG.setObjectName(u"progressThresholdG")
        sizePolicy1.setHeightForWidth(self.progressThresholdG.sizePolicy().hasHeightForWidth())
        self.progressThresholdG.setSizePolicy(sizePolicy1)
        self.progressThresholdG.setMinimumSize(QSize(50, 24))
        self.progressThresholdG.setMaximumSize(QSize(50, 24))
        self.progressThresholdG.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_254.addWidget(self.progressThresholdG)

        self.progressThresholdB = ClickableLineEdit(self.progress_thresholdRGB)
        self.progressThresholdB.setObjectName(u"progressThresholdB")
        sizePolicy1.setHeightForWidth(self.progressThresholdB.sizePolicy().hasHeightForWidth())
        self.progressThresholdB.setSizePolicy(sizePolicy1)
        self.progressThresholdB.setMinimumSize(QSize(50, 24))
        self.progressThresholdB.setMaximumSize(QSize(50, 24))
        self.progressThresholdB.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_254.addWidget(self.progressThresholdB)

        self.frame_421 = QFrame(self.progress_thresholdRGB)
        self.frame_421.setObjectName(u"frame_421")
        sizePolicy2.setHeightForWidth(self.frame_421.sizePolicy().hasHeightForWidth())
        self.frame_421.setSizePolicy(sizePolicy2)
        self.frame_421.setMinimumSize(QSize(0, 24))
        self.frame_421.setMaximumSize(QSize(16777215, 24))
        self.frame_421.setFont(font)
        self.frame_421.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_421.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_254.addWidget(self.frame_421)


        self.verticalLayout_2.addWidget(self.progress_thresholdRGB)

        self.progress_thresholdMode = QFrame(self.baseWidgets)
        self.progress_thresholdMode.setObjectName(u"progress_thresholdMode")
        self.progress_thresholdMode.setMinimumSize(QSize(0, 24))
        self.progress_thresholdMode.setMaximumSize(QSize(16777215, 24))
        self.progress_thresholdMode.setFrameShape(QFrame.Shape.StyledPanel)
        self.progress_thresholdMode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_253 = QHBoxLayout(self.progress_thresholdMode)
        self.horizontalLayout_253.setSpacing(0)
        self.horizontalLayout_253.setObjectName(u"horizontalLayout_253")
        self.horizontalLayout_253.setContentsMargins(32, 0, 0, 0)
        self.frame_419 = QFrame(self.progress_thresholdMode)
        self.frame_419.setObjectName(u"frame_419")
        self.frame_419.setMaximumSize(QSize(0, 24))
        self.frame_419.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_419.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_419.setLineWidth(0)

        self.horizontalLayout_253.addWidget(self.frame_419)

        self.progressThresholdMode = ClickableLabel(self.progress_thresholdMode)
        self.progressThresholdMode.setObjectName(u"progressThresholdMode")
        self.progressThresholdMode.setMinimumSize(QSize(0, 24))
        self.progressThresholdMode.setMaximumSize(QSize(16777215, 24))
        self.progressThresholdMode.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_253.addWidget(self.progressThresholdMode)


        self.verticalLayout_2.addWidget(self.progress_thresholdMode)

        self.progress_thresholdModeComboBox = QFrame(self.baseWidgets)
        self.progress_thresholdModeComboBox.setObjectName(u"progress_thresholdModeComboBox")
        self.progress_thresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.progress_thresholdModeComboBox.setMaximumSize(QSize(16777215, 24))
        self.progress_thresholdModeComboBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.progress_thresholdModeComboBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_251 = QHBoxLayout(self.progress_thresholdModeComboBox)
        self.horizontalLayout_251.setSpacing(0)
        self.horizontalLayout_251.setObjectName(u"horizontalLayout_251")
        self.horizontalLayout_251.setContentsMargins(32, 0, 0, 0)
        self.frame_414 = QFrame(self.progress_thresholdModeComboBox)
        self.frame_414.setObjectName(u"frame_414")
        self.frame_414.setMinimumSize(QSize(0, 24))
        self.frame_414.setMaximumSize(QSize(0, 24))
        self.frame_414.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_414.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_251.addWidget(self.frame_414)

        self.progressThresholdModeComboBox = QComboBox(self.progress_thresholdModeComboBox)
        self.progressThresholdModeComboBox.addItem("")
        self.progressThresholdModeComboBox.addItem("")
        self.progressThresholdModeComboBox.addItem("")
        self.progressThresholdModeComboBox.addItem("")
        self.progressThresholdModeComboBox.addItem("")
        self.progressThresholdModeComboBox.setObjectName(u"progressThresholdModeComboBox")
        self.progressThresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.progressThresholdModeComboBox.setMaximumSize(QSize(80, 24))
        self.progressThresholdModeComboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_251.addWidget(self.progressThresholdModeComboBox)

        self.frame_415 = QFrame(self.progress_thresholdModeComboBox)
        self.frame_415.setObjectName(u"frame_415")
        self.frame_415.setMinimumSize(QSize(0, 24))
        self.frame_415.setMaximumSize(QSize(16777215, 24))
        self.frame_415.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_415.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_251.addWidget(self.frame_415)


        self.verticalLayout_2.addWidget(self.progress_thresholdModeComboBox)

        self.progress_color2 = QFrame(self.baseWidgets)
        self.progress_color2.setObjectName(u"progress_color2")
        self.progress_color2.setMinimumSize(QSize(0, 24))
        self.progress_color2.setMaximumSize(QSize(16777215, 24))
        self.progress_color2.setFrameShape(QFrame.Shape.StyledPanel)
        self.progress_color2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_252 = QHBoxLayout(self.progress_color2)
        self.horizontalLayout_252.setSpacing(0)
        self.horizontalLayout_252.setObjectName(u"horizontalLayout_252")
        self.horizontalLayout_252.setContentsMargins(32, 0, 0, 0)
        self.frame_417 = QFrame(self.progress_color2)
        self.frame_417.setObjectName(u"frame_417")
        self.frame_417.setMaximumSize(QSize(0, 24))
        self.frame_417.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_417.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_417.setLineWidth(0)

        self.horizontalLayout_252.addWidget(self.frame_417)

        self.progressColor2 = ClickableLabel(self.progress_color2)
        self.progressColor2.setObjectName(u"progressColor2")
        self.progressColor2.setMinimumSize(QSize(0, 24))
        self.progressColor2.setMaximumSize(QSize(16777215, 24))
        self.progressColor2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_252.addWidget(self.progressColor2)


        self.verticalLayout_2.addWidget(self.progress_color2)

        self.progress_color2RGBA = QFrame(self.baseWidgets)
        self.progress_color2RGBA.setObjectName(u"progress_color2RGBA")
        self.progress_color2RGBA.setMinimumSize(QSize(0, 24))
        self.progress_color2RGBA.setMaximumSize(QSize(16777215, 24))
        self.progress_color2RGBA.setStyleSheet(u"")
        self.horizontalLayout_255 = QHBoxLayout(self.progress_color2RGBA)
        self.horizontalLayout_255.setSpacing(6)
        self.horizontalLayout_255.setObjectName(u"horizontalLayout_255")
        self.horizontalLayout_255.setContentsMargins(32, 0, 0, 0)
        self.progressColor2R = ClickableLineEdit(self.progress_color2RGBA)
        self.progressColor2R.setObjectName(u"progressColor2R")
        sizePolicy1.setHeightForWidth(self.progressColor2R.sizePolicy().hasHeightForWidth())
        self.progressColor2R.setSizePolicy(sizePolicy1)
        self.progressColor2R.setMinimumSize(QSize(50, 24))
        self.progressColor2R.setMaximumSize(QSize(50, 24))
        self.progressColor2R.setSizeIncrement(QSize(0, 0))
        self.progressColor2R.setBaseSize(QSize(0, 18))
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
        self.progressColor2R.setPalette(palette18)
        self.progressColor2R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressColor2R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_255.addWidget(self.progressColor2R)

        self.progressColor2G = ClickableLineEdit(self.progress_color2RGBA)
        self.progressColor2G.setObjectName(u"progressColor2G")
        sizePolicy1.setHeightForWidth(self.progressColor2G.sizePolicy().hasHeightForWidth())
        self.progressColor2G.setSizePolicy(sizePolicy1)
        self.progressColor2G.setMinimumSize(QSize(50, 24))
        self.progressColor2G.setMaximumSize(QSize(50, 24))
        self.progressColor2G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_255.addWidget(self.progressColor2G)

        self.progressColor2B = ClickableLineEdit(self.progress_color2RGBA)
        self.progressColor2B.setObjectName(u"progressColor2B")
        sizePolicy1.setHeightForWidth(self.progressColor2B.sizePolicy().hasHeightForWidth())
        self.progressColor2B.setSizePolicy(sizePolicy1)
        self.progressColor2B.setMinimumSize(QSize(50, 24))
        self.progressColor2B.setMaximumSize(QSize(50, 24))
        self.progressColor2B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_255.addWidget(self.progressColor2B)

        self.progressColor2A = ClickableLineEdit(self.progress_color2RGBA)
        self.progressColor2A.setObjectName(u"progressColor2A")
        sizePolicy1.setHeightForWidth(self.progressColor2A.sizePolicy().hasHeightForWidth())
        self.progressColor2A.setSizePolicy(sizePolicy1)
        self.progressColor2A.setMinimumSize(QSize(50, 24))
        self.progressColor2A.setMaximumSize(QSize(50, 24))
        self.progressColor2A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_255.addWidget(self.progressColor2A)

        self.frame_423 = QFrame(self.progress_color2RGBA)
        self.frame_423.setObjectName(u"frame_423")
        sizePolicy2.setHeightForWidth(self.frame_423.sizePolicy().hasHeightForWidth())
        self.frame_423.setSizePolicy(sizePolicy2)
        self.frame_423.setMinimumSize(QSize(0, 24))
        self.frame_423.setMaximumSize(QSize(16777215, 24))
        self.frame_423.setFont(font)
        self.frame_423.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_423.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_255.addWidget(self.frame_423)


        self.verticalLayout_2.addWidget(self.progress_color2RGBA)

        self.duration = ClickableLabel(self.baseWidgets)
        self.duration.setObjectName(u"duration")
        self.duration.setMinimumSize(QSize(0, 40))
        self.duration.setMaximumSize(QSize(16777215, 40))
        self.duration.setStyleSheet(u"font-size: 26px;")

        self.verticalLayout_2.addWidget(self.duration)

        self.duration_size = QFrame(self.baseWidgets)
        self.duration_size.setObjectName(u"duration_size")
        self.duration_size.setMinimumSize(QSize(0, 24))
        self.duration_size.setMaximumSize(QSize(16777215, 24))
        self.duration_size.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_size.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_287 = QHBoxLayout(self.duration_size)
        self.horizontalLayout_287.setSpacing(0)
        self.horizontalLayout_287.setObjectName(u"horizontalLayout_287")
        self.horizontalLayout_287.setContentsMargins(32, 0, 0, 0)
        self.frame_454 = QFrame(self.duration_size)
        self.frame_454.setObjectName(u"frame_454")
        self.frame_454.setMaximumSize(QSize(0, 24))
        self.frame_454.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_454.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_454.setLineWidth(0)

        self.horizontalLayout_287.addWidget(self.frame_454)

        self.durationSize = ClickableLabel(self.duration_size)
        self.durationSize.setObjectName(u"durationSize")
        self.durationSize.setMinimumSize(QSize(0, 24))
        self.durationSize.setMaximumSize(QSize(16777215, 24))
        self.durationSize.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_287.addWidget(self.durationSize)


        self.verticalLayout_2.addWidget(self.duration_size)

        self.duration_sizePx = QFrame(self.baseWidgets)
        self.duration_sizePx.setObjectName(u"duration_sizePx")
        self.duration_sizePx.setMinimumSize(QSize(0, 24))
        self.duration_sizePx.setMaximumSize(QSize(16777215, 24))
        self.duration_sizePx.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_sizePx.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_293 = QHBoxLayout(self.duration_sizePx)
        self.horizontalLayout_293.setSpacing(0)
        self.horizontalLayout_293.setObjectName(u"horizontalLayout_293")
        self.horizontalLayout_293.setContentsMargins(32, 0, 0, -1)
        self.frame_473 = QFrame(self.duration_sizePx)
        self.frame_473.setObjectName(u"frame_473")
        self.frame_473.setMinimumSize(QSize(0, 24))
        self.frame_473.setMaximumSize(QSize(0, 24))
        self.frame_473.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_473.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_293.addWidget(self.frame_473)

        self.durationSizePx = ClickableLineEdit(self.duration_sizePx)
        self.durationSizePx.setObjectName(u"durationSizePx")
        self.durationSizePx.setMinimumSize(QSize(80, 24))
        self.durationSizePx.setMaximumSize(QSize(80, 24))
        self.durationSizePx.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_293.addWidget(self.durationSizePx)

        self.frame_474 = QFrame(self.duration_sizePx)
        self.frame_474.setObjectName(u"frame_474")
        self.frame_474.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_474.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_293.addWidget(self.frame_474)


        self.verticalLayout_2.addWidget(self.duration_sizePx)

        self.duration_position = QFrame(self.baseWidgets)
        self.duration_position.setObjectName(u"duration_position")
        self.duration_position.setMinimumSize(QSize(0, 24))
        self.duration_position.setMaximumSize(QSize(16777215, 24))
        self.duration_position.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_position.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_288 = QHBoxLayout(self.duration_position)
        self.horizontalLayout_288.setSpacing(0)
        self.horizontalLayout_288.setObjectName(u"horizontalLayout_288")
        self.horizontalLayout_288.setContentsMargins(32, 0, 0, 0)
        self.frame_457 = QFrame(self.duration_position)
        self.frame_457.setObjectName(u"frame_457")
        self.frame_457.setMaximumSize(QSize(0, 24))
        self.frame_457.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_457.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_457.setLineWidth(0)

        self.horizontalLayout_288.addWidget(self.frame_457)

        self.durationPosition = ClickableLabel(self.duration_position)
        self.durationPosition.setObjectName(u"durationPosition")
        self.durationPosition.setMinimumSize(QSize(0, 24))
        self.durationPosition.setMaximumSize(QSize(16777215, 24))
        self.durationPosition.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_288.addWidget(self.durationPosition)


        self.verticalLayout_2.addWidget(self.duration_position)

        self.duration_positionXY = QFrame(self.baseWidgets)
        self.duration_positionXY.setObjectName(u"duration_positionXY")
        self.duration_positionXY.setMinimumSize(QSize(0, 24))
        self.duration_positionXY.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout_289 = QHBoxLayout(self.duration_positionXY)
        self.horizontalLayout_289.setObjectName(u"horizontalLayout_289")
        self.horizontalLayout_289.setContentsMargins(32, 0, 0, 0)
        self.durationPositionX = ClickableLineEdit(self.duration_positionXY)
        self.durationPositionX.setObjectName(u"durationPositionX")
        self.durationPositionX.setMinimumSize(QSize(70, 24))
        self.durationPositionX.setMaximumSize(QSize(70, 24))
        self.durationPositionX.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_289.addWidget(self.durationPositionX)

        self.durationPositionY = ClickableLineEdit(self.duration_positionXY)
        self.durationPositionY.setObjectName(u"durationPositionY")
        self.durationPositionY.setMinimumSize(QSize(70, 24))
        self.durationPositionY.setMaximumSize(QSize(70, 24))
        self.durationPositionY.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_289.addWidget(self.durationPositionY)

        self.frame_462 = QFrame(self.duration_positionXY)
        self.frame_462.setObjectName(u"frame_462")
        self.frame_462.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_462.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_289.addWidget(self.frame_462)


        self.verticalLayout_2.addWidget(self.duration_positionXY)

        self.duration_color = QFrame(self.baseWidgets)
        self.duration_color.setObjectName(u"duration_color")
        self.duration_color.setMinimumSize(QSize(0, 30))
        self.duration_color.setMaximumSize(QSize(16777215, 30))
        self.duration_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_color.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_285 = QHBoxLayout(self.duration_color)
        self.horizontalLayout_285.setSpacing(0)
        self.horizontalLayout_285.setObjectName(u"horizontalLayout_285")
        self.horizontalLayout_285.setContentsMargins(16, 0, 0, 0)
        self.durationColor = ClickableLabel(self.duration_color)
        self.durationColor.setObjectName(u"durationColor")
        self.durationColor.setMinimumSize(QSize(0, 30))
        self.durationColor.setMaximumSize(QSize(16777215, 30))
        self.durationColor.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_285.addWidget(self.durationColor)

        self.frame_436 = QFrame(self.duration_color)
        self.frame_436.setObjectName(u"frame_436")
        self.frame_436.setMinimumSize(QSize(0, 30))
        self.frame_436.setMaximumSize(QSize(0, 30))
        self.frame_436.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_436.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_285.addWidget(self.frame_436)


        self.verticalLayout_2.addWidget(self.duration_color)

        self.duration_color1 = QFrame(self.baseWidgets)
        self.duration_color1.setObjectName(u"duration_color1")
        self.duration_color1.setMinimumSize(QSize(0, 24))
        self.duration_color1.setMaximumSize(QSize(16777215, 24))
        self.duration_color1.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_color1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_291 = QHBoxLayout(self.duration_color1)
        self.horizontalLayout_291.setSpacing(0)
        self.horizontalLayout_291.setObjectName(u"horizontalLayout_291")
        self.horizontalLayout_291.setContentsMargins(32, 0, 0, 0)
        self.frame_470 = QFrame(self.duration_color1)
        self.frame_470.setObjectName(u"frame_470")
        self.frame_470.setMaximumSize(QSize(0, 24))
        self.frame_470.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_470.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_470.setLineWidth(0)

        self.horizontalLayout_291.addWidget(self.frame_470)

        self.durationColor1 = ClickableLabel(self.duration_color1)
        self.durationColor1.setObjectName(u"durationColor1")
        self.durationColor1.setMinimumSize(QSize(0, 24))
        self.durationColor1.setMaximumSize(QSize(16777215, 24))
        self.durationColor1.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_291.addWidget(self.durationColor1)


        self.verticalLayout_2.addWidget(self.duration_color1)

        self.duration_color1RGBA = QFrame(self.baseWidgets)
        self.duration_color1RGBA.setObjectName(u"duration_color1RGBA")
        self.duration_color1RGBA.setMinimumSize(QSize(0, 24))
        self.duration_color1RGBA.setMaximumSize(QSize(16777215, 24))
        self.duration_color1RGBA.setStyleSheet(u"")
        self.horizontalLayout_295 = QHBoxLayout(self.duration_color1RGBA)
        self.horizontalLayout_295.setSpacing(6)
        self.horizontalLayout_295.setObjectName(u"horizontalLayout_295")
        self.horizontalLayout_295.setContentsMargins(32, 0, 0, 0)
        self.durationColor1R = ClickableLineEdit(self.duration_color1RGBA)
        self.durationColor1R.setObjectName(u"durationColor1R")
        sizePolicy1.setHeightForWidth(self.durationColor1R.sizePolicy().hasHeightForWidth())
        self.durationColor1R.setSizePolicy(sizePolicy1)
        self.durationColor1R.setMinimumSize(QSize(50, 24))
        self.durationColor1R.setMaximumSize(QSize(50, 24))
        self.durationColor1R.setSizeIncrement(QSize(0, 0))
        self.durationColor1R.setBaseSize(QSize(0, 18))
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
        self.durationColor1R.setPalette(palette19)
        self.durationColor1R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.durationColor1R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_295.addWidget(self.durationColor1R)

        self.durationColor1G = ClickableLineEdit(self.duration_color1RGBA)
        self.durationColor1G.setObjectName(u"durationColor1G")
        sizePolicy1.setHeightForWidth(self.durationColor1G.sizePolicy().hasHeightForWidth())
        self.durationColor1G.setSizePolicy(sizePolicy1)
        self.durationColor1G.setMinimumSize(QSize(50, 24))
        self.durationColor1G.setMaximumSize(QSize(50, 24))
        self.durationColor1G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_295.addWidget(self.durationColor1G)

        self.durationColor1B = ClickableLineEdit(self.duration_color1RGBA)
        self.durationColor1B.setObjectName(u"durationColor1B")
        sizePolicy1.setHeightForWidth(self.durationColor1B.sizePolicy().hasHeightForWidth())
        self.durationColor1B.setSizePolicy(sizePolicy1)
        self.durationColor1B.setMinimumSize(QSize(50, 24))
        self.durationColor1B.setMaximumSize(QSize(50, 24))
        self.durationColor1B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_295.addWidget(self.durationColor1B)

        self.durationColor1A = ClickableLineEdit(self.duration_color1RGBA)
        self.durationColor1A.setObjectName(u"durationColor1A")
        sizePolicy1.setHeightForWidth(self.durationColor1A.sizePolicy().hasHeightForWidth())
        self.durationColor1A.setSizePolicy(sizePolicy1)
        self.durationColor1A.setMinimumSize(QSize(50, 24))
        self.durationColor1A.setMaximumSize(QSize(50, 24))
        self.durationColor1A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_295.addWidget(self.durationColor1A)

        self.frame_478 = QFrame(self.duration_color1RGBA)
        self.frame_478.setObjectName(u"frame_478")
        sizePolicy2.setHeightForWidth(self.frame_478.sizePolicy().hasHeightForWidth())
        self.frame_478.setSizePolicy(sizePolicy2)
        self.frame_478.setMinimumSize(QSize(0, 24))
        self.frame_478.setMaximumSize(QSize(16777215, 24))
        self.frame_478.setFont(font)
        self.frame_478.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_478.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_295.addWidget(self.frame_478)


        self.verticalLayout_2.addWidget(self.duration_color1RGBA)

        self.fixedColor_duration = QFrame(self.baseWidgets)
        self.fixedColor_duration.setObjectName(u"fixedColor_duration")
        self.fixedColor_duration.setMinimumSize(QSize(0, 20))
        self.fixedColor_duration.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_292 = QHBoxLayout(self.fixedColor_duration)
        self.horizontalLayout_292.setSpacing(5)
        self.horizontalLayout_292.setObjectName(u"horizontalLayout_292")
        self.horizontalLayout_292.setContentsMargins(32, 0, 0, 0)
        self.fixedColorDuration = ClickableLabel(self.fixedColor_duration)
        self.fixedColorDuration.setObjectName(u"fixedColorDuration")
        self.fixedColorDuration.setMinimumSize(QSize(195, 0))
        self.fixedColorDuration.setMaximumSize(QSize(195, 24))
        self.fixedColorDuration.setStyleSheet(u"")

        self.horizontalLayout_292.addWidget(self.fixedColorDuration)

        self.fixedColorDurationCheckBox = QCheckBox(self.fixedColor_duration)
        self.fixedColorDurationCheckBox.setObjectName(u"fixedColorDurationCheckBox")
        self.fixedColorDurationCheckBox.setMaximumSize(QSize(16777215, 24))
        self.fixedColorDurationCheckBox.setStyleSheet(u"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	background-color: rgb(18, 18, 18);\n"
"	border: 1px solid;\n"
"	border-radius: 5px;\n"
"} QCheckBox::indicator::checked {\n"
"	background-color: white;\n"
"}")
        self.fixedColorDurationCheckBox.setIconSize(QSize(18, 18))
        self.fixedColorDurationCheckBox.setChecked(False)
        self.fixedColorDurationCheckBox.setTristate(False)

        self.horizontalLayout_292.addWidget(self.fixedColorDurationCheckBox)


        self.verticalLayout_2.addWidget(self.fixedColor_duration)

        self.duration_threshold = QFrame(self.baseWidgets)
        self.duration_threshold.setObjectName(u"duration_threshold")
        self.duration_threshold.setMinimumSize(QSize(0, 24))
        self.duration_threshold.setMaximumSize(QSize(16777215, 24))
        self.duration_threshold.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_threshold.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_284 = QHBoxLayout(self.duration_threshold)
        self.horizontalLayout_284.setSpacing(0)
        self.horizontalLayout_284.setObjectName(u"horizontalLayout_284")
        self.horizontalLayout_284.setContentsMargins(32, 0, 0, 0)
        self.frame_428 = QFrame(self.duration_threshold)
        self.frame_428.setObjectName(u"frame_428")
        self.frame_428.setMaximumSize(QSize(0, 24))
        self.frame_428.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_428.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_428.setLineWidth(0)

        self.horizontalLayout_284.addWidget(self.frame_428)

        self.durationThreshold = ClickableLabel(self.duration_threshold)
        self.durationThreshold.setObjectName(u"durationThreshold")
        self.durationThreshold.setMinimumSize(QSize(0, 24))
        self.durationThreshold.setMaximumSize(QSize(16777215, 24))
        self.durationThreshold.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_284.addWidget(self.durationThreshold)


        self.verticalLayout_2.addWidget(self.duration_threshold)

        self.duration_thresholdRGB = QFrame(self.baseWidgets)
        self.duration_thresholdRGB.setObjectName(u"duration_thresholdRGB")
        self.duration_thresholdRGB.setMinimumSize(QSize(0, 24))
        self.duration_thresholdRGB.setMaximumSize(QSize(16777215, 24))
        self.duration_thresholdRGB.setStyleSheet(u"")
        self.horizontalLayout_286 = QHBoxLayout(self.duration_thresholdRGB)
        self.horizontalLayout_286.setSpacing(6)
        self.horizontalLayout_286.setObjectName(u"horizontalLayout_286")
        self.horizontalLayout_286.setContentsMargins(32, 0, 0, 0)
        self.durationThresholdR = ClickableLineEdit(self.duration_thresholdRGB)
        self.durationThresholdR.setObjectName(u"durationThresholdR")
        sizePolicy1.setHeightForWidth(self.durationThresholdR.sizePolicy().hasHeightForWidth())
        self.durationThresholdR.setSizePolicy(sizePolicy1)
        self.durationThresholdR.setMinimumSize(QSize(50, 24))
        self.durationThresholdR.setMaximumSize(QSize(50, 24))
        self.durationThresholdR.setSizeIncrement(QSize(0, 0))
        self.durationThresholdR.setBaseSize(QSize(0, 18))
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
        self.durationThresholdR.setPalette(palette20)
        self.durationThresholdR.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.durationThresholdR.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_286.addWidget(self.durationThresholdR)

        self.durationThresholdG = ClickableLineEdit(self.duration_thresholdRGB)
        self.durationThresholdG.setObjectName(u"durationThresholdG")
        sizePolicy1.setHeightForWidth(self.durationThresholdG.sizePolicy().hasHeightForWidth())
        self.durationThresholdG.setSizePolicy(sizePolicy1)
        self.durationThresholdG.setMinimumSize(QSize(50, 24))
        self.durationThresholdG.setMaximumSize(QSize(50, 24))
        self.durationThresholdG.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_286.addWidget(self.durationThresholdG)

        self.durationThresholdB = ClickableLineEdit(self.duration_thresholdRGB)
        self.durationThresholdB.setObjectName(u"durationThresholdB")
        sizePolicy1.setHeightForWidth(self.durationThresholdB.sizePolicy().hasHeightForWidth())
        self.durationThresholdB.setSizePolicy(sizePolicy1)
        self.durationThresholdB.setMinimumSize(QSize(50, 24))
        self.durationThresholdB.setMaximumSize(QSize(50, 24))
        self.durationThresholdB.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_286.addWidget(self.durationThresholdB)

        self.frame_445 = QFrame(self.duration_thresholdRGB)
        self.frame_445.setObjectName(u"frame_445")
        sizePolicy2.setHeightForWidth(self.frame_445.sizePolicy().hasHeightForWidth())
        self.frame_445.setSizePolicy(sizePolicy2)
        self.frame_445.setMinimumSize(QSize(0, 24))
        self.frame_445.setMaximumSize(QSize(16777215, 24))
        self.frame_445.setFont(font)
        self.frame_445.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_445.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_286.addWidget(self.frame_445)


        self.verticalLayout_2.addWidget(self.duration_thresholdRGB)

        self.duration_thresholdMode = QFrame(self.baseWidgets)
        self.duration_thresholdMode.setObjectName(u"duration_thresholdMode")
        self.duration_thresholdMode.setMinimumSize(QSize(0, 24))
        self.duration_thresholdMode.setMaximumSize(QSize(16777215, 24))
        self.duration_thresholdMode.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_thresholdMode.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_298 = QHBoxLayout(self.duration_thresholdMode)
        self.horizontalLayout_298.setSpacing(0)
        self.horizontalLayout_298.setObjectName(u"horizontalLayout_298")
        self.horizontalLayout_298.setContentsMargins(32, 0, 0, 0)
        self.frame_484 = QFrame(self.duration_thresholdMode)
        self.frame_484.setObjectName(u"frame_484")
        self.frame_484.setMaximumSize(QSize(0, 24))
        self.frame_484.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_484.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_484.setLineWidth(0)

        self.horizontalLayout_298.addWidget(self.frame_484)

        self.durationThresholdMode = ClickableLabel(self.duration_thresholdMode)
        self.durationThresholdMode.setObjectName(u"durationThresholdMode")
        self.durationThresholdMode.setMinimumSize(QSize(0, 24))
        self.durationThresholdMode.setMaximumSize(QSize(16777215, 24))
        self.durationThresholdMode.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_298.addWidget(self.durationThresholdMode)


        self.verticalLayout_2.addWidget(self.duration_thresholdMode)

        self.duration_thresholdModeComboBox = QFrame(self.baseWidgets)
        self.duration_thresholdModeComboBox.setObjectName(u"duration_thresholdModeComboBox")
        self.duration_thresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.duration_thresholdModeComboBox.setMaximumSize(QSize(16777215, 24))
        self.duration_thresholdModeComboBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_thresholdModeComboBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_290 = QHBoxLayout(self.duration_thresholdModeComboBox)
        self.horizontalLayout_290.setSpacing(0)
        self.horizontalLayout_290.setObjectName(u"horizontalLayout_290")
        self.horizontalLayout_290.setContentsMargins(32, 0, 0, 0)
        self.frame_466 = QFrame(self.duration_thresholdModeComboBox)
        self.frame_466.setObjectName(u"frame_466")
        self.frame_466.setMinimumSize(QSize(0, 24))
        self.frame_466.setMaximumSize(QSize(0, 24))
        self.frame_466.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_466.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_290.addWidget(self.frame_466)

        self.durationThresholdModeComboBox = QComboBox(self.duration_thresholdModeComboBox)
        self.durationThresholdModeComboBox.addItem("")
        self.durationThresholdModeComboBox.addItem("")
        self.durationThresholdModeComboBox.addItem("")
        self.durationThresholdModeComboBox.addItem("")
        self.durationThresholdModeComboBox.addItem("")
        self.durationThresholdModeComboBox.setObjectName(u"durationThresholdModeComboBox")
        self.durationThresholdModeComboBox.setMinimumSize(QSize(0, 24))
        self.durationThresholdModeComboBox.setMaximumSize(QSize(80, 24))
        self.durationThresholdModeComboBox.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_290.addWidget(self.durationThresholdModeComboBox)

        self.frame_468 = QFrame(self.duration_thresholdModeComboBox)
        self.frame_468.setObjectName(u"frame_468")
        self.frame_468.setMinimumSize(QSize(0, 24))
        self.frame_468.setMaximumSize(QSize(16777215, 24))
        self.frame_468.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_468.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_290.addWidget(self.frame_468)


        self.verticalLayout_2.addWidget(self.duration_thresholdModeComboBox)

        self.duration_color2 = QFrame(self.baseWidgets)
        self.duration_color2.setObjectName(u"duration_color2")
        self.duration_color2.setMinimumSize(QSize(0, 24))
        self.duration_color2.setMaximumSize(QSize(16777215, 24))
        self.duration_color2.setFrameShape(QFrame.Shape.StyledPanel)
        self.duration_color2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_297 = QHBoxLayout(self.duration_color2)
        self.horizontalLayout_297.setSpacing(0)
        self.horizontalLayout_297.setObjectName(u"horizontalLayout_297")
        self.horizontalLayout_297.setContentsMargins(32, 0, 0, 0)
        self.frame_482 = QFrame(self.duration_color2)
        self.frame_482.setObjectName(u"frame_482")
        self.frame_482.setMaximumSize(QSize(0, 24))
        self.frame_482.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_482.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_482.setLineWidth(0)

        self.horizontalLayout_297.addWidget(self.frame_482)

        self.durationColor2 = ClickableLabel(self.duration_color2)
        self.durationColor2.setObjectName(u"durationColor2")
        self.durationColor2.setMinimumSize(QSize(0, 24))
        self.durationColor2.setMaximumSize(QSize(16777215, 24))
        self.durationColor2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_297.addWidget(self.durationColor2)


        self.verticalLayout_2.addWidget(self.duration_color2)

        self.duration_color2RGBA = QFrame(self.baseWidgets)
        self.duration_color2RGBA.setObjectName(u"duration_color2RGBA")
        self.duration_color2RGBA.setMinimumSize(QSize(0, 24))
        self.duration_color2RGBA.setMaximumSize(QSize(16777215, 24))
        self.duration_color2RGBA.setStyleSheet(u"")
        self.horizontalLayout_296 = QHBoxLayout(self.duration_color2RGBA)
        self.horizontalLayout_296.setSpacing(6)
        self.horizontalLayout_296.setObjectName(u"horizontalLayout_296")
        self.horizontalLayout_296.setContentsMargins(32, 0, 0, 0)
        self.durationColor2R = ClickableLineEdit(self.duration_color2RGBA)
        self.durationColor2R.setObjectName(u"durationColor2R")
        sizePolicy1.setHeightForWidth(self.durationColor2R.sizePolicy().hasHeightForWidth())
        self.durationColor2R.setSizePolicy(sizePolicy1)
        self.durationColor2R.setMinimumSize(QSize(50, 24))
        self.durationColor2R.setMaximumSize(QSize(50, 24))
        self.durationColor2R.setSizeIncrement(QSize(0, 0))
        self.durationColor2R.setBaseSize(QSize(0, 18))
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
        self.durationColor2R.setPalette(palette21)
        self.durationColor2R.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.durationColor2R.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_296.addWidget(self.durationColor2R)

        self.durationColor2G = ClickableLineEdit(self.duration_color2RGBA)
        self.durationColor2G.setObjectName(u"durationColor2G")
        sizePolicy1.setHeightForWidth(self.durationColor2G.sizePolicy().hasHeightForWidth())
        self.durationColor2G.setSizePolicy(sizePolicy1)
        self.durationColor2G.setMinimumSize(QSize(50, 24))
        self.durationColor2G.setMaximumSize(QSize(50, 24))
        self.durationColor2G.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_296.addWidget(self.durationColor2G)

        self.durationColor2B = ClickableLineEdit(self.duration_color2RGBA)
        self.durationColor2B.setObjectName(u"durationColor2B")
        sizePolicy1.setHeightForWidth(self.durationColor2B.sizePolicy().hasHeightForWidth())
        self.durationColor2B.setSizePolicy(sizePolicy1)
        self.durationColor2B.setMinimumSize(QSize(50, 24))
        self.durationColor2B.setMaximumSize(QSize(50, 24))
        self.durationColor2B.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_296.addWidget(self.durationColor2B)

        self.durationColor2A = ClickableLineEdit(self.duration_color2RGBA)
        self.durationColor2A.setObjectName(u"durationColor2A")
        sizePolicy1.setHeightForWidth(self.durationColor2A.sizePolicy().hasHeightForWidth())
        self.durationColor2A.setSizePolicy(sizePolicy1)
        self.durationColor2A.setMinimumSize(QSize(50, 24))
        self.durationColor2A.setMaximumSize(QSize(50, 24))
        self.durationColor2A.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_296.addWidget(self.durationColor2A)

        self.frame_480 = QFrame(self.duration_color2RGBA)
        self.frame_480.setObjectName(u"frame_480")
        sizePolicy2.setHeightForWidth(self.frame_480.sizePolicy().hasHeightForWidth())
        self.frame_480.setSizePolicy(sizePolicy2)
        self.frame_480.setMinimumSize(QSize(0, 24))
        self.frame_480.setMaximumSize(QSize(16777215, 24))
        self.frame_480.setFont(font)
        self.frame_480.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_480.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_296.addWidget(self.frame_480)


        self.verticalLayout_2.addWidget(self.duration_color2RGBA)

        self.baseWidgets_srollArea.setWidget(self.baseWidgets)

        self.horizontalLayout_3.addWidget(self.baseWidgets_srollArea)

        self.tabWidget.addTab(self.base_widgets, "")
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy4)
        self.textBrowser_2.setStyleSheet(u"border: none;")

        self.horizontalLayout_205.addWidget(self.textBrowser_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_26.addWidget(self.tabWidget)

        self.element_documentation = QTextBrowser(self.frame_5)
        self.element_documentation.setObjectName(u"element_documentation")
        sizePolicy4.setHeightForWidth(self.element_documentation.sizePolicy().hasHeightForWidth())
        self.element_documentation.setSizePolicy(sizePolicy4)
        self.element_documentation.setStyleSheet(u"border-left: 2px solid white;\n"
"margin-left: 2px")

        self.horizontalLayout_26.addWidget(self.element_documentation)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 25))
        self.frame.setMaximumSize(QSize(16777215, 25))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 2, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame_3)

        self.ok = QPushButton(self.frame)
        self.ok.setObjectName(u"ok")
        self.ok.setMinimumSize(QSize(90, 0))
        self.ok.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.ok)

        self.cancel = QPushButton(self.frame)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(90, 0))
        self.cancel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.cancel)

        self.apply = QPushButton(self.frame)
        self.apply.setObjectName(u"apply")
        self.apply.setMinimumSize(QSize(90, 0))
        self.apply.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.apply)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)



    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.background.setText(QCoreApplication.translate("Dialog", u"\u0424\u043e\u043d:", None))
        self.fixedColorBackground.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430", None))
        self.fixedColorBackgroundCheckBox.setText("")
        self.backgroundColor.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430", None))
        self.backgroundR.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.backgroundG.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.backgroundB.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.albumImg.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043b\u043e\u0436\u043a\u0430 \u0442\u0440\u0435\u043a\u0430:", None))
        self.albumImgSize.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043e\u0431\u043b\u043e\u0436\u043a\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.albumImgSizePx.setPlaceholderText(QCoreApplication.translate("Dialog", u"px", None))
        self.albumImgRadius.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043e\u0431\u043b\u043e\u0436\u043a\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.albumImgRadiusPx.setPlaceholderText(QCoreApplication.translate("Dialog", u"px", None))
        self.albumImgPosition.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043e\u0431\u043b\u043e\u0436\u043a\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.albumImgPositionX.setPlaceholderText(QCoreApplication.translate("Dialog", u"X", None))
        self.albumImgPositionY.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y", None))
        self.trackName.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u0442\u0440\u0435\u043a\u0430:", None))
        self.trackNameMode.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.trackNameModeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"right", None))
        self.trackNameModeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"left", None))
        self.trackNameModeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"up", None))
        self.trackNameModeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"down", None))

        self.trackNameSize.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.trackNameSizePx.setPlaceholderText(QCoreApplication.translate("Dialog", u"px", None))
        self.trackNamePosition.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.trackNamePositionX.setPlaceholderText(QCoreApplication.translate("Dialog", u"X", None))
        self.trackNamePositionY.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y", None))
        self.trackNameColor.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430:", None))
        self.trackNameColor1.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430 1:", None))
        self.trackNameColor1R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.trackNameColor1G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.trackNameColor1B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.trackNameColor1A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.fixedColorTrackName.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.fixedColorTrackNameCheckBox.setText("")
        self.trackNameThreshold.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.trackNameThresholdR.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.trackNameThresholdG.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.trackNameThresholdB.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.trackNameThresholdMode.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.trackNameThresholdModeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u">", None))
        self.trackNameThresholdModeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"<", None))
        self.trackNameThresholdModeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u">=", None))
        self.trackNameThresholdModeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"<=", None))
        self.trackNameThresholdModeComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"==", None))

        self.trackNameColor2.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0435\u043d\u0438 \u0442\u0440\u0435\u043a\u0430 2:", None))
        self.trackNameColor2R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.trackNameColor2G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.trackNameColor2B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.trackNameColor2A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.artists.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u0435\u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439:", None))
        self.artistsMode.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.artistsModeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"right", None))
        self.artistsModeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"left", None))
        self.artistsModeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"up", None))
        self.artistsModeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"down", None))

        self.artistsSize.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.artistsSizePx.setPlaceholderText(QCoreApplication.translate("Dialog", u"px", None))
        self.artistsPosition.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0441\u0442\u0443\u043f \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.artistsPositionPx.setPlaceholderText(QCoreApplication.translate("Dialog", u"px", None))
        self.artistsColor.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439:", None))
        self.artistsColor1.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439 1:", None))
        self.artistsColor1R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.artistsColor1G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.artistsColor1B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.artistsColor1A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.fixedColorArtists.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.fixedColorArtistsCheckBox.setText("")
        self.artistsThreshold.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.artistsThresholdR.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.artistsThresholdG.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.artistsThresholdB.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.artistsThresholdMode.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.artistsThresholdModeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u">", None))
        self.artistsThresholdModeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"<", None))
        self.artistsThresholdModeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u">=", None))
        self.artistsThresholdModeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"<=", None))
        self.artistsThresholdModeComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"==", None))

        self.artistsColor2.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0438\u043c\u0451\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439 2:", None))
        self.artistsColor2R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.artistsColor2G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.artistsColor2B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.artistsColor2A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.progressbar.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440 \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044f:", None))
        self.progressbarSize.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0431\u0430\u0440\u0430", None))
        self.progressbarSizeX.setPlaceholderText(QCoreApplication.translate("Dialog", u"X", None))
        self.progressbarSizeY.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y", None))
        self.progresbarRadius.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0431\u0430\u0440\u0430", None))
        self.progresbarRadiusPx.setPlaceholderText(QCoreApplication.translate("Dialog", u"px", None))
        self.progresbarPosition.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0431\u0430\u0440\u0430", None))
        self.progresbarPositionX.setPlaceholderText(QCoreApplication.translate("Dialog", u"X", None))
        self.progresbarPositionY.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y", None))
        self.progresbarAddColor.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u043f\u0435\u0440\u0432\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0431\u0430\u0440\u0430:", None))
        self.progresbarAddColor1.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u043f\u0435\u0440\u0432\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 1:", None))
        self.progressbarAddColor1R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progressbarAddColor1G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progressbarAddColor1B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progressbarAddColor1A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.fixedColorProgrsbarAdd.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.fixedColorProgrsbarAddCheckBox.setText("")
        self.progressbarAddThreshold.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.progresbarAddThresholdR.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progresbarAddThresholdG.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progresbarAddThresholdB.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progresbarAddThresholdMode.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.progresbarAddThresholdModeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u">", None))
        self.progresbarAddThresholdModeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"<", None))
        self.progresbarAddThresholdModeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u">=", None))
        self.progresbarAddThresholdModeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"<=", None))
        self.progresbarAddThresholdModeComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"==", None))

        self.progresbarAddColor2.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u043f\u0435\u0440\u0432\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 2:", None))
        self.progresbarAddColor2R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progresbarAddColor2G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progresbarAddColor2B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progresbarAddColor2A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.progresbarSubColor.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0432\u0442\u043e\u0440\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430:", None))
        self.progresbarSubColor1.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0432\u0442\u043e\u0440\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 1:", None))
        self.progressbarSubColor1R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progressbarSubColor1G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progressbarSubColor1B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progressbarSubColor1A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.fixedColorProgresbarSub.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.fixedColorProgresbarSubCheckBox.setText("")
        self.progresbarSubThreshold.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.progresbarSubThresholdR.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progresbarSubThresholdG.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progresbarSubThresholdB.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progresbarSubThresholdMode.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.progresbarSubThresholdModeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u">", None))
        self.progresbarSubThresholdModeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"<", None))
        self.progresbarSubThresholdModeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u">=", None))
        self.progresbarSubThresholdModeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"<=", None))
        self.progresbarSubThresholdModeComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"==", None))

        self.progresbarSubColor2.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0432\u0442\u043e\u0440\u043e\u0439 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u044b \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 2:", None))
        self.progresbarSubColor2R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progresbarSubColor2G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progresbarSubColor2B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progresbarSubColor2A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.progresbarHandlerLabel.setText(QCoreApplication.translate("Dialog", u"\u0425\u0435\u043d\u0434\u043b\u0435\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430:", None))
        self.progresbarHandlerSize.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0445\u0435\u043d\u0434\u043b\u0435\u0440\u0430 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430", None))
        self.progresbarHandlerSizeX.setPlaceholderText(QCoreApplication.translate("Dialog", u"X", None))
        self.progresbarHandlerSizeY.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y", None))
        self.progresbarHandlerRadius.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0445\u0435\u043d\u0434\u043b\u0435\u0440\u0430 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430", None))
        self.progresbarHandlerRadiusPx.setPlaceholderText(QCoreApplication.translate("Dialog", u"px", None))
        self.progresbarHandlerColor.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0445\u0435\u043d\u0434\u043b\u0435\u0440\u0430 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430", None))
        self.progresbarHandlerColor1.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0445\u0435\u043d\u0434\u043b\u0435\u0440\u0430 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 1:", None))
        self.progresbarHandlerColor1R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progresbarHandlerColor1G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progresbarHandlerColor1B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progresbarHandlerColor1A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.fixedColorProgresbarHandler.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.fixedColorProgresbarHandlerCheckBox.setText("")
        self.progresbarHandlerThreshold.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.progresbarHandlerThresholdR.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progresbarHandlerThresholdG.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progresbarHandlerThresholdB.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progresbarHandlerThresholdMode.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.progresbarHandlerThresholdModeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u">", None))
        self.progresbarHandlerThresholdModeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"<", None))
        self.progresbarHandlerThresholdModeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u">=", None))
        self.progresbarHandlerThresholdModeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"<=", None))
        self.progresbarHandlerThresholdModeComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"==", None))

        self.progresbarHandlerColor2.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0445\u0435\u043d\u0434\u043b\u0435\u0440\u0430 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0431\u0430\u0440\u0430 2:", None))
        self.progresbarHandlerColor2R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progresbarHandlerColor2G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progresbarHandlerColor2B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progresbarHandlerColor2A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.progress.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u0442\u0440\u0435\u043a\u0430:", None))
        self.progressSze.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430", None))
        self.progressSizePx.setPlaceholderText(QCoreApplication.translate("Dialog", u"px", None))
        self.progressPosition.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430", None))
        self.progressPositionX.setPlaceholderText(QCoreApplication.translate("Dialog", u"X", None))
        self.progressPositionY.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y", None))
        self.progressColor.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430:", None))
        self.progressColor1.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430 1:", None))
        self.progressColor1R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progressColor1G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progressColor1B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progressColor1A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.fixedColorProgress.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.fixedColorProgressCheckBox.setText("")
        self.progressThreshold.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.progressThresholdR.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progressThresholdG.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progressThresholdB.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progressThresholdMode.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.progressThresholdModeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u">", None))
        self.progressThresholdModeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"<", None))
        self.progressThresholdModeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u">=", None))
        self.progressThresholdModeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"<=", None))
        self.progressThresholdModeComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"==", None))

        self.progressColor2.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u0442\u0440\u0435\u043a\u0430 2:", None))
        self.progressColor2R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.progressColor2G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.progressColor2B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.progressColor2A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.duration.setText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0440\u0435\u043a\u0430:", None))
        self.durationSize.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.durationSizePx.setPlaceholderText(QCoreApplication.translate("Dialog", u"px", None))
        self.durationPosition.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430", None))
        self.durationPositionX.setPlaceholderText(QCoreApplication.translate("Dialog", u"X", None))
        self.durationPositionY.setPlaceholderText(QCoreApplication.translate("Dialog", u"Y", None))
        self.durationColor.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430:", None))
        self.durationColor1.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430 1:", None))
        self.durationColor1R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.durationColor1G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.durationColor1B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.durationColor1A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.fixedColorDuration.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 ", None))
        self.fixedColorDurationCheckBox.setText("")
        self.durationThreshold.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u043e\u0433 \u043e\u0442\u0442\u0435\u043d\u043a\u0430", None))
        self.durationThresholdR.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.durationThresholdG.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.durationThresholdB.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.durationThresholdMode.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0442\u043e\u0434 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.durationThresholdModeComboBox.setItemText(0, QCoreApplication.translate("Dialog", u">", None))
        self.durationThresholdModeComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"<", None))
        self.durationThresholdModeComboBox.setItemText(2, QCoreApplication.translate("Dialog", u">=", None))
        self.durationThresholdModeComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"<=", None))
        self.durationThresholdModeComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"==", None))

        self.durationColor2.setText(QCoreApplication.translate("Dialog", u"\u0426\u0432\u0435\u0442 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0442\u0440\u0435\u043a\u0430 2:", None))
        self.durationColor2R.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.durationColor2G.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.durationColor2B.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
        self.durationColor2A.setPlaceholderText(QCoreApplication.translate("Dialog", u"A", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.base_widgets), QCoreApplication.translate("Dialog", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0432\u0438\u0434\u0436\u0435\u0442\u044b", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\u0410\u0434\u0434\u043e\u043d\u044b", None))
        self.element_documentation.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.ok.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.apply.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi
