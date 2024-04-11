from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Manager(models.Model):
    full_name = models.TextField(max_length=150, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name="номер")
    email = models.EmailField(verbose_name='почта')
    temporary_password = models.CharField(max_length=20, verbose_name='временный пароль')

    def __str__(self):
        return self.full_name


class Apartment(models.Model):
    STATUS_CHOICES = (
        ('Активно', 'Активно'),
        ('Бронь', 'Бронь'),
        ('Куплено', 'Куплено'),
        ('Рассрочка', 'Рассрочка'),
        ('Бартер', 'Бартер'),
    )
    floor = models.IntegerField(verbose_name='Этаж')
    object_name = models.CharField(max_length=100, verbose_name='Объект')
    square_meters = models.FloatField(verbose_name='Кв м квартиры')
    date = models.DateField(verbose_name='Дата')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True, blank=True, related_name='client')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Активно')

    def __str__(self):
        return f"Apartment {self.id} --- {self.status} --- {self.client}"


class Client(models.Model):
    STATUS_CHOICES = (
        ('Активно', 'Активно'),
        ('Бронь', 'Бронь'),
        ('Куплено', 'Куплено'),
        ('Рассрочка', 'Рассрочка'),
        ('Бартер', 'Бартер'),
    )
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    contract_number = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateField(verbose_name='Дата')
    apartment = models.OneToOneField(Apartment, on_delete=models.CASCADE, related_name='apartment', default=None)

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=Client)
def update_apartment_status(sender, instance, **kwargs):
    if instance.apartment:
        instance.apartment.status = instance.status
        instance.apartment.save()


@receiver(post_save, sender=Client)
def update_apartment_client(sender, instance, **kwargs):
    if instance.apartment:
        instance.apartment.client = instance
        instance.apartment.save()


class Review(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='reviews')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField(max_length=500)
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f"Review for Apartment {self.apartment.id} by {self.manager.full_name}"