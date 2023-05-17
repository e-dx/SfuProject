from django.contrib import admin

from .models import *

class AuthorAdmin(admin.ModelAdmin):
    pass

# Регистрация пользовательских моделей
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Warehouse)