from django.db import models



class Movies(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название фильма")
    plot = models.TextField(blank=True, verbose_name="Сюжет")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title


class Category(models.Model):
    title_cat = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.title_cat
