# from django.conf.urls import url
from django.urls import path
from DashboardApp import views

urlpatterns=[
    path("items/", views.dashboardApi, name='dashboardApi'),
    path('items/<int:id>/', views.dashboardApi, name='dashboardApi-detail'),  
    path("categories/", views.categoryApi, name='categoryApi'),
    path("categories/<int:id>/", views.categoryApi, name='categoryApi-detail'),
    path("tags/", views.tagApi, name='tagApi'),
    path("tags/<int:id>/", views.tagApi, name='tagApi-detail'),
]