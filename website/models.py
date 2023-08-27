from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(maxlength=50)
    last_name = models.CharField(maxlength=50)
    email = models.CharField(maxlength=100)
    address = models.CharField(maxlength=10)
    city = models.CharField(maxlength=50)
    state = models.CharField(maxlength=10)
    zipcode = models.CharField(maxlength=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")