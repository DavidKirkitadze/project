from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from news.views import ArticlesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('api/v1/articlelist/', ArticlesAPIView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
