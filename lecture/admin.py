from django.contrib import admin

from .models import Lecture

# Register your models here.


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title','lecturer_name' ,'duration','date')
    search_fields = ('title','lecturer_name')
