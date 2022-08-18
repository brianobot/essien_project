from django.urls import path, include
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('home/', views.home_page, name='homepage'),
    path('search-list/<str:search_word>', views.search_list, name='search'),
]