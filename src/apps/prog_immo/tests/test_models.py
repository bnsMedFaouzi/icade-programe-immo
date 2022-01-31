import pytest
from apps.prog_immo.models import Program, Apartment


@pytest.mark.django_db
def test_create_program(db):
    program = Program.objects.create(name='test program', is_active=True)
    assert program.is_active is True
    assert program.name == 'test program'


@pytest.fixture
def program(db) -> Program:
    return Program.objects.create(name='test program', is_active=True)


def test_filter_program(program):
    assert Program.objects.filter(name='test program').exists()


@pytest.mark.django_db
def test_create_apartment(db, program):
    apartment = Apartment.objects.create(
        area=80,
        price=100000.0,
        nb_rooms=4,
        characteristics=['proche station ski', 'piscine', 'jardin', 'cave', 'parking', ],
        program=program
    )
    assert apartment.id
