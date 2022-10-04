from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.HomePage.as_view(), name='index'),
]