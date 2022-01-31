# python lib
# django lib
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# custom lib

from ..models import Apartment
from ..serializers import ApartmentSerializer


class ApartmentCreateListAPIView(generics.ListCreateAPIView):
    """
        Returns a list of all Apartment.
        Create new Apartment.
    """
    queryset = Apartment.objects
    permission_classes = [IsAuthenticated]
    serializer_class = ApartmentSerializer
