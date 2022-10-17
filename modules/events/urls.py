from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modules.events import views

# Viewset router
router = DefaultRouter()
router.register('', views.EventViewSet)


# route: event/
app_name = 'event'
urlpatterns = [
    path('', include(router.urls)),
]