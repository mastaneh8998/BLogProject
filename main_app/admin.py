from django.contrib import admin
from .models import post , Label
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
   
admin.site.register(post , PostAdmin)
admin.site.register(Label)
