from django.urls import path

from. import views

urlpatterns = [
    path('', views.chairman, name='chairman'),
    path('secretery/', views.secretery, name='secretery'),
    path('financial/', views.financial, name='financial'),
    path('women/', views.women, name='women'),
    path('youth/', views.youth, name='youth'),
]
