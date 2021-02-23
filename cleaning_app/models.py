from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    user_service_pk = models.ForeignKey('UserService', models.CASCADE, db_column='user_service_pk')
    service_type_pk = models.ForeignKey('ServiceType', models.RESTRICT, db_column='service_type_pk')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    service_pk = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    importance = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'SERVICE'
        unique_together = (('service_pk', 'user_service_pk', 'service_type_pk'),)


class ServiceType(models.Model):
    service_type_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'SERVICE_TYPE'


class UserService(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_service_pk = models.AutoField(primary_key=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    TYPES_OF_USER = [
        (1, 'Частное лицо'),
        (2, 'Клининговое агенство')
    ]
    type = models.SmallIntegerField(choices=TYPES_OF_USER)
    phone = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.last_name

    class Meta:
        db_table = 'USER_SERVICE'
