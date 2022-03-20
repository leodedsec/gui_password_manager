from PyQt6 import QtCore, QtGui, QtWidgets


class UiCreatePassForm(object):
    def __init__(self, form):
        self.main_tab = QtWidgets.QTabWidget(form)

        # Tab 1
        self.tab_1 = QtWidgets.QWidget()
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.label_service_name_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.line_edit_service_name_1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.label_pass_len = QtWidgets.QLabel(self.formLayoutWidget)
        self.line_edit_pass_len = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.label_result = QtWidgets.QLabel(self.formLayoutWidget)
        self.text_edit_result = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.button_generate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_save_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        # Tab 2
        self.tab_2 = QtWidgets.QWidget()
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.label_service_name_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.line_edit_service_name_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.label_password = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.text_edit_password = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.button_save_2 = QtWidgets.QPushButton(self.tab_2)

    def setup_ui(self, form):
        form.setObjectName("CreatePasswordForm")
        form.resize(420, 280)
        form.setStyleSheet("\n"
                           "")
        self.main_tab.setGeometry(QtCore.QRect(10, 10, 401, 261))
        self.main_tab.setObjectName("main_tab")
        self.tab_1.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.tab_1.setObjectName("tab_1")
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 129))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_service_name_1.setFont(font)
        self.label_service_name_1.setObjectName("label_service_name_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_service_name_1)
        self.line_edit_service_name_1.setMaxLength(100)
        self.line_edit_service_name_1.setPlaceholderText("")
        self.line_edit_service_name_1.setObjectName("line_edit_service_name_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_service_name_1)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_pass_len.setFont(font)
        self.label_pass_len.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_pass_len.setObjectName("label_pass_len")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_pass_len)
        self.line_edit_pass_len.setMaxLength(2)
        self.line_edit_pass_len.setObjectName("line_edit_pass_len")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_pass_len)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_result)
        self.text_edit_result.setReadOnly(True)
        self.text_edit_result.setObjectName("text_edit_result")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.text_edit_result)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 150, 381, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.button_generate.setFont(font)
        self.button_generate.setStyleSheet("QPushButton {\n"
                                           "    background-color: #E0FFFF;\n"
                                           "    border: 2px solid #87CEEB;\n"
                                           "    border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "background-color: #ADD8E6;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "background-color: #00BFFF\n"
                                           "}")
        self.button_generate.setObjectName("button_generate")
        self.horizontalLayout.addWidget(self.button_generate)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.button_save_1.setFont(font)
        self.button_save_1.setStyleSheet("QPushButton {\n"
                                         "    background-color: #67f5a9;\n"
                                         "    border: 2px solid #67f5a9;\n"
                                         "    border-radius: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background-color: #66ed6a;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "background-color: #23db29;\n"
                                         "}")
        self.button_save_1.setObjectName("button_save_1")
        self.horizontalLayout.addWidget(self.button_save_1)
        self.main_tab.addTab(self.tab_1, "Generate")
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 371, 111))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_service_name_2.setFont(font)
        self.label_service_name_2.setObjectName("label_service_name_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_service_name_2)
        self.line_edit_service_name_2.setObjectName("line_edit_service_name_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_edit_service_name_2)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_password)
        self.text_edit_password.setObjectName("text_edit_password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.text_edit_password)
        self.button_save_2.setGeometry(QtCore.QRect(10, 130, 186, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_save_2.setFont(font)
        self.button_save_2.setStyleSheet("QPushButton {\n"
                                         "    background-color: #67f5a9;\n"
                                         "    border: 2px solid #67f5a9;\n"
                                         "    border-radius: 5px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background-color: #66ed6a;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "background-color: #23db29;\n"
                                         "}")
        self.button_save_2.setObjectName("button_save_2")
        self.main_tab.addTab(self.tab_2, "SimpleCreate")

        self.retranslate_ui(form)
        self.main_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("FormCreatePassword", "Create Password"))
        self.label_service_name_1.setText(_translate("FormCreatePassword", "Service Name:"))
        self.label_pass_len.setText(_translate("FormCreatePassword", "Password Length:"))
        self.line_edit_pass_len.setPlaceholderText(_translate("FormCreatePassword", "10"))
        self.label_result.setText(_translate("FormCreatePassword", "Result:"))
        self.button_generate.setText(_translate("FormCreatePassword", "Generate"))
        self.button_save_1.setText(_translate("FormCreatePassword", "Save"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.tab_1),
                                 _translate("FormCreatePassword", "Generate"))
        self.label_service_name_2.setText(_translate("FormCreatePassword", "Service Name:"))
        self.label_password.setText(_translate("FormCreatePassword", "Password:"))
        self.button_save_2.setText(_translate("FormCreatePassword", "Save"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.tab_2),
                                 _translate("FormCreatePassword", "SimpleCreate"))
