from rest_framework.routers import SimpleRouter
from .views import JobModelViewSet
router = SimpleRouter()
router.register("",JobModelViewSet)
