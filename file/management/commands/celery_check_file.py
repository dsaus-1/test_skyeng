from datetime import datetime, timedelta

from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from config import settings


class Command(BaseCommand):
    """Создание задачи на проверку файлов"""

    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=2,
            period=IntervalSchedule.MINUTES,
        )


        PeriodicTask.objects.create(
            interval=schedule,  # we created this above.
            name='Check files',  # simply describes this periodic task.
            task='file.tasks.check_files',  # name of task.
            expires=datetime.now() + timedelta(days=1)
        )