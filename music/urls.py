from django.urls import path, include
from . import views

urlpatterns = [
    path('music/', views.get_all_songs),
    path('music/<int:pk>/', views.get_by_id),
]