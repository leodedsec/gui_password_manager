from PyQt6.QtGui import QFont, QFontDatabase
from services.system_service import SystemService
from traceback import format_exc

_system_service = SystemService()


class UiService:

    @staticmethod
    def create_standard_font(font_name: str, size: int, bold=False) -> QFont:
        assigned_fonts = [font for font in QFontDatabase.families()]
        if {font_name} & {assigned_fonts}:
            font = QFont()
            font.setFamily(font_name)
            font.setPointSize(size)
            font.setBold(bold)
            return font
        else:
            raise ValueError(f"Invalid font with name: {font_name}")

    @staticmethod
    def create_custom_font(path: str, size=12) -> QFont:
        # noinspection PyBroadException
        try:
            _id = QFontDatabase.addApplicationFont(path)
            font = QFont(QFontDatabase.applicationFontFamilies(_id)[0])
            font.setPointSize(size)
            return font
        except Exception:
            _system_service.logger(format_exc())
            raise Exception
