from django.urls import path
from apps.usermanagement.views import register, \
        petpal_login, petpal_logout
        
urlpatterns = [
    path('user-registration/',register,name='user_registration'),
    path('login/',petpal_login,name='petpal_login'),
    path('logout/',petpal_logout,name='petpal_logout'),
    
]