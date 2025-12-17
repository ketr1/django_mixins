from django.test import TestCase
from media.models import Book, AudioBook, Movie
from media.services import MediaFactory

class MediaModelTests(TestCase):

    def setUp(self):
        self.book = MediaFactory.create_media(
            'book',
            title='Мастер и Маргарита',
            creator='Булгаков',
            publication_date='1967-01-01',
            isbn='1234567890',
            page_count=480
        )
        self.audiobook = MediaFactory.create_media(
            'audiobook',
            title='Гарри Поттер',
            creator='Роулинг',
            publication_date='2001-01-01',
            narrator='Иванов',
            duration=600
        )
        self.movie = MediaFactory.create_media(
            'movie',
            title='Интерстеллар',
            creator='Нолан',
            publication_date='2014-11-07',
            duration=169,
            format='mp4'
        )

    def test_book_description(self):
        self.assertIn('Книга', self.book.get_description())

    def test_audiobook_download(self):
        result = self.audiobook.download()
        self.assertIn('Загрузка', result)

    def test_borrow_mixin(self):
        result = self.book.borrow('Кэт')
        self.assertIn('успешно', result)

    def test_movie_description(self):
        desc = self.movie.get_description()
        self.assertIn('Фильм', desc)

    def test_movie_play_trailer(self):
        self.assertIn('трейлера', self.movie.play_trailer())
