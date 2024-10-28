from django.core.exceptions import ValidationError


def name_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Your name must contain letters only!")


def only_digits_validator(value):
    for ch in value:
        if not ch.isdigit():
            raise ValidationError("Your passcode must be a combination of 6 digits")
