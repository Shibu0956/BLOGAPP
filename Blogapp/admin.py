from django.contrib import admin
from Blogapp.models import Myblog
 
# Register your models here.
class Blogadmin(admin.ModelAdmin):
    list_display=("title","name","content")
admin.site.register(Myblog,Blogadmin)    
 