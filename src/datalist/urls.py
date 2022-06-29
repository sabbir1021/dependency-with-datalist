from django.urls import path
from . import views

app_name = 'datalist'

urlpatterns = [
    path('', views.datalist, name='datalist'),
]