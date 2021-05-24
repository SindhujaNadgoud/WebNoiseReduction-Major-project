from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("welcome/",views.welcome,name="welcome"),
    path("view_project/<str:topic_id>",views.view_project,name="view_project"),
    path("view_project/<str:topic_id>/<str:link_id>",views.view_project,name="view_project"),
    
  #  path("welcome/cinema1",views.cinema,name="cinema1"),
]