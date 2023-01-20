from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('usercreate/',views.usercreate,name="usercreate"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
]