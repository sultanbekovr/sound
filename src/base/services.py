from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """ Генерация пути для сохранения аватара. format: (media)/avatar/user_id/media.jpg """

    return f'avatart/{instance.id}/{file}'

def validate_size_image(file_obj):
    """Проверка размера файла"""

    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError('Максимальный размер файла 2 мегабайта')


