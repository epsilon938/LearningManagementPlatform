from django.urls import path
from . import views
urlpatterns=[
    path("",views.index, name="index"),
    path("login_page/", views.login_page, name="login_page"),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
]