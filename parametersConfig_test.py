# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confui.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractScrollArea, QApplication, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QScrollArea,
    QSizePolicy, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(882, 514)
        Dialog.setStyleSheet(u"background-color: rgb(18, 18, 18);\n"
"color: white;\n"
"font-size: 14px;")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_27.setSpacing(2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.frame_5)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setMinimumSize(QSize(430, 0))
        self.tabWidget_2.setMaximumSize(QSize(430, 16777215))
        self.tabWidget_2.setStyleSheet(u"QTabWidget::pane\n"
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
        self.tabWidget_2.setTabPosition(QTabWidget.TabPosition.West)
        self.base_widgets_2 = QWidget()
        self.base_widgets_2.setObjectName(u"base_widgets_2")
        self.base_widgets_2.setMinimumSize(QSize(0, 0))
        self.base_widgets_2.setMaximumSize(QSize(16777215, 16777215))
        self.base_widgets_2.setStyleSheet(u"background: rgb(42, 42, 42);")
        self.horizontalLayout_4 = QHBoxLayout(self.base_widgets_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.baseWidgets_srollArea_2 = QScrollArea(self.base_widgets_2)
        self.baseWidgets_srollArea_2.setObjectName(u"baseWidgets_srollArea_2")
        self.baseWidgets_srollArea_2.setStyleSheet(u"border: none;")
        self.baseWidgets_srollArea_2.setLineWidth(0)
        self.baseWidgets_srollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.baseWidgets_srollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.baseWidgets_srollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.baseWidgets_srollArea_2.setWidgetResizable(True)
        self.baseWidgets_2 = QWidget()
        self.baseWidgets_2.setObjectName(u"baseWidgets_2")
        self.baseWidgets_2.setGeometry(QRect(0, 0, 403, 461))
        self.verticalLayout_3 = QVBoxLayout(self.baseWidgets_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 9, 0, 12)
        self.baseWidgets_srollArea_2.setWidget(self.baseWidgets_2)

        self.horizontalLayout_4.addWidget(self.baseWidgets_srollArea_2)

        self.tabWidget_2.addTab(self.base_widgets_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setMinimumSize(QSize(0, 0))
        self.tab_3.setMaximumSize(QSize(16777215, 16777215))
        self.tab_3.setStyleSheet(u"background: rgb(42, 42, 42);")
        self.horizontalLayout_206 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_206.setSpacing(0)
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_206.setContentsMargins(2, 6, 0, 0)
        self.textBrowser_3 = QTextBrowser(self.tab_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy1)
        self.textBrowser_3.setStyleSheet(u"border: none;")

        self.horizontalLayout_206.addWidget(self.textBrowser_3)

        self.tabWidget_2.addTab(self.tab_3, "")

        self.horizontalLayout_27.addWidget(self.tabWidget_2)

        self.element_documentation_2 = QTextBrowser(self.frame_5)
        self.element_documentation_2.setObjectName(u"element_documentation_2")
        sizePolicy1.setHeightForWidth(self.element_documentation_2.sizePolicy().hasHeightForWidth())
        self.element_documentation_2.setSizePolicy(sizePolicy1)
        self.element_documentation_2.setStyleSheet(u"border-left: 2px solid white;\n"
"margin-left: 2px")

        self.horizontalLayout_27.addWidget(self.element_documentation_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|
                                          QDialogButtonBox.StandardButton.Cancel|
                                          QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.button(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.base_widgets_2), QCoreApplication.translate("Dialog", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0432\u0438\u0434\u0436\u0435\u0442\u044b", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"\u0410\u0434\u0434\u043e\u043d\u044b", None))
        self.element_documentation_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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

