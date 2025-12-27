from daphne.cli import CommandLineInterface
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run Daphne ASGI server"

    def handle(self, *args, **options):
        cli = CommandLineInterface()
        cli.run(["-b", "0.0.0.0", "-p", "8000", "study.conf.asgi:application"])
