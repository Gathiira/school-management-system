from django.contrib import admin

from .models import CertificateModel

# Register your models here.

@admin.register(CertificateModel)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at','updated_at')

    search_fields = ('name',)
    ordering = ('created_at','name')
    filter_horizontal = ()

