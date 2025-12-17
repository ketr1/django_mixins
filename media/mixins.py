from datetime import datetime

class BorrowableMixin:
    """Миксин для объектов, которые можно взять в аренду."""
    def borrow(self, user):
        if getattr(self, "is_borrowed", False):
            return f"'{self.title}' уже находится у {self.borrowed_by}"
        self.is_borrowed = True
        self.borrowed_by = user
        self.save()
        return f"'{self.title}' успешно взято пользователем {user}"

    def return_item(self):
        if not getattr(self, "is_borrowed", False):
            return f"'{self.title}' не было в аренде"
        user = self.borrowed_by
        self.is_borrowed = False
        self.borrowed_by = ""
        self.save()
        return f"'{self.title}' возвращено пользователем {user}'"


class DownloadableMixin:
    """Миксин для скачиваемых объектов."""
    def download(self):
        return f"Загрузка {self.get_media_type()} '{self.title}' начата ({datetime.now().strftime('%H:%M:%S')})"


class ReviewableMixin:
    """Миксин для добавления отзывов (реализован базово для совместимости)."""
    reviews = []

    def add_review(self, user, text, rating):
        review = {
            "user": user,
            "text": text,
            "rating": rating,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.reviews.append(review)
        return f"Отзыв от {user} добавлен: {text}"

    def get_reviews(self):
        return self.reviews

class StreamableMixin:
    """Миксин для онлайн-просмотра фильмов."""
    def stream(self):
        return f"Воспроизведение онлайн фильма '{self.title}' начато"