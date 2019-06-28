from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ['top_name']

class WebPage(models.Model):
    category = models.ForeignKey('Topic', on_delete = models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=264, unique=True, verbose_name="Имя страницы")
    url = models.URLField(unique=True, verbose_name="Ссылка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Страницы"
        verbose_name = "Страница"
        ordering = ['name']

class AccessRecord(models.Model):
    name = models.ForeignKey('WebPage', on_delete = models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)

class User(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    