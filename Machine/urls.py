from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Machine import views as vista

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Machine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',vista.Inicio),
    url(r'^sobre/$',vista.dinamica),
    url(r'^pandillagranadilla/$',vista.granadilla),
    url(r'^Marla/$',vista.Marla),
    url(r'^foto/$',vista.foto),
    url(r'^encajar/$',vista.encajar),
    url(r'^predecir/$',vista.predecir),
    url(r'^reset/$',vista.reset),
    url(r'^traficovista/$',vista.vista_trafico),
    url(r'^trafico/$',vista.trafico),
    url(r'^suma/$',vista.suma),
)

urlpatterns += staticfiles_urlpatterns()