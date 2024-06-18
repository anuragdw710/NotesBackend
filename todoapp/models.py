from django.conf import settings
from django.db import models
from django.contrib import admin

# Create your models here.

class Writer(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone=models.CharField(max_length=20)
    birth_date=models.DateField(null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    @admin.display(ordering='user__username')
    def username(self):
        return self.user.username
    
    @admin.display(ordering='user__email')
    def email(self):
        return self.user.email
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name','user__last_name']

class Note(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    writer= models.ForeignKey(Writer, on_delete=models.PROTECT)

    def __str__(self):
        return self.heading
    
    class Meta:
        ordering = ['-created_at']



