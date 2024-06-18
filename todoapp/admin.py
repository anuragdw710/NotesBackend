from django.contrib import admin
from .models import Writer
# Register your models here.
@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ['username','email','first_name','last_name']
    list_per_page=10
    list_select_related = ['user']
    ordering = ['user__username']
    search_fields = ['username__istartswith','email__istartswith','first_name__istartswith','last_name__istartswith']

