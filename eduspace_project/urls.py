from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from eduspace_project import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cart/", include("cart.urls")),
    path("", include("accounts.urls")),
    path("", include("eduspace.urls")),
    path("", include("courses.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
