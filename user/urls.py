

from rest_framework import routers
from user.views import *


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = router.urls
