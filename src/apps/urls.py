from django.urls import path, re_path, include


urlpatterns = [
    # re_path(r'^', include('apps.jwt_authentication.urls')),
    re_path(r'^', include('apps.prog_immo.urls')),
    re_path(r'^', include('apps.api_authentication.urls')),
]
