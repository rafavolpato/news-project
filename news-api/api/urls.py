from django.urls import include, path
from rest_framework import routers
from api.views import EntryViewSet

router = routers.SimpleRouter()
router.register(r'entry', EntryViewSet)

urlpatterns = router.urls