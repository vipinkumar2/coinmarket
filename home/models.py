from django.db import models

# Create your models here.


class user_details(models.Model):
    STATUS = (
        ("ACTIVE", "ACTIVE"),
        ("NOT_ACTIVE", "NOT_ACTIVE"),
        ("BANNED","BANNED"),
        ("DELETED","DELETED"),
        )
    username = models.CharField(max_length=255,default='')
    email = models.CharField(max_length=255,default='')
    password = models.CharField(max_length=255,default='')
    profile_name = models.IntegerField(default=0)
    status = models.CharField(max_length=255,choices=STATUS,default='NOT_ACTIVE')
    profile_updated = models.BooleanField(default=False,null=True,blank=True)
    total_commented = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self) :
        return str(self.profile_name)

class comments(models.Model):
    
    user = models.ForeignKey(to=user_details,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self) :
        return str(f'{self.user} commented {self.comment} at : {self.created_at}')
