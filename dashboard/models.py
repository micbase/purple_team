from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(
        max_length=50,
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
        max_length=150,
        default='',
        blank=True,
    )

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'Users'


class Skill(models.Model):
    skill_name = models.CharField(
        max_length=50,
        default='',
        blank=False,
    )

    def __unicode__(self):
        return self.skill_name

    class Meta:
        db_table = 'Skills'


class Strength(models.Model):

    uid = models.ForeignKey(User)
    skill_id = models.ForeignKey(Skill)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Strengths'


class Weakness(models.Model):

    uid = models.ForeignKey(User)
    skill_id = models.ForeignKey(Skill)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = 'Weaknesses'