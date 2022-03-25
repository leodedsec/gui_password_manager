import os
import random
import base64
import subprocess
from typing import Callable, Union
from traceback import format_exc
from string import ascii_letters, punctuation
from peewee import Model, SqliteDatabase
from source.models.models import PasswordModel

ROOT = os.path.abspath(os.path.join(os.getcwd(), "./"))


class SystemService:

    @staticmethod
    def get_path_to_font(font_name: str) -> str:
        """Get path to font"""
        path = os.path.join(ROOT, "style", "fonts", font_name)
        return path

    @staticmethod
    def get_path_to_icon(icon_name: str) -> str:
        """Get path to icon"""
        path = os.path.join(ROOT, "style", "icons", icon_name)
        return path

    @staticmethod
    def get_path_to_db(db_name: str) -> str:
        """Get path to database"""
        path = os.path.join(ROOT, db_name)
        return path

    @staticmethod
    def get_css_file(css_name: str) -> str:
        """Get css file"""
        path = os.path.join(ROOT, "style", "css", css_name)
        with open(path, "r") as file:
            return file.read()

    @staticmethod
    def logger(func: Callable):
        """Custom decorator for write errors to logs"""
        def wrapper(*args, **kwargs):
            # noinspection PyBroadException
            try:
                return func(*args, **kwargs)
            except Exception:
                error = format_exc()
                if 'logs.txt' not in os.listdir(ROOT):
                    with open(os.path.join(ROOT, 'logs.txt'), 'w') as file:
                        file.write(error + "\n\n")
                else:
                    with open(os.path.join(ROOT, 'logs.txt'), 'a') as file:
                        file.write(error + "\n\n")

        return wrapper

    @staticmethod
    def generate_password(length=10) -> str:
        """Generate password"""
        numbers = list(map(str, range(10)))
        alphabet = list(ascii_letters)
        symbols = list(punctuation)

        result = numbers + alphabet + symbols
        random.shuffle(result)

        password = "".join([random.choice(result) for _ in range(length)])
        return password

    def simple_encode_password(self, password: str) -> str:
        """Encode password"""
        return base64.b64encode(password.encode('ascii')).decode('ascii')

    @staticmethod
    def simple_decode_password(password: str) -> str:
        """Decode password"""
        return base64.b64decode(password.encode('ascii')).decode('ascii')

    def get_or_create_table(self, database: SqliteDatabase, table: Model):
        """Get or create table"""
        all_tables = database.get_tables()
        if table._meta.table_name not in all_tables:
            table.create_table()

    def check_upd_db(self, service, password: Union[None, str] = None, saved_value=None):
        """Check values to update"""
        if saved_value is None:  # edit password
            field: Union[PasswordModel, None] = PasswordModel.get_or_none(PasswordModel.service == service)
            if field is not None and password is not None:
                field.password = self.simple_encode_password(password)
                field.save()
        else:  # edit service name
            field: Union[PasswordModel, None] = PasswordModel.get_or_none(
                PasswordModel.service == saved_value)
            if field is not None:
                field.service = service
                field.save()

    def hide_db(self, path_to_db: str):
        """Hide database"""
        subprocess.call(['attrib', '+h', '+s', path_to_db])
