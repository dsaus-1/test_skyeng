import pycodestyle
import sys
import logging
from io import StringIO
from datetime import datetime

from django.template.loader import render_to_string
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER, BASE_DIR


logger = logging.getLogger(__name__)

def check_file_pep8(file):
    """
    Принимает объект File, проводит проверку на pep8 и отдает ошибки по файлу
    """

    sys.stdout = StringIO()

    checker = pycodestyle.StyleGuide(quiet=False)
    checker.check_files([f'{BASE_DIR}/media/{file.file.name}', ])

    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__

    errors = []
    for line in output.split('\n'):
        parts = line.split(' ', 2)
        if len(parts) == 3:
            location, error, desc = parts
            line_no = location.split(':')[1]
            errors.append('%s ln:%s %s' % (error, line_no, desc))

    return errors


def send_message(file, statistics):
    """
    Принимает объект File и статистику проверки по файлу, 
    отправляет статистику по email и записывает лог 
    """

    filename = file.file.name.split('/')[-1]

    if not statistics:
        statistics = ['Ошибок не обнаружено']

    msg = render_to_string(f'{BASE_DIR}/file/templates/file/message.txt', \
        {'statistics': statistics, 'filename': filename})

    try:

        send_mail(
                    subject=f'Проверка по файлу {filename}',
                    message=msg,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[file.user.email],
                    fail_silently=False,
                )
        logger.info({'file': file.uuid, 'statistics': statistics, \
             'send_mail': True, 'user': file.user.id})
    except:
        logger.info({'file': file.uuid, 'statistics': statistics, \
             'send_mail': False, 'user': file.user.id})
