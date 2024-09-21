from django.contrib import admin
from book.models import AuthorModel, BookModel, CommentModel
# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.register(CommentModel)
