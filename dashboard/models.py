from django.db import models


# Create your models here.


class User(models.Model):
    email = models.EmailField(
        max_length=100,
        default='',
        blank=False,
    )
    password = models.CharField(
        max_length=50,
        default='',
        blank=False,
    )
    first_name = models.CharField(
        max_length=50,
        default='',
        blank=False,
    )
    last_name = models.CharField(
        max_length=50,
        default='',
        blank=False,
    )
    phonenumber = models.CharField(
        max_length=15,
        default='',
        blank=False,
    )
    bio = models.CharField(
        max_length=500,
        default='',
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)  

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'Users'


class Group(models.Model):
    group_name = models.CharField(
        max_length=150,
        default='',
        blank=False,
    )
    description = models.CharField(
        max_length=400,
        default='',
        blank=True,
    )    
    manager = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)  

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Groups'


class Membership(models.Model):

    member = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    status=models. PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True) 
    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Memberships'

class Event(models.Model):

    group = models.ForeignKey(Group)
    event_name = models.CharField(
        max_length=250,
        default='',
        blank=False,
    )    
    #dateAdded=models.DateField(blank=True )
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True) 

    location=models.CharField(
        max_length=50,
        default='',
        blank=False)
    status=models. PositiveSmallIntegerField(default=1)
    details = models.CharField(
        max_length=800,
        default='',
        blank=True,
    ) 

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Events'

     
