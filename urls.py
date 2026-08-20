from django.urls import path
from contacts import views
urlpatterns=[path("",views.index,name="index"),path("add/",views.add_contact,name="add"),path("delete/<int:pk>/",views.delete_contact,name="delete")]
