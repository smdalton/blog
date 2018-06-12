from techblog import models
from django.core.management.base import BaseCommand
import os




class Command(BaseCommand):

    def __init__(self):
        self.migrations_path = os.path.join(os.getcwd(), '/techblog/migrations')
        self.sqlite_path = os.path.join(os.getcwd(), '/sqlite3.db')

    def delete_sqlite(self):
        print(self.sqlite_path)

    def delete_migrations(self):
        print(self.migrations_path)

    def handle(self, **args):
        self.delete_sqlite()
        self.delete_migrations()

