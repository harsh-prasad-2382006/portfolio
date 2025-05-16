from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    level = models.CharField(
        max_length=50,
        choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')],
        default='beginner',
    )  
    icon = models.ImageField(null=True,upload_to='skills_icon')
    description = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ContactPage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name