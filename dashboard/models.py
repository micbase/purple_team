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


class Class(models.Model):
    class_name = models.CharField(
        max_length=150,
        default='',
        blank=False,
    )
	professor_firstname = models.CharField(
		max_length=50,
		default='',
		blank=True,
	)
	professor_lastname = models.CharField(
		max_length = 50,
		default = '',
		blank = True,
	)
    class_time = models.CharField(
		max_length = 20,
		default = '',
		blank = False,
	)
	
	manager = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)  

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Classes'


class Topic(models.Model):
	topic_title = models.CharField(
        max_length=150,
        default='',
        blank=False,
    )
	topic_content = models.CharField(
        max_length=500,
        default='',
        blank=False,
    )

    topic_author = models.ForeignKey(User)
    class_id = models.ForeignKey(Class)  #class is a resevered word, so I made it class_id   
    
	# status=models. PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True) 
    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Topics'

class Post(models.Model):
	post_content = models.CharField(
        max_length=500,
        default='',
        blank=False,
    )

    post_author = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)


    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True) 

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Posts'

     
