from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    pages_number = models.IntegerField('Страницы', default=100)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = "Книги"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.book}, {self.user}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = "Отзывы"