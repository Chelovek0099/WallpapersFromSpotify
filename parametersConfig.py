from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QFrame,
                               QHBoxLayout, QPushButton, QScrollArea, QSizePolicy,
                               QTabWidget, QTextBrowser, QVBoxLayout, QWidget)

import json
from markdownToHtml import *
from extraWidgets import *
from exception import *


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
        self.scroll = QVBoxLayout(self.baseWidgets)
        self.scroll.setObjectName(u"verticalLayout_2")
        self.scroll.setContentsMargins(6, 9, 0, 12)
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

        self.scroll.addWidget(QFrame())
        self.widgets = 0

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

        with open('widgets.json', "r", encoding = "utf-8") as widgets:
            all_widgets = json.load(widgets)

        self.parameter_configs = {}
        for widget in all_widgets:
            with open(fr"addons\{widget}\parametersConfig.json", "r", encoding = "utf-8") as parameters_files:
                parameters = json.load(parameters_files)
            with open(fr"addons\{widget}\config.json", 'r') as config_file:
                config = json.load(config_file)

            title = H1(parameters["name"])
            self.addWidgetIntoSroll(title)

            self.parameter_configs[widget] = {}

            for category in parameters["categories"].keys():
                if category == "main":
                    margin = 16
                else:
                    category_label = H2(category)
                    self.addWidgetIntoSroll(category_label)
                    margin = 32

                for parameter in parameters["categories"][category]:
                    widget_type = parameter["widget_type"]
                    data_type = parameter["data_type"]
                    parameter_name = parameter['parameter']
                    doc_file = parameter["documentation"]

                    self.parameter_configs[widget][parameter_name] = {}
                    self.parameter_configs[widget][parameter_name]['widget_type'] = widget_type
                    self.parameter_configs[widget][parameter_name]['data_type'] = data_type
                    self.parameter_configs[widget][parameter_name]['parameter_name'] = parameter_name

                    if widget_type == "line_edits":
                        parameter_title = H3(margin, parameter["name"])
                        line_edits = LineEdits(margin, *parameter["placeholders"])
                        line_edits.setTexts(config[parameter_name])

                        self.parameter_configs[widget][parameter_name]['widget'] = line_edits

                        parameter_title.label.clicked.connect(lambda d_f=doc_file: self.setDocumentation(d_f))
                        for line_edit in line_edits.getLineEdits():
                            line_edit.clicked.connect(lambda d_f=doc_file: self.setDocumentation(d_f))

                        self.addWidgetIntoSroll(parameter_title)
                        self.addWidgetIntoSroll(line_edits)
                    elif widget_type == "combo_box":
                        parameter_title = H3(margin, parameter["name"])
                        combo_box = ComboBox(margin, *parameter["options"])
                        combo_box.setText(config[parameter_name])

                        self.parameter_configs[widget][parameter_name]['widget'] = combo_box.comboBox

                        parameter_title.label.clicked.connect(lambda d_f=doc_file: self.setDocumentation(d_f))

                        self.addWidgetIntoSroll(parameter_title)
                        self.addWidgetIntoSroll(combo_box)
                    elif widget_type == "check_box":
                        check_box = NamedCheckBox(margin, parameter["name"])
                        check_box.setChecked(config[parameter_name])

                        self.parameter_configs[widget][parameter_name]['widget'] = check_box.checkbox

                        check_box.label.clicked.connect(lambda d_f=doc_file: self.setDocumentation(d_f))

                        self.addWidgetIntoSroll(check_box)
                    else:
                        raise ConfigTypeError("'" + widget_type + "'", widget,
                                              str(parameters["categories"][category]))

    def get_configs(self):
        configs = {}
        for widget in self.parameter_configs.keys():
            with open(fr"addons\{widget}\config.json", 'r') as config_file:
                configs[widget] = json.load(config_file)
        self.configs = configs

    def set_configs(self):
        for widget in self.configs.keys():
            with open(fr"addons\{widget}\config.json", 'w') as config_file:
                json.dump(self.configs[widget], config_file)

    def change_config(self):
        for widget in self.parameter_configs.keys():

            with open(fr"addons\{widget}\config.json", 'r') as config_file:
                config = json.load(config_file)

            for parameter in self.parameter_configs[widget]:
                parameter = self.parameter_configs[widget][parameter]
                widget_type = parameter['widget_type']
                data_type = parameter['data_type']
                parameter_widget = parameter['widget']
                parameter_name = parameter['parameter_name']

                if widget_type == "line_edits":
                    line_edits = parameter_widget.getLineEdits()
                    if len(line_edits) != 1:
                        values = []
                        for line_edit in line_edits:
                            values.append(eval(f"{data_type}(line_edit.text())"))
                    else:
                        values = eval(f"{data_type}(line_edits[0].text())")
                    config[parameter_name] = values
                elif widget_type == "combo_box":
                    combo_box = parameter_widget
                    config[parameter_name] = eval(f"{data_type}(combo_box.currentText())")
                elif widget_type == "check_box":
                    check_box = parameter_widget
                    config[parameter_name] = eval(f"{data_type}(check_box.isChecked())")

            with open(fr"addons\{widget}\config.json", 'w') as config_file:
                json.dump(config, config_file, indent=4)

    def apply_func(self):
        self.change_config()

    def cancel_func(self):
        self.set_configs()
        del self.configs

    def ok_func(self):
        self.change_config()
        del self.configs

    def addWidgetIntoSroll(self, widget):
        self.scroll.insertWidget(self.widgets, widget)
        self.widgets += 1

    def setDocumentation(self, documentation_file):
        self.element_documentation.setHtml(markdownToHtml(documentation_file))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.base_widgets), QCoreApplication.translate("Dialog",
                                                                                                        u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0432\u0438\u0434\u0436\u0435\u0442\u044b",
                                                                                                        None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Dialog",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "hr { height: 1px; border-width: 0; }\n"
                                                              "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                              "li.checked::marker { content: \"\\2612\"; }\n"
                                                              "</style></head><body style=\" font-family:'Segoe UI'; font-size:14px; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:700;\">\u0412 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435</span></p>\n"
                                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:700;\"><br /></p>\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                                                              "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u0417\u0434\u0435\u0441\u044c \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u044b\u0445 \u0430\u0434\u0434\u043e\u043d\u043e\u0432(\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u0432\u0438\u0434\u0436\u0435\u0442\u044b \u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b)</span></p></body></html>",
                                                              None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("Dialog", u"\u0410\u0434\u0434\u043e\u043d\u044b", None))
        self.element_documentation.setHtml(QCoreApplication.translate("Dialog",
                                                                      u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                      "p, li { white-space: pre-wrap; }\n"
                                                                      "hr { height: 1px; border-width: 0; }\n"
                                                                      "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                      "li.checked::marker { content: \"\\2612\"; }\n"
                                                                      "</style></head><body style=\" font-family:'Segoe UI'; font-size:14px; font-weight:400; font-style:normal;\">\n"
                                                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:700;\">\u0412 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435</span></p>\n"
                                                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:700;\"><br /></p>\n"
                                                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                                                                      "0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">\u042d\u0442\u043e \u043f\u043e\u043b\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438(\u0431\u0443\u0434\u0435\u0442 \u0433\u043e\u0442\u043e\u0432\u043e \u0432 \u0431\u0435\u0442\u0435)</span></p></body></html>",
                                                                      None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.apply.setText(
            QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi
