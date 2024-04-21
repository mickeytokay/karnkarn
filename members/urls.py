from django.urls import path

from. import views

urlpatterns = [
    path('', views.members, name='members'),
    path('block/<slug:block_slug>/', views.members, name='members_by_block'),
    path('search/', views.search, name='search'),
]
