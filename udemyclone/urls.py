from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from udemyclone import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('udemy.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
