from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Data object storing all address details

    Attributes
    -------
    number: int
        the street number of the address

    street: str
        the street of the address

    state: str
        the state of the address (2 digits)

    zip_code: int
        the zip code of the address (int between 0 and 99999)

    country_iso_code: str
        iso code of the address's country (3 chars)
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

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

    Attributes
    -------
    title : str
        the title of the letting

    address : Address
        A reference to an Address object
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Gives a string representation of a Letting Object.
        """
        return self.title
