from django.db import models
from college.models import College


# Create your models here.
class Course(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.course_name


class Subject(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    suject_name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.suject_name
