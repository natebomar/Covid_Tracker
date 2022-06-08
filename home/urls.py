from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    path('index.html', views.summary),
    path('day.html', views.day),
    path('week.html', views.week),
    path('month.html', views.month),
    path('alltime.html', views.alltime),
    path('vaccination.html', views.vaccination)
]