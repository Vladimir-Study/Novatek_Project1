from django.db import models
from django.urls import reverse
from datetime import date


class Parameters(models.Model):
    OT_in_day = models.IntegerField(verbose_name='Наработка за сутки')
    max_power = models.IntegerField(verbose_name='Максимальная нагрузка', blank=True, null=True)
    max_temperature = models.FloatField(verbose_name='Максимальная температура', blank=True, null=True)
    duty_officer = models.CharField(max_length=255, verbose_name='Оперативный дежурный ФИО')
    volume_oil = models.IntegerField(verbose_name='Уровень масла')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    time_work = models.DateTimeField(verbose_name='Дата')
    journal = models.TextField(max_length=500, verbose_name='Произведенные работы', blank=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Фото', blank=True)
    status = models.CharField(max_length=50, verbose_name='Статус', null=True)
    TO = models.BooleanField(default=False, verbose_name='Техническое обслуживание')
    engine = models.ForeignKey('Engine', on_delete=models.PROTECT, verbose_name='Двигатель', related_name='engine')
    station = models.ForeignKey('Station', on_delete=models.PROTECT, verbose_name='Станция', null=True)

    def __str__(self):
        return 'Параметры ' + str(self.engine)

    class Meta:
        verbose_name = 'Параметры'
        verbose_name_plural = 'Параметры'
        ordering = ['-time_create']

    def get_absolute_url(self):
        return reverse('station', kwargs={'station_id': self.station.pk})


class DateCheck(models.Model):
    title = models.CharField(max_length=255, verbose_name='Описание', null=True)
    date_installation = models.DateTimeField(verbose_name='Дата монтажа', blank=True, null=True)
    date_unistall = models.DateTimeField(verbose_name='Дата демонтажа', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Дата'
        verbose_name_plural = 'Даты'
        ordering = ['id']


class gas_par(models.Model):
    consumption_gas = models.IntegerField(verbose_name='Расход газа', blank=True, default=0)
    gas_temperature = models.FloatField(verbose_name='Температура газа', blank=True, default=0)
    station = models.ForeignKey('Station', verbose_name='Станция', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Потребление газа'
        verbose_name_plural = 'Потребление газа'
        ordering = ['id']

    def __str__(self):
        return 'Потребление газа'


class EnergyGenerate(models.Model):
    power_active = models.FloatField(verbose_name='Активная мощность', blank=True, default=0)
    power_react = models.FloatField(verbose_name='Реактивная мощность', blank=True, default=0)
    station = models.ForeignKey('Station', verbose_name='Станция', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Выработка электроэнергии'
        verbose_name_plural = 'Выработка электроэнергии'
        ordering = ['id']

    def __str__(self):
        return 'Выработка электроэнергии'


class Engine(models.Model):
    engine_number = models.CharField(max_length=50, verbose_name='Номер двигателя')
    date_check = models.ForeignKey('DateCheck', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'
        ordering = ['id']

    def __str__(self):
        return 'Двигатель ' + self.engine_number

    def get_absolute_url(self):
        return reverse('engine', kwargs={'engine_id': self.pk})


class Station(models.Model):
    station_number = models.CharField(max_length=50, verbose_name='Номер станции')
    date_check = models.ForeignKey('DateCheck', on_delete=models.PROTECT, verbose_name='Дата')

    def __str__(self):
        return self.station_number

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('station', kwargs={'station_id': self.pk})
