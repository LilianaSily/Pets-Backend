from django.views.generic import TemplateView

class IndexPage (TemplateView):
    template_name = "index.html" 
   
class Contacto (TemplateView):
    template_name = "contacto.html" 
    
class Productos (TemplateView):
    template_name = "productos.html"   
    
class Perros (TemplateView):
    template_name = "perros.html"        
class Gatos (TemplateView):
    template_name = "gatos.html"    
