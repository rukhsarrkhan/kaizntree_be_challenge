# from django.conf.urls import url
from django.urls import path
from DashboardApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("items/",views.dashboardApi),
    # path(r"item/([0-9]+)$",views.dashboardApi), 
]