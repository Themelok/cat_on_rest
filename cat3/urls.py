from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^', include('catmodel_frontend.urls', namespace='frontend')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/', include('catmodel.urls', namespace='api'))
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
