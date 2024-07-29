from django.db import models
from django.contrib.postgres.fields import JSONField

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.JSONField()
    phone = models.CharField(max_length=20)
    website = models.URLField()
    company = models.JSONField()  

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name

class Album(models.Model):
    user = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title

class Todo(models.Model):
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
