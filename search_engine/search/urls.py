from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),  # Homepage with search form
    path('search/', views.search, name='search_results'),  # Search results page
]