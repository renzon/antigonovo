from django.contrib import admin

# Register your models here.
from antigonovo.moveis.models import Movel


@admin.register(Movel)
class MovelAdmin(admin.ModelAdmin):
    list_display = 'titulo preco'.split()
    ordering = ('titulo',)
