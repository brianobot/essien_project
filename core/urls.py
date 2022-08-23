from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# general settings for all admin pages registered in the project
AdminSite.site_header = "MAadonna E-Library Admin"
AdminSite.index_title = "Madonna E-Library Admin Homepage"
AdminSite.site_title = "Madonna E-Library Admin"

urlpatterns = [
    path('', include('library.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # in dev mode mode: add the path for django toolbar (review does django toolbar disappear in production mode)
    
