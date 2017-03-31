from rest_framework.routers import SimpleRouter
from core.views import *

router = SimpleRouter()

router.register(r'mailer', MailerViewSet, 'mailer')

urlpatterns = router.urls