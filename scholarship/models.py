from django.db import models
from django.contrib.auth.models import User

# Create your All models here.

# Student User start
class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True)
    image = models.FileField()
    gender = models.CharField(max_length=10, null=False)
    usertype = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.user.username

# Student User end

# Provider User start
class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12, null=False)
    image = models.FileField()
    gender = models.CharField(max_length=10, null=False)
    companyname = models.CharField(max_length=50, null=False)
    usertype = models.CharField(max_length=30, null=False)
    status = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.user.username
# Provider User end

    


# Student User end

