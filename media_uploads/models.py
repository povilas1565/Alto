
from django.db import models
from django.contrib.auth.models import User

class MediaFile(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_files')
    title = models.CharField(max_length=100)
    caption = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/')
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
    is_public = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-uploaded_at']