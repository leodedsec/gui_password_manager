from peewee import SqliteDatabase, Model, CharField

my_database = SqliteDatabase('passwords.db')


class PasswordModel(Model):
    service = CharField(max_length=100)
    password = CharField(max_length=500)

    class Meta:
        database = my_database
        table_name = 'passwords'

    def __str__(self):
        return self.service
