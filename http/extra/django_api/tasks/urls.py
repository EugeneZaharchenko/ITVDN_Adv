from django.contrib import admin
from django.urls import path, include

from issues.views import IssueModelViewSet, AuthView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('issues', IssueModelViewSet, basename='issues')
router.register('auth', AuthView, basename='auth')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.get_urls())),
]
