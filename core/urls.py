from django.urls import path
from core.views import *


app_name = 'core'

urlpatterns = [
    path('', LoginView.as_view(), name='user-login'),
    path('login', LoginView.as_view(), name='user-login'),
    path('home', HomeView.as_view(), name='home'),
    path('user-logout/', UserLogout, name='user-logout'),
    path('user-register/', UserRegistrationView.as_view(), name='user-register'),

]
