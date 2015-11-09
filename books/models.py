from django.db import models

# Create your models here.

class Author(models.Model):
    AuthorID = models.CharField(max_length = 30,primary_key = True)
    Name = models.CharField(max_length = 30)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 30)

    def __unicode__(self):
            return self.Name

class Book(models.Model):
    ISBN = models.CharField(max_length = 20, primary_key = True)
    Title = models.CharField(max_length = 100)
    AuthorsID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=30)
    PublishDate = models.DateField()
    Price = models.CharField(max_length=8)
    
    def __unicode__(self):
            return self.Title
