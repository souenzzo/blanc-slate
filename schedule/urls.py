from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bokeh_demo', views.bokeh_demo, name='bokeh_demo'),
]
