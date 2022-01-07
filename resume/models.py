from django.db import models


class ProgrammingLanguages(models.Model):
    PROGRESS = (
        (None, 'Выберите урвоень навыка'),
        (1, 'intern'),
        (2, 'junior'),
        (3, 'middle'),
        (4, 'senior'),
        # (5, 'intern'),
        # (6, 'intern'),
    )

    title = models.CharField(max_length=20, primary_key=True, verbose_name='Язык')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    process = models.SmallIntegerField(null=True, blank=True, verbose_name='Процесс')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Знания'
        verbose_name = 'Знание'
        ordering = ['-title']


