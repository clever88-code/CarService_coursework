from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include





urlpatterns = [
    #приложения main
    path('', include('main.urls') ),
    #приложения news
    path('news/', include('news.urls') ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
