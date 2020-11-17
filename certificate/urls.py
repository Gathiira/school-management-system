from rest_framework import routers

from .views import CertificateView

router = routers.DefaultRouter()
router.register(r'', CertificateView, basename="certificates")

urlpatterns = router.urls 
