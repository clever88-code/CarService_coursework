from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('main.urls')),
    path('record/', include('record.urls')),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
