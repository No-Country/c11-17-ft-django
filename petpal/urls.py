from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('modpro/', views.modpro, name='modpro'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('buscar_paseador/', views.buscar_paseador, name='buscar_paseador'),
    path('buscar_perro/', views.buscar_perro, name='buscar_perro'),
    path("",include("apps.homepage.urls")),
    path("dog/",include("apps.dog.urls")),
    path("posts/",include("apps.posts.urls")),
    path("reservations/",include("apps.reservation.urls")),
    path("posts/",include("apps.posts.urls")),
    path("",include("apps.user.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
