from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', views.criar_objeto, name='criar_objeto'),
    path('update/<int:objeto_id>/', views.atualizar_objeto, name='atualizar_objeto'),
    path('delete/<int:objeto_id>/', views.deletar_objeto, name='deletar_objeto'),
    path('list/', views.mostrar_objeto, name='mostrar_objeto'),
]
