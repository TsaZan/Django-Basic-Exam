from django.core.validators import MinLengthValidator
from django.db import models

from furryFunnies.validators import name_validator, only_digits_validator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(4), name_validator],
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2),
                    name_validator],
        verbose_name="Last Name",
    )

    passcode = models.CharField(
        max_length=6,
        validators=[MinLengthValidator(6, "Your passcode must be exactly 6 digits!"),
                    only_digits_validator],
        help_text="Your passcode must be a combination of 6 digits",
    )

    pets_number = models.PositiveSmallIntegerField(
        verbose_name="Pets Number",
    )

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Profile Image URL",
    )
