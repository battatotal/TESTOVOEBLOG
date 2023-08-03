from django.urls import path
from . import views


app_name = 'blogapp'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:id>', views.user_selected, name='user_selected'),
    path('delete/<str:slug>', views.post_delete, name='post_delete'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.loguot_user, name='logout'),
    ]