from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('create-account/', views.sign_up_page, name='create-account'),
    path('login/', views.LoginPage.as_view() , name='login-account'),
    path('logout/', views.logout_account, name='logout-account'),    
]