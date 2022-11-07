from statistics import mode
from django.db import models
from django.contrib.auth.models import User


# Create your All models here.

# Student User SignUp details start
class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True)
    image = models.FileField()
    gender = models.CharField(max_length=10, null=False)
    usertype = models.CharField(max_length=30, null=False)
    currentdegree = models.CharField(max_length=100)
    previousmarks = models.CharField(max_length=100, blank=True)
    education_level = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    discriotion = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.user.username

# Student User end

# Provider User SignUp details start
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

    
# Provider Add scholarship datails start
class AddScholarship(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    logo = models.FileField()
    startdate = models.DateField()
    enddate = models.DateField()
    noofscholarships = models.IntegerField()
    Location = models.CharField(max_length=256, null=False)
    scholarshiptype =  models.CharField(max_length=100)
    prviousmarks = models.CharField(max_length=100, null=False)
    education_level = models.CharField(max_length=100, null=True)
    discription = models.TextField()
    createdate = models.DateField()
    scholarshipform = models.FileField(blank=True)

    def __str__(self):
        return self.title
    
class ApplyScholarship(models.Model):
    addscholarship = models.ForeignKey(AddScholarship, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    scholarshipform = models.FileField(blank=True)
    applyeddate = models.DateField()




