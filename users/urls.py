from django.urls import path
from .views import register, login_view 
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('register/',register, name='register'),
    path('login/', login_view, name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
