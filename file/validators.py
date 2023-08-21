from django.core.exceptions import ValidationError


def validate_file(value):
    if not value.name.endswith('.py'):

     raise ValidationError('Можно загрузить файл только в расширение ".py"')
