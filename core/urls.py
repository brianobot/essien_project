from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('library.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # in dev mode mode: add the path for django toolbar (review does django toolbar disappear in production mode)
    
