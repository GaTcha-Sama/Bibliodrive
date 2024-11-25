from django.db import models
from uuid import uuid4
import os

def cover_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.isbn}_{uuid4().hex[:8]}.{ext}"
    return os.path.join('cover_images', filename)
 
# Table "AUTHORS"
class Author(models.Model):
    au_id = models.AutoField(primary_key=True)  # SERIAL equivalent
    author = models.CharField(max_length=50)
    year_born = models.SmallIntegerField()

    def __str__(self):
        return self.author
 
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

    def __str__(self):
        return self.name
 
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
    cover_image = models.ImageField(upload_to=cover_image_upload_to, blank=True, null=True)

    def __str__(self):
        return self.title
 