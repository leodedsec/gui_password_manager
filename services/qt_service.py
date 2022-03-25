from typing import Union
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtWidgets import QMessageBox
from services.system_service import SystemService


class QtService:

    @staticmethod
    @SystemService.logger
    def create_standard_font(font_name: str, size: int, bold=False) -> QFont:
        font = QFont()
        font.setFamily(font_name)
        font.setPointSize(size)
        font.setBold(bold)
        return font

    @staticmethod
    @SystemService.logger
    def create_custom_font(path: str, size=12) -> QFont:
        _id = QFontDatabase.addApplicationFont(path)
        font = QFont(QFontDatabase.applicationFontFamilies(_id)[0])
        font.setPointSize(size)
        return font

    @staticmethod
    @SystemService.logger
    def create_message_box(message: str, path_to_icon: Union[str, None] = None):
        message_box = QMessageBox()
        if path_to_icon is not None:
            message_box.setWindowIcon(QIcon(path_to_icon))
        message_box.setWindowTitle('Notification')
        message_box.setIcon(QMessageBox.Icon.Information)
        message_box.setText(message)
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        message_box.exec()
        return message_box


