from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200) #required field
    description = models.TextField(null=True, blank=True) #not required
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) #auto generate timestamp
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # must be unique