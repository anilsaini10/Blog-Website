from django.contrib import admin
from .models import Contact,HomeBlog

# Register your models here.
admin.site.register((Contact, HomeBlog))
