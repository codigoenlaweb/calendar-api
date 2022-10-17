from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from modules import events

urlpatterns = [
    # admin route
    path('admin/', admin.site.urls),

    # auth route
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),

    # event route
    path('event/', include('modules.events.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
