from django.contrib import admin
from cars.models import Car,Brand

# Register your models here.

#Configurando a criação de novos carros no painel de admin
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'contact', 'id')
    search_fields = ('model', 'brand', 'factory_year', 'model_year', 'value', 'contact', 'id')

admin.site.register(Car, CarAdmin)

#Configurando a adição de novas marcas através do painel de admin
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Brand, BrandAdmin)