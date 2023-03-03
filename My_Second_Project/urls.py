from django.contrib import admin
from django.urls import path, include
from login_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('login_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
