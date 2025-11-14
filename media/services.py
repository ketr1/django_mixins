from media.models import Book, AudioBook


class MediaFactory:
    @staticmethod
    def create_media(media_type, **kwargs):
        creators = {
            'book': Book,
            'audiobook': AudioBook,
        }

        media_class = creators.get(media_type)
        if not media_class:
            raise ValueError(f"Неизвестный тип медиа: {media_type}")

        return media_class.objects.create(**kwargs)