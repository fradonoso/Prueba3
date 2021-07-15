from django.contrib import admin
from .models import Dueño, Mascota, Ficha

# Register your models here.

admin.site.register(Dueño)
admin.site.register(Mascota)
admin.site.register(Ficha)