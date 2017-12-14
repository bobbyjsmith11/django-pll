from django.urls import path

from . import views

app_name = 'splotr'
urlpatterns = [
        path('', views.index, name='index'),
        path('test_ajax', views.test_ajax, name='test_ajax'),
        path('get_logmag', views.get_logmag, name='get_logmag'),
    ]
