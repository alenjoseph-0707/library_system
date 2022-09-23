from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login),
    path('detail',views.detail),
    path('edit',views.edit),
    path('update',views.update),
    path('delete',views.delete),
]