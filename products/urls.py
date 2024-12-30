from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('women/', views.women, name='women'),
    path('man/', views.man, name="man"),
    path('search/', views.search_products, name='search'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
