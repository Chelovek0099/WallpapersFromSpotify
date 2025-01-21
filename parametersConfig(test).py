# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parametersConfig(copy).ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QFrame,
    QHBoxLayout, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(967, 502)
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
        self.baseWidgets.setGeometry(QRect(0, 0, 403, 463))
        self.verticalLayout_2 = QVBoxLayout(self.baseWidgets)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 9, 0, 12)
        self.frame_4 = QFrame(self.baseWidgets)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 24))
        self.lineEdit_3.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 24))
        self.lineEdit.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 24))
        self.lineEdit_2.setStyleSheet(u"color: white;\n"
"border:1px solid rgb(18, 18, 18);\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 18, 18);")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(180, 0))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.baseWidgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy1)
        self.textBrowser_2.setStyleSheet(u"border: none;")

        self.horizontalLayout_205.addWidget(self.textBrowser_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_26.addWidget(self.tabWidget)

        self.element_documentation = QTextBrowser(self.frame_5)
        self.element_documentation.setObjectName(u"element_documentation")
        sizePolicy1.setHeightForWidth(self.element_documentation.sizePolicy().hasHeightForWidth())
        self.element_documentation.setSizePolicy(sizePolicy1)
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

    def deleteWidgetFromScroll(self, widget):
        self.verticalLayout_2.removeWidget(widget)
        del widget

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"R", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"G", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"B", None))
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

