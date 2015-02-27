# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'categoria'
        
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)  # AutoField?
    cif = models.CharField(max_length=9)
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=40)
    email = models.CharField(max_length=75)
    provincia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    cp = models.CharField("Codigo Postal", max_length=5)
    
    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'proveedor'

class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)  # AutoField?
    id_categoria = models.ForeignKey(Categoria, db_column='id_categoria')
    id_proveedor = models.ForeignKey(Proveedor, db_column='id_proveedor')
    cod_fabricante = models.CharField(max_length=20)
    stock = models.IntegerField()
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'articulo'

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)  # AutoField?
    nif = models.CharField(max_length=9)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    email = models.CharField(max_length=75)
    provincia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    cp = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'cliente'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)  # AutoField?
    nif = models.CharField(max_length=12)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    email = models.CharField(max_length=75)
    provincia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    cp = models.CharField(max_length=5, verbose_name ="Codigo Postal")
    estado = models.BooleanField(default = True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'empleado'


class FormaPago(models.Model):
    id_forma_pago = models.AutoField(primary_key=True)  # AutoField?
    descripcion = models.CharField(max_length=45)
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        managed = True
        db_table = 'forma_pago'

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)  # AutoField?
    id_cliente = models.ForeignKey(Cliente, db_column='id_cliente')
    empleado = models.ForeignKey(Empleado, db_column='empleado')
    forma_pago = models.ForeignKey(FormaPago,db_column='forma_pago')
    fecha = models.DateField()
    presupuesto = models.IntegerField()
    pagado = models.IntegerField()

    def __str__(self):
        return self.id_pedido+" - "+self.id_cliente

    class Meta:
        managed = True
        db_table = 'pedido'

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)  # AutoField?
    id_empleado = models.ForeignKey(Empleado, db_column='id_empleado')
    nombre = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    admin = models.BooleanField(default = False)
    def __str__(self):
        return self.nombre
    class Meta:
        managed = True
        db_table = 'usuario'

class Lineas_Pedido(models.Model):
    id_linea = models.AutoField(primary_key = True)
    id_pedido = models.ForeignKey(Pedido, db_column='id_pedido')
    id_articulo = models.ForeignKey(Articulo, db_column='id_articulo')
    num_articulos = models.IntegerField()

    def __str__(self):
        return self.id_linea+" - "+self.id_pedido+" - "+self.id_articulo

    class Meta:
        managed = True
        db_table = 'lineas_pedido'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'




