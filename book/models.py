from django.db import models
from decimal import Decimal
from django.core.validators import MinLengthValidator, MinValueValidator
from django.contrib.auth.models import User


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthorModel(Common):
    first_name = models.CharField(max_length=64, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=64, validators=[MinLengthValidator(3)])
    age = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class BookModel(Common):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10,
                                validators=[MinValueValidator(Decimal('0.55'))])

    HARD = 'hard'
    SOFT = 'soft'

    CHOICES = (
        (HARD, 'Hard'),
        (SOFT, 'Soft'),
    )
    cover = models.CharField(max_length=64, choices=CHOICES, default=SOFT)

    author = models.ForeignKey(AuthorModel, related_name='book',
                               on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class CommentModel(Common):
    title = models.CharField(max_length=255)
    text = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
