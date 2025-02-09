from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_views

urlpatterns = [
    path('', views.Index, name='index'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('contact/', contact_views, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
