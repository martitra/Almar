'''
Created on 10/02/2015

@author: dam201
'''

from django.db import models
from django.forms import ModelForm
from datetime import datetime

class Proveedor(models.Model):
    cif = models.CharField("CIF", max_length=9)
    nombre = models.CharField("Nombre", max_length=20)
    telefono = models.CharField("Telefono", max_length=40)
    email = models.EmailField("Email",blank = True)
    provincia = models.CharField("Provincia", max_length=40)
    ciudad = models.CharField("Ciudad", max_length=40)
    direccion = models.CharField("Direccion", max_length=40)
    cp = models.CharField("Codigo Postal", max_length=5)
    def __str__(self):
        return self.nombre
    class Meta():
        app_label = 'Almar'
class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['cif', 'nombre', 'telefono', 'email', 'provincia', 'ciudad', 'direccion', 'cp']

class Empleado(models.Model):
    nif = models.CharField("NIF", max_length=12)
    nombre = models.CharField("Nombre", max_length=20)
    apellidos = models.CharField("Apellidos", max_length=40)
    telefono = models.CharField("Telefono", max_length=40)
    email = models.EmailField("Email",blank = True)
    provincia = models.CharField("Provincia", max_length=40)
    ciudad = models.CharField("Ciudad", max_length=40)
    direccion = models.CharField("Direccion", max_length=40)
    cp = models.CharField("Codigo Postal", max_length=5)
    estado = models.BooleanField("Activo", default = True)
    def __str__(self):
        return self.nombre
    class Meta():
        app_label = 'Almar'
class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nif', 'nombre', 'apellidos', 'telefono', 'email', 'provincia', 'ciudad', 'direccion', 'cp', 'estado']
        
class Categoria(models.Model):
    nombre = models.CharField("Nombre de Categoria", max_length=20)
    def __str__(self):
        return self.nombre
    class Meta():
        app_label = 'Almar'
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
                
class Forma_Pago(models.Model):
    descripcion = models.CharField("Forma de Pago", max_length = 45)
    def __str__(self):
        return self.descripcion
    class Meta():
        app_label = 'Almar'
class Forma_PagoForm(ModelForm):
    class Meta:
        model = Forma_Pago
        fields = ['descripcion']
        
class Articulo(models.Model):
    id_categoria = models.ForeignKey(Categoria, verbose_name="Categoria")
    id_proveedor = models.ForeignKey(Proveedor, verbose_name="Proveedor")
    cod_fabricante = models.CharField("Codigo de Fabricante", max_length = 20)
    stock = models.IntegerField("Stock", max_length=4)
    nombre = models.CharField("Nombre Articulo", max_length=30)
    precio = models.IntegerField("Precio", max_length=11)
    descripcion = models.CharField("Descripcion", max_length=300)
    def __str__(self):
        return self.nombre
    class Meta():
        app_label = 'Almar'
class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['id_categoria', 'id_proveedor', 'cod_fabricante', 'stock', 'nombre', 'precio', 'descripcion']
        
class Cliente(models.Model):
    nif = models.CharField("NIF", max_length =9)
    nombre = models.CharField("Nombre", max_length=20)
    apellidos = models.CharField("Apellidos", max_length=40)
    telefono = models.CharField("Telefono", max_length=40)
    email = models.EmailField("Email",blank = True)
    provincia = models.CharField("Provincia", max_length=40)
    ciudad = models.CharField("Ciudad", max_length=40)
    direccion = models.CharField("Direccion", max_length=40)
    cp = models.CharField("Codigo Postal", max_length=5)
    def __str__(self):
        return self.nombre
    class Meta():
        app_label = 'Almar'
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nif', 'nombre', 'apellidos', 'telefono', 'email', 'provincia', 'ciudad', 'direccion', 'cp']
        
class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, verbose_name="Cliente")
    empleado = models.ForeignKey(Empleado, verbose_name = "Empleado")
    forma_pago = models.ForeignKey(Forma_Pago, verbose_name = "Forma de Pago")
    fecha = models.DateField(default=datetime.date, verbose_name="Fecha")
    presupuesto = models.BooleanField("Presupuesto", default = False)
    pagado = models.BooleanField("Pagado", default = False)
    def __str__(self):
        return self.id_cliente+self.empleado
    class Meta():
        app_label= 'Almar'
class PedidoForm(ModelForm):
    class MEta:
        model = Pedido
        fields = ['id_cliente', 'empleado', 'forma_pago', 'fecha', 'presupuesto', 'pagado']
        
class Linea_Pedido(models.Model):
    id_pedido = models.ForeignKey(Pedido, verbose_name = "Pedido")
    id_articulo = models.ForeignKey(Articulo, verbose_name = "Articulo")
    num_articulos = models.IntegerField("Numero de Articulos", max_length = 4)
    def __str__(self):
        return self.id_pedido+self.id_articulo
    class Meta():
        app_label='Almar'
        
class Usuario(models.Model):
    id_empleado = models.ForeignKey(Empleado, verbose_name = "Empleado")
    nombre = models.CharField("Nombre", max_length = 45)
    password = models.CharField("Contrasena", max_length = 45)
    admin = models.BooleanField("Administrador", default = False)
    def __str__(self):
        return self.nombre
    class Meta():
        app_label = 'Almar'
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['id_empleado', 'nombre', 'password', 'admin']
    
    