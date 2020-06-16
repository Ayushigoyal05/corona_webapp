from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home , name='home'),
    #path('',views.tb, name='tb'),
    path('Ventilators/', views.ventilators , name="ventilators"),
    path("Hospitals/", views.hospitals, name="hospitals"),
    path("Beds/", views.beds, name="beds"),
    path("Graphic/", views.graphic, name="graphic"),
    ]