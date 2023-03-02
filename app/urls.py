from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.login, name='login'),
    path("create_doc", views.create_doc, name='create_doc'),
    path("read_doc", views.read_doc, name='read_doc'),
    path("pedidos", views.pedidos, name='pedidos'),
]