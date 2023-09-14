from django.db import models
from accounts.models import User
from college.models import College


# Create your models here.
class Blog(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    blog_title = models.CharField(max_length=250)
    blog_text = models.TextField()
    blog_image = models.ImageField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, default=0)
    college = models.ForeignKey(College, on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return str(self.id) + " " + self.blog_title
