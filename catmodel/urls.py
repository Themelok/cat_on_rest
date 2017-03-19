from django.conf.urls import include, url
from catmodel.views import CatViewSet, AuthorViewSet
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(prefix='cats', viewset=CatViewSet)
# router.register(prefix='authors', viewset=AuthorViewSet)
router.register(prefix='cats', viewset=CatViewSet)
router.register(prefix='authors', viewset=AuthorViewSet)
urlpatterns = [
    url(r'^',include(router.urls))
]