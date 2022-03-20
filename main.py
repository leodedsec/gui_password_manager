import sys
from PyQt6 import QtWidgets
from ui_templates.ui_main_form import UiMainForm
from ui_templates.ui_create_pass_form import UiCreatePassForm


class PasswordManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(PasswordManager, self).__init__()
        self.main_ui = UiMainForm(self)
        self.main_ui.setup_ui(self)
        self.form_ui = Form()

        self.main_ui.button_create_password.clicked.connect(self.open_create_pass_form)

    def open_create_pass_form(self):
        self.form_ui.show()


class Form(QtWidgets.QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.form_ui = UiCreatePassForm(self)
        self.form_ui.setup_ui(self)


app = QtWidgets.QApplication(sys.argv)
main_app = PasswordManager()
main_app.show()
sys.exit(app.exec())
