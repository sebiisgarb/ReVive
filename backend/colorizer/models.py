from django.db import models
from django.contrib.auth.models import User

class ColorizedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_image = models.ImageField(upload_to='original_images/')
    colorized_image = models.ImageField(upload_to='colorized_images/')
    method_used = models.CharField(max_length=100, choices=[
        ('unsupervised', 'Unsupervised'),
        ('supervised_prompt', 'Supervised_Prompt'),
        ('supervised_color_map', 'Supervised_Color_Map'),
        ('supervised_scribble', 'Supervised_Scribble'),
])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Colorized Image by {self.user.username} on {self.created_at}"


class ColorizedVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_video = models.FileField(upload_to='original_videos/')
    colorized_video = models.FileField(upload_to='colorized_videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Colorized Video by {self.user.username} on {self.created_at}"