from django.db import models
import uuid
from django.urls import reverse


# Create your models here.

class Referral(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=120, unique=False, verbose_name="Name")
    Surname = models.CharField(max_length=120, unique=False, verbose_name="Surname")
    PolicyNumber = models.CharField(max_length=10, unique=False, verbose_name="Policy")
    Email = models.CharField(max_length=150, unique=False, verbose_name="Email")
    BrokerName = models.CharField(max_length=100, unique=False, verbose_name="Broker")
    BrokerEmail = models.CharField(max_length=150, unique=False, verbose_name="BrokerEmail")
    PolicyPhone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PolicyNumber

    def get_absolute_url(self):  # new
        return reverse('referral_detail', args=[str(self.id)])


class Referred(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=120, unique=False, verbose_name="Name")
    Surname = models.CharField(max_length=120, unique=False, verbose_name="Surname")
    Email = models.CharField(max_length=150, unique=False, verbose_name="Email")
    RefferedPhone = models.IntegerField()
    Status = models.CharField(max_length=20,
                              choices=[('PENDING', 'Pending'), ('ACTIVATED', 'Activated'), ('CLOSED', 'Closed')])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FirstName

    def get_absolute_url(self):  # new
        return reverse('index')

