"""villagr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_extensions.routers import ExtendedSimpleRouter

from village_api import views


ROUTER = ExtendedSimpleRouter()
ROUTER.register(r'users', views.UserProfileViewSet)
ROUTER.register(r'person', views.PersonViewSet)

VILLAGE_ROUTER = ROUTER.register('villages', views.VillageViewSet, basename='village')
VILLAGE_ROUTER.register(
    'attendance',
    views.AttendanceLogViewSet,
    basename='village-attendance',
    parents_query_lookups=['village']
)

urlpatterns = [
    path('', include(ROUTER.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
