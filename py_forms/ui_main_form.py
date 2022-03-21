from PyQt6 import QtCore, QtWidgets
from services.ui_service import UiService
from services.system_service import SystemService


class UiMainForm(object):
    def __init__(self, form):
        self.ui_service = UiService()
        self.system_service = SystemService()

        self.central_widget = QtWidgets.QWidget(form)
        self.table = QtWidgets.QTableWidget(self.central_widget)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.button_create_password = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_show_passwords = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.central_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.label_powered = QtWidgets.QLabel(self.horizontalLayoutWidget_2)

    def setup_ui(self, form):
        font = self.ui_service.create_custom_font(self.system_service.get_path_to_font('montserrat_regular.ttf'))
        form.setObjectName("MainForm")
        form.setFixedSize(380, 455)
        form.setFont(font)
        
        self.central_widget.setObjectName("central_widget")

        self.table.setGeometry(QtCore.QRect(10, 60, 360, 300))
        self.table.setHorizontalHeaderLabels(["service", "password"])
        self.table.setStyleSheet("")
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)

        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 360, 360, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.button_create_password.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.button_create_password.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_create_password.setStyleSheet("QPushButton {background-color: #E0FFFF;"
                                                  "border: 2px solid #87CEEB;border-radius: 5px;}"
                                                  "\n"
                                                  "QPushButton:hover {background-color: #ADD8E6;}"
                                                  "\n"
                                                  "QPushButton:pressed {background-color: #00BFFF}")
        self.button_create_password.setObjectName("button_create_password")
        self.horizontalLayout.addWidget(self.button_create_password)

        self.button_show_passwords.setStyleSheet("QPushButton {background-color: #E0FFFF;border: 2px solid #87CEEB;"
                                                 "border-radius: 5px;}"
                                                 "\n"
                                                 "QPushButton:hover {background-color: #ADD8E6;}"
                                                 "\n"
                                                 "QPushButton:pressed {background-color: #00BFFF}")
        self.button_show_passwords.setObjectName("button_show_passwords")
        self.horizontalLayout.addWidget(self.button_show_passwords)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 361, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

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
