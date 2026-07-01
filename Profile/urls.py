from django.urls import path
from . import views
app_name='Profile'
urlpatterns = [
    path('register',views.RegisterView,name="register"),
    path('updateprofile/<int:pk>',views.RegisterView,name="update"),
    path('login',views.LoginView,name="loginu"),
    path('logout',views.LogoutView,name="logout")
]
