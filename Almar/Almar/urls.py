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

    
)
