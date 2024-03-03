from rest_framework.routers import SimpleRouter
from .views import UserViewSet,UserExperienceModelViewSet
router = SimpleRouter()
router.register("exp",UserExperienceModelViewSet)
router.register("",UserViewSet)