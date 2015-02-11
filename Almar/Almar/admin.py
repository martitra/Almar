'''
Created on 11/02/2015

@author: dam201
'''

from django.contrib import admin
from Almar.models import Proveedor, Empleado, Categoria, FormaPago, Articulo, Cliente, Pedido, Lineas_Pedido, Usuario

admin.site.register(Proveedor)
admin.site.register(Empleado)
admin.site.register(Categoria)
admin.site.register(FormaPago)
admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Lineas_Pedido)
admin.site.register(Usuario)