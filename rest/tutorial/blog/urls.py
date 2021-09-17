from rest_framework import routers
from blog.views.views import BlogView
from django.urls import path, include


router = routers.DefaultRouter()
router.register('', Blog, 'blog')
urlpatterns = router.urls

urlpatterns = {
    path('blog/', BlogView.as_view())
}