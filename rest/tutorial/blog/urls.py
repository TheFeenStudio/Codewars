from rest_framework import routers
from blog.views.views import BlogView
from django.urls import path, include

<<<<<<< HEAD
# router = routers.DefaultRouter()
# router.register('', Blog, 'blog')
# urlpatterns = router.urls
=======

urlpatterns = {
    path('blog/', BlogView.as_view())
}
>>>>>>> 1c3b26634dd2b724a818c058c742b101cfba0bef
