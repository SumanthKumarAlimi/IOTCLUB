from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    url(r'^$', views.homepage, name='index'),
    url(r'^workshops/$', views.workshops, name='workshops'),
    url(r'^course/$', views.course, name='course'),
    url(r'^achievements/$', views.achievements, name='achievements'),
    url(r'^corebody/$', views.corebody, name='corebody'),
    url(r'^projects/$', views.projects, name='Projects'),
    url(r'^actionplan/$', views.action, name='ActionPlan'),
    url(r'^Reports/$', views.Reports, name='Reports'),

]
urlpatterns += staticfiles_urlpatterns()
