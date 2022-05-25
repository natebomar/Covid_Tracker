from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    path('index.html', views.us_sum),
    path('today.html', views.us_today),
    path('week.html', views.us_week),
    path('month.html', views.us_month),
    path('alltime.html', views.us_alltime),
    path('vaccination.html', views.us_vaccination)
]