# media/services.py

from media.models import Book, AudioBook, Movie


class MediaFactory:
    @staticmethod
    def get_all_media_types():
        """Возвращает список всех типов медиа"""
        return ['book', 'audiobook', 'movie']

    @staticmethod
    def get_media_class(media_type):
        """Возвращает соответствующий класс модели по типу"""
        creators = {
            'book': Book,
            'audiobook': AudioBook,
            'movie': Movie,
        }
        return creators.get(media_type)

    @staticmethod
    def create_media(media_type, **kwargs):
        """Создает объект нужного медиа-класса"""
        media_class = MediaFactory.get_media_class(media_type)
        if not media_class:
            raise ValueError(f"Неизвестный тип медиа: {media_type}")
        return media_class.objects.create(**kwargs)
