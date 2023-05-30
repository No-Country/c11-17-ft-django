from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
  
    path("admin/", admin.site.urls),
    path("",include("apps.homepage.urls")),
    path("posts/",include("apps.posts.urls")),
    path("",include("apps.user.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
