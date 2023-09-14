from django.db import models
from accounts.models import User
from college.models import College


# Create your models here.
class Faculty(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    faculty_id = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=20, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(default=None, blank=True, null=True)
    aadhar = models.IntegerField(blank=True, null=True)
    pan = models.CharField(max_length=12, blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    post_office = models.CharField(max_length=100, blank=True, null=True)
    police_station = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.faculty_id


class FacultySpecialization(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    # subject =
