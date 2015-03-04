'''
Created on 11/02/2015

@author: dam201
'''

from django.contrib import admin
from Almar.models import Proveedor, Empleado, Categoria, FormaPago, Articulo, Cliente, Pedido, Lineas_Pedido, Usuario



class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'cif', 'nombre', 'telefono', 'email', 'direccion', 'ciudad', 'provincia', 'cp')
    
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nif', 'nombre', 'apellidos', 'telefono', 'direccion', 'ciudad', 'provincia', 'cp', 'email', 'cp')
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre')

class ArticuloAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id_articulo', 'id_categoria', 'id_proveedor','cod_fabricante', 'stock', 'nombre', 'precio','descripcion' )
    
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nif','nombre','apellidos','telefono','email','direccion','ciudad', 'provincia','cp')
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido','id_cliente','empleado','forma_pago','fecha','presupuesto','pagado')

class Lineas_PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_linea','id_pedido','id_articulo','num_articulos')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario','id_empleado','nombre','password','admin' ) 
  
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(FormaPago)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Lineas_Pedido, Lineas_PedidoAdmin)
admin.site.register(Usuario, UsuarioAdmin)