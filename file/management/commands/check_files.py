from django.core.management import BaseCommand

from file.tasks import check_files
from file.models import File


class Command(BaseCommand):
    """Ручной запуск проверки файлов"""

    def handle(self, *args, **options):
        check_files()
