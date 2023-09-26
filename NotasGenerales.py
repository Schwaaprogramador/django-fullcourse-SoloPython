#----------------------------------------------
#----------------------------------------------
#    TUTORIAL SOLOPYTHON FULL COURSE DJANGO


#----------------------------------------------
#----------------------------------------------
# Al inicial un proyecto siempre recordar Crear un ambiente virtual:
#       Para instalarlo: pip install virtualenv [En la terminal]
#       Para crear un ambiente: virtual env [En la terminal]
#       Para Activarlo: navegar a la carpeta env/Scripts y ejecutar active


#----------------------------------------------
#----------------------------------------------
#   Cuando se vincula el proyecto con github recordar crear el gitignore [python]
#   Crear una branch para cada cambio del projecto.

#


#----------------------------------------------
#----------------------------------------------
#   Instalar dentro del ambiente virtual Django.
#   [En la terminal] pip install -r requirements.txt
#   Para crear un proeycto de django: django-admin startproject core . [En la terminal]
#   Para iniciar el server : python manage.py runserver
#
#   Para hacer las migraciones:
#   python manage.py migrate [En la terminal]
#   
#   
#   Para crear un administrador:
#   python manage.py createsuperuser
#   admin admin123


#----------------------------------------------
#----------------------------------------------
#   En el archivo Setting pusimos en comentarios la descripcion del cada uno de los codigos que viene por default.
#   Al hacer las migraciones activamos las funcionalidades del setings.
#       Esto es importante a la hora de trabajar con la DB y los modelos.
#
#
#
#


#----------------------------------------------
#----------------------------------------------
#   Para crear una nueva views:
#       crear una archivo views.py en el core:
#           dentro de la clase, crear una fn() Get que retorna la request y el template
#               def get(self, request, *args, **kwargs):
#                return render(request, 'index.html', context)
#
#
#   Para crer un template:
#       creamos una carpeta template dentro del proyecto en si [fuera del core].