from django.contrib import admin
from myapp.models import Resume

# Register your models here.
admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'state']

admin.site.register(Resume)