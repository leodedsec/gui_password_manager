import sys
from peewee import Model
from typing import Union
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QLineEdit, QTextEdit, QTableWidgetItem
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt, QEvent, QObject
from source.forms.main_form import UiMainForm
from source.forms.create_pass_form import UiCreatePassForm
from source.models.models import PasswordModel, my_database
from services.system_service import SystemService
from services.qt_service import QtService


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.main_form = UiMainForm(self)
        self.main_form.setup_ui(self)

        self.current_item = None

        self.create_pass_form = CreatePassForm()
        self.create_pass_form_init = self.create_pass_form.main_form

        self.my_database = my_database
        self.my_database.connect()

        SystemService().hide_db(SystemService.get_path_to_db(self.my_database.database))

        self.local_saved_model = []

        self.main_form.button_create_password.clicked.connect(lambda: self.open_create_pass_form())
        self.main_form.button_show_passwords.clicked.connect(lambda: self.show_passwords(table=PasswordModel))
        self.create_pass_form_init.button_save_2.clicked.connect(lambda: self.notification_or_save(
            self.create_pass_form_init.line_edit_service_name_2, self.create_pass_form_init.text_edit_password))

        self.create_pass_form_init.button_save_1.clicked.connect(lambda: self.notification_or_save(
            self.create_pass_form_init.line_edit_service_name_1, self.create_pass_form_init.text_edit_result))

        self.create_pass_form_init.button_generate.clicked.connect(lambda: self.generate_password())
        self.main_form.table.viewport().installEventFilter(self)

    @SystemService.logger
    def open_create_pass_form(self):
        self.create_pass_form.show()

    @SystemService.logger
    def generate_password(self):
        line_edit_pass_len = self.create_pass_form_init.line_edit_pass_len
        if len(line_edit_pass_len.text()) == 0:
            length_password = int(line_edit_pass_len.placeholderText())
        else:
            length_password = int(line_edit_pass_len.text())
        password = SystemService.generate_password(length_password)

        text_edit_result = self.create_pass_form_init.text_edit_result
        text_edit_result.setText('')
        text_edit_result.setText(password)

    @SystemService.logger
    def notification_or_save(self, service_input: QLineEdit, password_input: Union[QTextEdit]):
        if len(service_input.text()) == 0 or len(password_input.toPlainText()) < 8:
            QtService.create_message_box(message='1) Service name must be inputted\n2) Length password must be >=8',
                                         path_to_icon=SystemService.get_path_to_icon('main_icon.png'))

        elif len(service_input.text()) != 0 and len(password_input.toPlainText()) >= 8:
            SystemService().get_or_create_table(database=self.my_database, table=PasswordModel)
            PasswordModel.create(service=service_input.text(),
                                 password=SystemService().simple_encode_password(password_input.toPlainText()))
            self.create_pass_form.close()
            self.show_passwords(PasswordModel)

    @SystemService.logger
    def show_passwords(self, table: Model):
        passwords: [PasswordModel] = [i for i in table.select().order_by(PasswordModel.id)]
        self.local_saved_model = [i.service for i in passwords]
        self.main_form.table.setRowCount(len(passwords))
        for row, field in enumerate(passwords, start=0):
            self.main_form.table.setItem(row, 0, QTableWidgetItem(field.service))
            self.main_form.table.setItem(row, 1, QTableWidgetItem(SystemService.simple_decode_password(field.password)))

    @SystemService.logger
    def clicked_to_table_item(self):
        item = self.main_form.table.currentItem()
        row, column = item.row(), item.column()
        if column == 0:  # edit service name
            service = item.text()
            if len(service) != 0:
                SystemService().check_upd_db(service=service, saved_value=self.local_saved_model[row])
                self.show_passwords(PasswordModel)
            else:
                QtService.create_message_box(message='The length of the service must be >= 1',
                                             path_to_icon=SystemService.get_path_to_icon('main_icon.png'))
        elif column == 1:  # edit password
            service = self.main_form.table.item(row, column - 1).text()
            password = item.text()
            if len(password) >= 8:
                SystemService().check_upd_db(service=service, password=password)
                self.show_passwords(PasswordModel)
            else:
                QtService.create_message_box(message='The length of the password must be >= 8',
                                             path_to_icon=SystemService.get_path_to_icon('main_icon.png'))

    @SystemService.logger
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        elif event.key() == Qt.Key.Key_Return:
            self.clicked_to_table_item()

    @SystemService.logger
    def eventFilter(self, source: QObject, event: QEvent):
        if event.type() == QEvent.Type.MouseButtonDblClick and source is self.main_form.table.viewport():
            position = event.position()
            item = self.main_form.table.itemAt(int(position.x()), int(position.y()))
            if item is not None:
                self.current_item = item
        return super(MainForm, self).eventFilter(source, event)


class CreatePassForm(QWidget):
    def __init__(self):
        super(CreatePassForm, self).__init__()
        self.main_form = UiCreatePassForm(self)
        self.main_form.setup_ui(self)


app = QApplication(sys.argv)
main_app = MainForm()
main_app.show()
sys.exit(app.exec())
