from django.urls import path
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show), 
    path('add/', views.add),
    path("details/<int:contact_id>/", views.details),
    path("edit/<int:contact_id>/", views.edit),
    path("delete/<int:contact_id>/", views.delete),
]