from django.db import models
from setting.models import SessionModel


# Create your models here.
class WebsiteInfoModel(models.Model):
    site_name = models.CharField(max_length=200)
    site_description = models.TextField(null=True, blank=True)
    site_info_email = models.EmailField(null=True, blank=True)
    site_support_email = models.EmailField(null=True, blank=True)
    site_line_one = models.CharField(max_length=20, null=True, blank=True)
    site_line_two = models.CharField(max_length=20, null=True, blank=True)
    site_social_facebook = models.CharField(max_length=100, null=True, blank=True)
    site_social_twitter = models.CharField(max_length=100, null=True, blank=True)
    site_social_instagram = models.CharField(max_length=100, null=True, blank=True)
    site_social_linkedin = models.CharField(max_length=100, null=True, blank=True)
    site_social_youtube = models.CharField(max_length=100, null=True, blank=True)
    site_social_youtube_video_link = models.CharField(max_length=200, null=True, blank=True)
    site_address = models.TextField()
    site_image = models.FileField(upload_to='images/site_images', null=True, blank=True)
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE)
    TERM = (
        ('1st TERM', '1st TERM'), ('2nd TERM', '2nd TERM'), ('3rd TERM', '3rd TERM')
    )
    term = models.CharField(max_length=10, choices=TERM, null=True, blank=True)

    def __str__(self):
        return self.site_name


class NewsLetterModel(models.Model):
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=20)
