from django.db import models
from django.utils import timezone

class Employee(models.Model):
    name = models.CharField(max_length=200)
    points_remain = models.IntegerField(default=0)
    points_received = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Giftcard(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    redeem_date = models.DateTimeField('date redeemed')
    def redeem(self):
        self.redeem_date = timezone.now()
        self.save()
    def __str__(self):
        return (self.employee, self.amount, self.redeem_date)

class Transfer(models.Model):
    giver = models.CharField(max_length=200)
    receiver = models.ForeignKey(Employee, on_delete=models.CASCADE)
    points_given = models.IntegerField(default=0)
    message = models.TextField()
    give_date = models.DateTimeField('date of giving')
    def give(self):
        self.give_date = timezone.now()
        self.save()

