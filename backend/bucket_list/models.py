from django.db import models
from django.conf import settings
from common.models import TimeStampModel
# Create your models here.
class BucketList(TimeStampModel):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,related_name = "bucket_lists")
    title = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    