from unicodedata import category
from django.db import models

# Create your models here.

# CATEGORY_CHOICES = (
#     ('A','ACTION')
#     ('D','DRAMA')
#     ('C','COMEDY')
#     ('R','ROMANCE')
# )

# LANGUAGE_CHOICES = (
#     ('EN' ,'ENGLISH'),
#     ('GR' , 'GERMAN'),
# )

# STATUS_CHOICES = (
#     ('RA' , 'RECENTLY ADDED')
#     ('MW' , 'MOST WATCHED')
#     ('TR' , 'TOP RATED')
# )


# class Movie(models.Model):
#     title =models.CharField(max_length=100)
#     description = models.TextField(max_length=1000)
#     image = models.ImageField(upload_to='movies')
#     category = models.CharField(choices=CATEGORY_CHOICES , max_length=1)
#     language = models.CharField(choices=LANGUAGE_CHOICES , max_length=2)
#     status = models.CharField(choices=STATUS_CHOICES , max_length=2)
#     year_of_production = models.DateField()
#     view_count = models.IntegerField(default=0)

AGE_CHOICES=(
    ('All','All'),
    ('Kids','Kids')
)

MOVIE_TYPE=(
    ('single','Single'),
    ('seasonal','Seasonal')
)

class CustomUser(models.Model):
    profiles=models.ManyToManyField('Profile')


class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES)
    # uuid=models.UUIDField(default=uuid.uuid4,unique=True)


    def __str__(self):
        return self.name +" "+self.age_limit

class Movie(models.Model):
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    # uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True)

class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')
    