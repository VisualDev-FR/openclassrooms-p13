from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Data object storing all address details
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    """ the street number of the address """

    street = models.CharField(max_length=64)
    """ the street of the address """

    city = models.CharField(max_length=64)
    """ the city of the address """

    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    """ the state of the address (2 digits) """

    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    """ the zip code of the address (int between 0 and 99999) """

    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )
    """ iso code of the address's country (3 chars) """

    def __str__(self):
        """
        Gives a string representation of an Address Object.
        """
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Data object storing letting informations
    """

    title = models.CharField(max_length=256)
    """ the title of the letting """
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    """ A reference to an Address object """

    def __str__(self):
        """
        Gives a string representation of a Letting Object.
        """
        return self.title
