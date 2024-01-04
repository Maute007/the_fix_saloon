from django.contrib import admin
from django.urls import path

from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('o/', views.index, name='index'),
    path('logout/', views.logout_and_show_login, name='logout'),
    path('add_registro', views.add_registro, name='add_registro'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<str:product_id>/', views.delete_product, name='delete_product'),
]
