from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("product/", include("products.urls")),
    path("pages/", include("pages.urls")),
    path("categories/", include("categories.urls")),
    path("", views.home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
