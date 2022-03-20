from PyQt6 import QtCore, QtGui, QtWidgets


class UiMainForm(object):
    def __init__(self, form):
        self.central_widget = QtWidgets.QWidget(form)
        self.table_information = QtWidgets.QTableWidget(self.central_widget)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.button_create_password = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_show_passwords = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.central_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.label_powered = QtWidgets.QLabel(self.horizontalLayoutWidget_2)

    def setup_ui(self, form):
        form.setObjectName("MainForm")
        form.resize(380, 454)
        form.setStyleSheet("")
        self.central_widget.setObjectName("central_widget")
        self.table_information.setGeometry(QtCore.QRect(10, 60, 360, 300))
        self.table_information.setHorizontalHeaderLabels(["service", "password"])
        self.table_information.setStyleSheet("")
        self.table_information.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table_information.setObjectName("table_information")
        self.table_information.setColumnCount(2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 360, 361, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setStrikeOut(False)
        self.button_create_password.setFont(font)
        self.button_create_password.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.button_create_password.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_create_password.setStyleSheet("QPushButton {\n"
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
        self.button_create_password.setObjectName("button_create_password")
        self.horizontalLayout.addWidget(self.button_create_password)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        self.button_show_passwords.setFont(font)
        self.button_show_passwords.setStyleSheet("QPushButton {\n"
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
        self.button_show_passwords.setObjectName("button_show_passwords")
        self.horizontalLayout.addWidget(self.button_show_passwords)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 361, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(13)
        self.label_powered.setFont(font)
        self.label_powered.setStyleSheet("background-color: rgb(255, 216, 19);\n"
                                         "border-radius: 5px;")
        self.label_powered.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_powered.setObjectName("label_powered")
        self.horizontalLayout_2.addWidget(self.label_powered)
        form.setCentralWidget(self.central_widget)

        self.retranslate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Password Manager"))
        self.button_create_password.setText(_translate("form", "Create Password"))
        self.button_show_passwords.setText(_translate("form", "Show Passwords"))
        self.label_powered.setText(_translate("form", "Your passwords:"))
