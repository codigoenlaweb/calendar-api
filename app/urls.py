from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from modules import events
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# swagger function
schema_view = get_schema_view(
   openapi.Info(
      title="Doc Calendar API",
      default_version='v1',
      description="Public documentation from Caelendar Restfull API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="codeenlaweb@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # admin route
    path('admin/', admin.site.urls),

    # auth route
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),

    # event route
    path('event/', include('modules.events.urls')),

    # swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
