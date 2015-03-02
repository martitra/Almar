'''
Created on 11/02/2015

@author: dam201
'''

from django.views import generic
from django.shortcuts import render
from Almar.models import *


class HomeView(generic.base.TemplateView):
    """
        General project index view (home)
    """
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    #@method_decorator(login_required) permitir acceso anonimo, no necesario ser usuario logueado
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
# End HomeView

def error404(request):
    """
        Error 404 view.
        The 404 view is also called if Django doesn't find a match after checking regular expression in the URLconf.
    """
    return render(request, '404.html')

def error500(request):
    """
        Error 500 view.
        The 404 view is called in case of server errors.
    """
    return render(request, '500.html')
  
class Proveedorview(generic.ListView):
    template_name= 'proveedor/proveedores.html'
       
    def get_queryset(self):
        """ Return 50 first proveedores."""
        return Proveedor.objects.order_by('-nombre')[:50]
    
class ProveedorDetalle(generic.DetailView):
    model = Proveedor
    template_name = 'provedor/ProveedorDetalle.html'


class Articuloview(generic.ListView):
    template_name='articulo/articulos.html'
    
    def get_queryset(self):
        """ Return 50 first articulos."""
        return Articulo.objects.order_by('-nombre')[:50]
    
class ArticuloDetalle(generic.DetailView):
    model = Articulo
    template_name = 'articulo/ArticuloDetalle.html'

class Clienteview(generic.ListView):
    template_name='cliente/clientes.html'
    
    def get_queryset(self):
        """ Return 50 first articulos."""
        return Cliente.objects.order_by('-nombre')[:50]
    
class ClienteDetalle(generic.DetailView):
    model = Cliente
    template_name = 'cliente/ClienteDetalle.html'

class Categoriaview(generic.ListView):
    template_name='categoria/categorias.html'
    
    def get_queryset(self):
        """ Return 50 first categorias."""
        return Categoria.objects.order_by('-nombre')[:50]

#class autorDetalle(generic.DetailView):
#    model = Autor
#    template_name='autores/autorDetalle.html'


#@login_required
#def PrestamoConfirm(request, id):
#    instance = get_object_or_404(Libro, pk=id)
#    prestamo = Prestamo.objects.
#    form = LibroForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         contact = form.save()
#         contact.save()
#         return HttpResponseRedirect('libros')
#    return render_to_response('libros/confirmacionprestamo.html',
#                           {'prestamo_form': form,
#                           'id':id},
#                            context_instance=RequestContext(request))
#    
    #return HttpResponseRedirect(reverse('libros'))
#@login_required#solo podran hacer pestamos los usuarios loqueados
#def pedir_prestamo_libro(request, id):
#    prestamo=Prestamo.objects.all()
#    if(prestamo==request.user.username and prestamo.libro==id or Prestamo.objects.count()==0): 
#        c = Libro.objects.get(pk=id)
#        _username = request.user.username
#        id_usuario = User.objects.get(username=_username)
#        elprestamo = Prestamo(usuario=id_usuario, libro=c, fecha_ini=datetime.datetime.now(), fecha_fin=datetime.datetime.now() + datetime.timedelta(15,0))
#        elprestamo.save()
#        c.stock = c.stock-1
#        c.save()
#        return HttpResponseRedirect(reverse('libros'))
    #return render(request, 'prestamo/prestamoForm.html', {'form': form})
#    print "Ya tienes este libro."
#    return HttpResponseRedirect(reverse('libros'))

#class misprestamos(generic.ListView):
#    template_name = 'prestamo/misprestamos.html'
    
#    def get_queryset(self):
#        if self.request.user:
#            user = User.objects.get(username=self.request.user)
#            return Prestamo.objects.filter(usuario=user)
#        else:
#            return HttpResponseRedirect(reverse('home'))
#    

#class prestamosdetalle(generic.DetailView):
#    model = Prestamo
#    template_name='prestamo/prestamoDetalle.html'
#    
#def prestamodev(request, id):
#    prestamo = Prestamo.objects.get(pk=id)
#    prestamo.devuelto = True
#    prestamo.save()
#    c = Libro.objects.get(titulo=prestamo)
#    c.stock = c.stock+1
#    c.save()
#    return HttpResponseRedirect(reverse('prestamos'))
