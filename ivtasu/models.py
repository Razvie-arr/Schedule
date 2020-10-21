from django.db import models
from django.utils import timezone
from django.conf import settings



# Create your models here.
class Zanyatia(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название занятия')
    lector = models.CharField(max_length=50, verbose_name='ФИО преподавателя')
    time_start = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Время начала пары')
    time_end = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Время конца пары')

    def __str__(self):
        return "{}\t({}): {}-{}".format(self.name, self.lector, self.time_start, self.time_end)


class Days(models.Model):
    MndSun = [
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье'),
    ]
    spisok = models.ForeignKey(to=Zanyatia, on_delete=models.CASCADE, verbose_name='Предметы')
    day = models.SmallIntegerField(choices=MndSun, verbose_name="День недели")

    def __str__(self):
        return "{}".format(self.spisok.name)
