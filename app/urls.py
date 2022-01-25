from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path("",views.Registerpage,name="registerpage"),
   path("update/<int:id>",views.Update,name="update"),
   path("delete/<int:id>",views.Deletedata,name="delete"),
   path("search/",views.Search,name="search"),
   # path("login/",views.login,name="login"),
]