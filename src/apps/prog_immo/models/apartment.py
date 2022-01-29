from django.contrib.postgres.fields import ArrayField
from django.db import models
from .program import Program


class Apartment(models.Model):
    """
        This class contains all the information about an Apartment. As Apartment is belongs to a single program.

        Attributes
        ----------
        area: models.IntegerField
            This is the area of the Apartment.
        price: models.FloatField
            This is the price of the Apartment.
        nb_rooms: models.IntegerField
            This is the number rooms in the Apartment.
        characteristics: models.ArrayField
            These are the characteristics of the Apartment.
            example : [proche station ski, piscine, jardin, cave, parking, ...].

        program: models.ForeignKey
            To specify if the program is available.
        """
    # class private attributes

    # class attributes

    # Constant attributes

    # Basic Field
    area = models.IntegerField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    nb_rooms = models.IntegerField(blank=False, null=False)
    characteristics = ArrayField(models.CharField(max_length=200), blank=False, null=False)
    # relation Fields
    program = models.ForeignKey(Program, null=False, blank=False, on_delete=models.CASCADE)

    # class Meta attributes
    def __str__(self):
        return f"{self.program} - {self.area} M² - {self.nb_rooms} of rooms."

    # overload python object methods

    # overload django methods

    # custom methods

    # django signal methods
