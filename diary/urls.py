from django.urls import path
from diary import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
    path('practice/', views.practice),
    path('practice_2/', views.practice_2),
]