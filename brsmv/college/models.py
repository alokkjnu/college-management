from django.db import models
from accounts.models import User


# Create your models here.
class College(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    college_id = models.CharField(max_length=50)
    college_name = models.CharField(max_length=250)
    college_logo = models.FileField(blank=True, null=True)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    updated_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.college_id + ", " + self.college_name
