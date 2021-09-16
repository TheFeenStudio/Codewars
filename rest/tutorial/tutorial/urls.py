from django.contrib import admin
from django.urls import path, include
from blog.views.views import ContactView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
    path('', ContactView.as_view(), name="contact")
]

