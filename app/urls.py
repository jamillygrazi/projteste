from django.urls import path
from . import views

urlpatterns = [
    path("", views.principal, name='principal'),
    path("login", views.login, name='login'),
    path("create_doc", views.create_doc, name='create_doc'),
    path("read_doc", views.read_doc, name='read_doc'),
    path("pedidos", views.pedidos, name='pedidos'),
    path("menu", views.menu, name='menu'),
    path("pagamentos", views.pagamentos, name='pagamentos'),
    path("create_person", views.person_create, name='create_person'),
    path("read_person", views.person_read, name='read_person'),
    path("update_person/<int:id>", views.person_update, name='update_person'),
    path("delete_person/<int:id>", views.person_delete, name='delete_person'),
    path("update_doc/<int:id>", views.doc_update, name='update_doc'),
    path("delete_doc/<int:id>", views.doc_delete, name='delete_doc'),
]
