from django.db.models import F, Value, Q, Case, When
from django.db.models.functions import Concat
from ..models import Apartment


def apartment_active_program():
    """
    select all Apartments which belongs to an active program.
    :return: queryset of Apartment
    """
    return Apartment.objects.filter(program__is_active=True)


def apartment_price_between(min_price: float = 100000.0, max_price: float = 180000.0):
    """
    Select all apartments who have a price between min_price and max_price.

    :param min_price:
    :param max_price:
    :return:queryset of Apartment
    """
    # return Apartment.objects.filter(price__range=[min_price, max_price])
    return Apartment.objects.filter(Q(price__gte=min_price) & Q(price__lte=max_price))


def apartment_in_promotion(reduction: float = 0.05, suffix_program: str = 'PROMO SPECIALE'):
    """
    Select all apartments with adding promo_price and suffixing program name with suffix_program.

    :return:queryset of Apartment
    """
    new_price = 1 - reduction
    return Apartment.objects.annotate(
        price_promo=(F('price') * new_price),
        program_name_promo=Concat(F('program__name'), Value(' '), Value(suffix_program))
    )


def apartments_has_characteristic(characteristic: str = 'piscine'):
    """
    Select all apartments who have a characteristic specified as a parameter.

    :param characteristic: to be used for the filter.
    :return:queryset of Apartment
    """
    return Apartment.objects.filter(characteristics__contains=[characteristic])


def apartments_has_characteristic_first(characteristic: str = 'proche station ski'):
    """

    :param characteristic:
    :return:queryset of Apartment
    """
    return Apartment.objects.annotate(
        characteristic_on_top=Case(
            When(characteristics__contains=[characteristic], then=0),
            default=1
        ), ).order_by(
        'characteristic_on_top',
        '-price',
        '-area',
    )


def apartments_desc_price_dec_area():
    """
    Select all apartments order by dec price and dec area.

    :return:queryset of Apartment
    """
    return Apartment.objects.order_by(
        '-price',
        '-area',
    )
