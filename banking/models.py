from django.db import models
from django.utils import timezone
import random
import string


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО клиента')
    citizenship = models.CharField(max_length=20, default='Кыргызстан', verbose_name='гражданство')
    birth_year = models.DateField(verbose_name='год рождения',)
    work_place = models.CharField(max_length=30, verbose_name='место работы')
    update_date = models.DateField(default=timezone.now, verbose_name='дата последнего обновления')

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.CharField(max_length=16, null=False, verbose_name='номер аккаунта')
    account_type = models.IntegerField(default=1, null=False, verbose_name='тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='clients')

    class Meta:
        db_table = 'Account'
        verbose_name = 'счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return self.number


class Credit(models.Model):
    sum = models.IntegerField(verbose_name='сумма кредита')
    date = models.DateField(default=timezone.now, verbose_name='дата получения кредита')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        db_table = 'Credit'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'

    def __str__(self):
        return self.sum


def id_generator(size=16, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))