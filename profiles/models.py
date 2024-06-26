from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Data object storing the tenants Profile informations.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """
    A reference to an user
    """
    favorite_city = models.CharField(max_length=64, blank=True)
    """
    A string representing the favorite city of the user
    """

    def __str__(self):
        """
        Gives a string representation of a Profile Object.
        """
        return self.user.username
