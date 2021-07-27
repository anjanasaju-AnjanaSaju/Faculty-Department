from django.db import models

# Create your models here.
class FacDepartment(models.Model):
    IT=models.CharField(max_length=20)
    Mechanical=models.CharField(max_length=20)
    Electrical=models.CharField(max_length=20)
    Teachers=models.CharField(max_length=20)



    def __str__(self):
        return self.IT
