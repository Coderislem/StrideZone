from django.urls import path
from .views import register, login_view ,home,logout_view,profile
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('register/',register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/',logout_view,name='logout'),
    path('home/',home,name='home'),
    path('profile/',profile,name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)