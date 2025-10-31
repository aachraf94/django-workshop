from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model with role-based access"""
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('PROJECT_MANAGER', 'Project Manager'),
        ('CONTRIBUTOR', 'Contributor')
    ]
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CONTRIBUTOR')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('User', related_name='projects', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey('User', related_name='assigned_tasks', on_delete=models.CASCADE)
    created_by = models.ForeignKey('User', related_name='created_tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title   
    
