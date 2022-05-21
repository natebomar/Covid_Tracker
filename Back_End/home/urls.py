from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    path('index/', views.us_sum)
]