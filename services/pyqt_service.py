from PyQt6.QtGui import QFont


class UiService:

    @staticmethod
    def create_font(name: str, size: int, bold: bool, strike_out: bool):
        font = QFont()
        font.setFamily(name)
        font.setPointSize(size)
        font.setBold(bold)
        font.setStrikeOut(strike_out)
        return font
