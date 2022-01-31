from ..models import Program, Apartment
from .queryset_apartment import apartments_has_characteristic


def program_apartments_has_characteristic(characteristic: str = 'piscine'):
    """
    Select all program who have at least one apartment that contains a characteristic specified as a parameter.

    :param characteristic: to be used for the filter.
    :return: queryset of Program
    """
    apartments = apartments_has_characteristic(characteristic)
    programs_ids = apartments.values_list('program').distinct()

    return Program.objects.filter(id__in=programs_ids)
