from django.urls import path
from .views import UserLoginView, UserRegisterView, home_view, logout_view

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
]
