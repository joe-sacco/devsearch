from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200) #required field
    description = models.TextField(null=True, blank=True) #not required
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True) #auto generate timestamp
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # must be unique

    # display proper title string in Admin Panel
    def __str__(self): 
        return self.title
    

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #will delete reviews if project deleted
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name