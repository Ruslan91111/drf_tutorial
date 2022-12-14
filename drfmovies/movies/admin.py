from django.contrib import admin
from .models import Movies, Category


admin.site.register(Movies)
admin.site.register(Category)