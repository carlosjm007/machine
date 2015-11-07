from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Machine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','Machine.views.Inicio'),
    url(r'^sobre/$','Machine.views.dinamica'),
    url(r'^pandillagranadilla/$','Machine.views.granadilla'),
    url(r'^Marla/$','Machine.views.Marla'),
    # url(r'^foto/$','Machine.views.foto'),
    # url(r'^encajar/$','Machine.views.encajar'),
    # url(r'^predecir/$','Machine.views.predecir'),
)

urlpatterns += staticfiles_urlpatterns()