
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_page, name='main'),
    path('rules/', views.rules_page, name='rules'),
    path('about/', views.about_us_page, name='aboutus')
]