from django.db import models
from django.utils import timezone
# Create your models here.

#from o import - lineas para agregar algo de otro archivo

#define nuesto modelo (es un objeto)
#class palabra clave para indicar que estamos definiendo un objeto
#Post es el nombre de nuestro modelo, se puede dar un nombre diferentes, se deben evitar espacios en blanco y caractere especiales, siempre se inicia
#con letra mayuscula

#models.Model  significa que Post es un modeo de Django, asi Djngo sabe que debe guardarlo e la base de datos

class Post(models.Model):

    ##propiedades, tipo de cada campo, una relacion con otro objeto
    #models.CharField  se define un texto con numero limitado de caracteres
    #models.TextField  texto largo sin limites
    #models.DateTimeField es fecha y hora
    #models.ForeignKey  es una relacion con otro modelo

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    ##sdef publish(self):, y def __str__(self) : son indentados dentro de la clase
    #se necesitan definir os metodos dentro de las clase
    #de lo contrario el metodo no corresponde a la clase, se puede obtener un comportamieto inesperado

    ##metodo publish funcion/metodo, utilizar minusculas y guion bajos
    #suelen devolver return

    def publish(self):
        self.published_date =timezone.now()
        self.save()

    ##metodo obtener un texto (string) con un titulo
    def __str__(self):
        return self.title

    #agregar el modelo a la base de datos

    #1 notificar a django que se han hecho modificaiones a l modelo
    #python manage.py makemigrations blog
    #django preparo un archivo de migracion
    #2 aplicar a la base de datos
    #python manage.py migrate blog