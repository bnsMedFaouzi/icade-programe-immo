from django.db import models


class Program(models.Model):
    """
        This class contains all the information about a ICADE program immo. A Project is a collection of apartments.

        Attributes
        ----------
        name: models.CharField
            This is the name of the program.

        is_active: models.BooleanField
            To specify if the program is available.
        """
    # class private attributes

    # class attributes

    # Constant attributes

    # Basic Field
    name = models.CharField(max_length=12, blank=False, null=False)
    is_active = models.BooleanField(default=False)  # the program must be approved before being available

    # relation Fields

    # class Meta attributes
    def __str__(self):
        return self.name

    # overload python object methods

    # overload django methods

    # custom methods

    # django signal methods
