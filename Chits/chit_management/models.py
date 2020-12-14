from django.db import models
from datetime import *
# Create your models here.

class KycPanCard(models.Model):

    front = models.ImageField(upload_to='Pan/%Y/%m/%d/', null=False, max_length=255)
    back = models.ImageField(upload_to='Pan/%Y/%m/%d/', null=False, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['front', 'back']

    def __str__(self):
        return self.front, self.back

class KycAadharCard(models.Model):

    front = models.ImageField(upload_to='Aadhar/%Y/%m/%d/', null=False, max_length=255)
    back = models.ImageField(upload_to='Aadhar/%Y/%m/%d/', null=False, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['front', 'back']

    def __str__(self):
        return self.front, self.back

class KycAddress(models.Model):

    address = models.FileField(upload_to='Address/%Y/%m/%d/', null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['address']

    def __str__(self):
        return self.address

class KycBank(models.Model):

    statement = models.FileField(upload_to='Bank_statement/%Y/%m/%d/', null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['statement']

    def __str__(self):
        return self.statement



