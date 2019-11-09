from django.contrib import admin
from .models import Devnote

# Register your models here.


@admin.register(Devnote)
class DevnoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status',
                    'created_at', 'completed_at')
