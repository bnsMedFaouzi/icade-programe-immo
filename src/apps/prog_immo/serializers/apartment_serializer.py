# python lib
# django lib
from rest_framework import serializers

# custom lib
from ..models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    program_name = serializers.SerializerMethodField()
    program_id = serializers.SerializerMethodField()

    class Meta:
        model = Apartment
        fields = (
            'area',
            'price',
            'nb_rooms',
            'characteristics',
            'program',
            'program_name',
            'program_id',
            'id'
        )
        extra_kwargs = {
            'program': {'required': True, 'write_only': True},
        }

        read_only_fields = ('id', 'program_id', 'program_name')

    def get_program_id(self, obj):
        return obj.program.id

    def get_program_name(self, obj):
        return obj.program.name
