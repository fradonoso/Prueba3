from django.urls import path
from .views import form_del_mascota, home, form_mascota, form_mod_mascota

urlpatterns= [
    path('', home, name="home"),
    path('form-mascota', form_mascota, name="form_mascota"),
    path('form-mod-mascota/<id>', form_mod_mascota, name="form_mod_mascota"),
    path('form-del-mascota/<id>', form_del_mascota, name="form_del_mascota")
]