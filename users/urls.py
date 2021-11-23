from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name="profiles"),

    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    path('profile/<str:pk>/', views.user_profile, name="user_profile"),
    path('account/', views.user_account, name="account"),
    path('edit_account/', views.edit_account, name="edit_account")
]