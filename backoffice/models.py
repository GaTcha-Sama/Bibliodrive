from django.db import models
 
# Table "AUTHORS"
class Author(models.Model):
    au_id = models.AutoField(primary_key=True)  # SERIAL equivalent
    author = models.CharField(max_length=50)
    year_born = models.SmallIntegerField()
 
# Table "PUBLISHERS"
class Publisher(models.Model):
    pubid = models.AutoField(primary_key=True)  # SERIAL equivalent
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    zip = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    comments = models.TextField()
 
# Table "TITLES"
class Title(models.Model):
    title = models.CharField(max_length=255)
    year_published = models.SmallIntegerField()
    isbn = models.CharField(max_length=20, primary_key=True)
    pubid = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    comments = models.TextField()
    authors = models.ManyToManyField(Author)  # Relation Many-to-Many avec Author
 