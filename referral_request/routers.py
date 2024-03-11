from rest_framework.routers import SimpleRouter
from .views import ReferralRequestModelViewSet
router = SimpleRouter()
router.register("",ReferralRequestModelViewSet)