class BorrowableMixin:
    def borrow(self, user):
        self.is_borrowed = True
        self.borrowed_by = user
        self.save()
        return f"{self.title} взято в аренду пользователем {user}"

class DownloadableMixin:
    def download(self):
        return f"Скачивание {self.title} началось..."

class ReviewableMixin:
    def add_review(self, review_text, rating):
        self.reviews.create(text=review_text, rating=rating)
        return "Отзыв добавлен"