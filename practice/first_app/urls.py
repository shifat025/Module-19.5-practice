from django.urls import path
from . import views

urlpatterns = [
    path('sing_up/', views.sing_up, name='sing_up'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.pass_change, name='pass_change'),
    path('change_password2/', views.pass_change2, name='pass_change2'),
]