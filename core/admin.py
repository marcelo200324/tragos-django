from django.contrib import admin
from .models import Trago

@admin.register(Trago)
class TragoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'preparacion')





