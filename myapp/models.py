from django.db import models
from django.utils.text import slugify
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default= 'default-slug')
    content = models.TextField()
    deadline = models.DateTimeField()
    image = models.ImageField(upload_to='post_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['deadline']  # Orders posts by deadline in Ascending order

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
# myapp/models.py
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    details = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}


