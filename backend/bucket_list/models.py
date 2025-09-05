from django.db import models
from django.conf import settings
from common.models import TimeStampModel
# Create your models here.
class BucketList(TimeStampModel):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,related_name = "bucket_lists")
    title = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
class Activity(models.Model):
    bucketlist_id = models.ForeignKey("BucketList",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[("kept", "Kept"), ("removed", "Removed")])
    notes = models.TextField(blank=True)

class Photo(models.Model):
    activity_id = models.ForeignKey("Activity",on_delete=models.CASCADE)
    image_path = models.TextField()
    caption = models.TextField()

class Export(models.Model):
    bucketlist_id = models.ForeignKey("BucketList", on_delete=models.CASCADE)
    filepath = models.TextField()  #collage image/PDF