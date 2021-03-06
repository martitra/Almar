from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from Almar import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Almar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^proveedores$', views.Proveedorview.as_view(), name='proveedores'),
    url(r'^proveedor/detalle/(?P<pk>\d+)/$', views.ProveedorDetalle.as_view(), name='proveedordetalle'),
    url(r'^articulos', views.Articuloview.as_view(), name='articulos'),
    url(r'^articulos/cat/(?P<pk>\d+)/$', views.ArticuloCat.as_view(), name='articuloscat'),
    url(r'^articulo/detalle/(?P<pk>\d+)/$', views.ArticuloDetalle.as_view(),  name = 'articulodetalle'),
    url(r'^clientes', views.Clienteview.as_view(), name='clientes'),
    url(r'^cliente/detalle/(?P<pk>\d+)/$', views.ClienteDetalle.as_view(),  name = 'clientedetalle'),
    url(r'^categorias', views.Categoriaview.as_view(), name='categorias'),
    url(r'^pedidos', views.Pedidoview.as_view(), name='pedidos'),
    url(r'^pedido/detalle/(?P<pk>\d+)/$', views.LineaPedidoLineaview.as_view(),  name = 'pedidodetalle'),
    url(r'^clientes/detalle/(?P<pk>\d+)/$', views.PedidoClienteview.as_view(),  name = 'pedidocliente'),
    url(r'^ventas/$', views.misVentas.as_view(), name = 'ventas'),
    
    
)
