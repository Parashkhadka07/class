from django.urls import path
from . import views
   

urlpatterns=[
     path("",views.home,name="home_page"),
     path("project/<int:id>/",views.project,name="project_page")
]