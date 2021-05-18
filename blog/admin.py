from django.contrib import admin
from .models import Post #inlcuimos el modelo Post
# Register your models here.


#para hacer el modelo visible en la pagina del administrdor se tiene que registrar el modelo con 
admin.site.register(Post)

