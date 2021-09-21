from rest_framework import routers
from views import BlogView
from django.urls import path, include
from models import Blog


router = routers.DefaultRouter()
router.register('', Blog, 'blog')
urlpatterns = router.urls

urlpatterns = {
    path('blog', BlogView.as_view())
}