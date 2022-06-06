from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    path('index.html', views.summary),
    path('today.html', views.today),
    path('week.html', views.week),
    path('month.html', views.month),
    path('alltime.html', views.alltime),
    path('vaccination.html', views.vaccination)
]