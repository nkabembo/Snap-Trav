from django.contrib import admin
from .models import BucketList , Photo, Export, Activity
# Register your models here.

admin.site.register(BucketList)
admin.site.register(Photo)
admin.site.register(Export)
admin.site.register(Activity)