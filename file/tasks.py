from file.services import check_file_pep8, send_message
from file.models import File

from celery import shared_task


@shared_task
def check_files():
    """
    Совершает проверку всех новых или обновленных файлов на PEP8,
    меняет статус проверки и вызывает функцию отправки сообщения

    """
    files = File.objects.filter(verified=False)
    for file_obj in files:
        statistics = check_file_pep8(file_obj)
        
        file_obj.verified = True
        file_obj.save()

        send_message(file_obj, statistics)




    