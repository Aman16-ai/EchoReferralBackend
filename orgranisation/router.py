from rest_framework.routers import SimpleRouter
from .views import OrganisationViewSet
router = SimpleRouter()
router.register("",OrganisationViewSet)
