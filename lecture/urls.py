from rest_framework import routers

from .views import LectureView

router = routers.DefaultRouter()
router.register(r'', LectureView, basename="lecture")

urlpatterns = router.urls 
