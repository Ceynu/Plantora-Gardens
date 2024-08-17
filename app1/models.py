from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='stdnt')

    def __str__(self):
        return self.name

class teacher(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tchr')

    def __str__(self):
        return self.name

class complaint(models.Model):
    s_name = models.ForeignKey(student, on_delete=models.CASCADE)
    t_name = models.ForeignKey(teacher, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    submitted_date = date.today()

    def __str__(self):
        return f"{self.s_name} complainted about {self.t_name}"
    
class complaints(models.Model):
    s_name = models.ForeignKey(student, on_delete=models.CASCADE)
    t_name = models.ForeignKey(teacher, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    submitted_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.s_name} complained about {self.t_name}"
    
class reply(models.Model):
    s_name = models.ForeignKey(complaints, on_delete=models.CASCADE,related_name='replyto')
    t_name = models.ForeignKey(complaints, on_delete=models.CASCADE,related_name='replyby')
    message = models.TextField()

    def __str__(self):
        return f"{self.t_name} replied to {self.s_name}"



   