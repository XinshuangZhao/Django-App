from django.db import models
from django.utils import timezone
from django.conf import settings

class Employee(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    points_remain = models.IntegerField(default=0)
    points_received = models.IntegerField(default=0)
    user_em = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Giftcard(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    redeem_date = models.DateTimeField('date redeemed')
    def redeem(self):
        self.redeem_date = timezone.now()
        self.save()


class Transfer(models.Model):
    giver = models.CharField(max_length=200)
    receiver = models.ForeignKey(Employee, on_delete=models.CASCADE)
    points_given = models.IntegerField(default=0)
    message = models.TextField()
    give_date = models.DateTimeField('date of giving')
    def give(self):
        self.give_date = timezone.now()
        self.save()

