from django.contrib import admin
from .models import Estoque
# Register your models here.
@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'produto', 'genero', 'quantidade', 'preco')
