from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import OrganizationViewset

router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
