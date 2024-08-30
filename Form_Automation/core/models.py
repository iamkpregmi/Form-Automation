from django.db import models

class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=5)
    student_name = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    fee = models.DecimalField(max_digits=9, decimal_places=2)

    
