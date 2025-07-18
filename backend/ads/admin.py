from django.contrib import admin
from .models import Ad, AdImage, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(AdImage)