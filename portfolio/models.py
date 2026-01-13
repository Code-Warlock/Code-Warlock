from django.db import models

from ckeditor.fields import RichTextField


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    cv_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True) 

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Award(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_received = models.DateField()
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-date_received']

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50)
    is_key_skill = models.BooleanField(default=False)
    def __str__(self): return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    demo_link = models.URLField(blank=True, null=True)
    repo_link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    def __str__(self): return self.title

class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    class Meta:
        ordering = ['-end_date']
    def __str__(self): return f"{self.role} at {self.company}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Message from {self.name}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    excerpt = models.TextField()
    content = RichTextField(blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)
    read_time = models.IntegerField(default=5)
    def __str__(self): return self.title