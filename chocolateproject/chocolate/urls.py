from .import views
from django.urls import path


urlpatterns = [
    path('',views.indexpage,name='indexpage'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('ajax/load-cities',views.load_cities, name='ajax_load_cities'),
    path('customerorder', views.customerorder, name='customerorder'),
    path('logout', views.logout, name='logout'),
    path('tvm', views.tvm, name='tvm'),
    path('ekm', views.ekm, name='ekm'),
    path('thrissure', views.thrissure, name='thrissure'),
    path('kottayam', views.kottayam, name='kottayam'),
    path('alappuzha', views.alappuzha, name='alappuzha'),
    path('palakkad', views.palakkad, name='palakkad'),
    path('kozhikode', views.kozhikode, name='kozhikode'),

]
