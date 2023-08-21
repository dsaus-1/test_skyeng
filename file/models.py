from django.db import models
from django.utils.translation import gettext as _
import os
import uuid

from user.models import User
from file.validators import validate_file


NULLABLE = {'blank': True, 'null': True}


def get_upload_path(instance, filename):
    return os.path.join('file/%s' % instance.uuid, filename)


class File(models.Model):
    STATUSES = (
        ('new', 'новый'),
        ('updated', 'обновлен')
    )
    STATUS_NEW = 'new'
    STATUS_UPDATED = 'updated'
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    file = models.FileField(upload_to=get_upload_path, max_length=200, verbose_name=_('Файл'), \
        validators=[validate_file])
    downloads_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата загрузки'))
    update_date = models.DateTimeField(auto_now=True, verbose_name=_('Дата последнего обновления'))
    status = models.CharField(default=STATUS_NEW, choices=STATUSES, verbose_name=_('Статус'))
    verified = models.BooleanField(default=False, verbose_name=_('Статус проверки'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('Пользователь'), \
         **NULLABLE)


    def __str__(self):
        return f'{self.file.name}'
