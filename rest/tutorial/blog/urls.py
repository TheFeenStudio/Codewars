from rest_framework import routers
from blog.views.views import Blog

router = routers.DefaultRouter()
router.register('', Blog, 'blog')
urlpatterns = router.urls