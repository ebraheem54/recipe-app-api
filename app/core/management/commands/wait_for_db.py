"""
Django Command to wait for the database to be available.
"""

from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2opError
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """Django Command wait for database ."""

    def handle(self, *args, **options):
        "Entrypoint for command"
        self.stdout.write("waiting for database")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2opError, OperationalError):
                self.stdout.write("database unavailable,waiting 1 second..")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
