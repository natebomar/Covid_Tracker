from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    path('index/index.html', views.us_sum),
    path('index/today.html', views.us_today),
    path('index/week.html', views.us_week),
    path('index/month.html', views.us_month),
    path('index/alltime.html', views.us_alltime),
    path('index/vaccination.html', views.us_vaccination)
]