from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=264)

    def __str__(self):
        return self.name

class project(models.Model):
    category=models.ForeignKey(category,related_name='project',on_delete=models.DO_NOTHING)
    No=models.CharField(max_length=264)
    pname=models.CharField(max_length=264)
    cname=models.CharField(max_length=264)

    def __str__(self):
        return self.No

#For enquiry form
class fenquiry(models.Model):
    first_name=models.CharField(max_length=254)
    last_name=models.CharField(max_length=254)
    phone_no=models.IntegerField()
    email_Id=models.EmailField(max_length=254)
    city_name=models.CharField(max_length=254)
    state_name=models.CharField(max_length=254)
    your_enquiry=models.TextField(max_length=254)

    def __str__(self):
        return self.first_name

class fclient(models.Model):
    image=models.ImageField(upload_to='logo/')











