from django.db import models
from accounts.models import User
from college.models import College
from course.models import Course,Subject


# Create your models here.

class Student(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    student_id = models.CharField(max_length=100, unique=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(default=None, blank=True, null=True)
    aadhar = models.IntegerField(blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    post_office = models.CharField(max_length=100, blank=True, null=True)
    police_station = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.IntegerField()
    user = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE, default=0)
    enroll_year = models.DateField(default=None, blank=True, null=True)
    enroll_end_year = models.DateField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id


class StudentDocument(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    student_id = models.ForeignKey(Student, related_name='student', on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aadhar_doc = models.FileField(blank=True, null=True)
    student_photo = models.FileField(blank=True, null=True)
    student_sign = models.FileField(blank=True, null=True)
    student_10th = models.FileField(blank=True, null=True)
    student_12th = models.FileField(blank=True, null=True)
    document1 = models.FileField(blank=True, null=True)
    document2 = models.FileField(blank=True, null=True)
    document3 = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id


class StudentSubject(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE, default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id
