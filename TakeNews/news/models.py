from django.db import models

class New(models.Model):
    title = models.CharField(max_length=250, default=None)
    content = models.TextField(default=None)
    tags = models.CharField(max_length=300, default=None)
    sources = models.CharField(max_length=300, default=None)    
    
    def tags_list(self):
        return self.tags.split(',')
    
    def sources_list(self):
        return self.sources.split(',')

    def __str__(self):
        return self.title