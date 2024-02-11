# from django.conf.urls import url
from django.urls import path
from DashboardApp import views

urlpatterns=[
    path("items/",views.dashboardApi),
    path('items/<int:id>/', views.dashboardApi),  
    path("categories/",views.categoryApi),
    path("categories/<int:id>/",views.categoryApi),
    path("tags/",views.tagApi),
    path("tags/<int:id>/",views.tagApi),

]