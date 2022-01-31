from django.urls import path

from . import views

urlpatterns = [
    # Apartment routes
    path(r'apartments', views.ApartmentCreateListAPIView.as_view()),
]
