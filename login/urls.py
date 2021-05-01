from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'logins'

urlpatterns = [
    path('', views.login_view, name="login"), #로그인 뷰와 연결
    path('logout', views.logout_view, name="logout"), #로그아웃 뷰와 연결
    path('signup', views.signup_view, name="signup") #회원가입 뷰와 연결
]