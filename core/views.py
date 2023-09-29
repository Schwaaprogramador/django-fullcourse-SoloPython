# Este archivo lo creamos nosotros para hacer una nueva view

from django.views.generic import View
from django.shortcuts import render

#vistas de clase
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={
            

        }
        return render(request, 'index.html', context)#por la configuracion de TEMPLATES, no es necesario especficar toda la ruta.
    
        