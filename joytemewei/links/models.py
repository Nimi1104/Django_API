from webbrowser import get
from django.db import models
from django.contrib.auth import get_user_model

class Link(models.Model):
    target_url = models.URLField(max_length = 200)
    description = models.CharField(max_length = 200)
    identifier = models.SlugField(max_length = 200, blank = True, unique = True)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    created_date = models.DateTimeField
    active = models.BooleanField(default = True)
    
    def __str__(self):
        return self.description
        