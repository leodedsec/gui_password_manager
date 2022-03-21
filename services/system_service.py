import os


class SystemService:
    root = os.path.abspath(os.path.join(os.getcwd(), "./"))

    @classmethod
    def get_path_to_font(cls, font_name: str) -> str:
        path = os.path.join(cls.root, "ui_source", "fonts", font_name)
        return path

    @classmethod
    def logger(cls, error: str):
        if 'logs.txt' not in os.listdir(cls.root):
            with open(os.path.join(cls.root, 'logs.txt'), 'w') as file:
                file.write(error+"\n\n")
        else:
            with open(os.path.join(cls.root, 'logs.txt'), 'a') as file:
                file.write(error+"\n\n")
