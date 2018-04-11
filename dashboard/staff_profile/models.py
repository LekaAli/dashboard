from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    RACE_OPTIONS = (
        ('A', 'African'),
        ('W', 'White'),
        ('I', 'Indian'),
        ('C', 'Coloured'),
        ('O', 'Others'),
    )
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.ForeignKey(User, related_name='employee', blank=True, null=True, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=13, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    physical_address = models.CharField(max_length=200, blank=True, null=True)
    tax_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    personal_email = models.EmailField(blank=True, null=True)
    github_user = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, blank=True, null=True)
    race = models.CharField(max_length=1, choices=RACE_OPTIONS, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['-id']

    def __unicode__(self):
        return '%s' % self.user

    @models.permalink
    def get_absolute_url(self):
        return ''

