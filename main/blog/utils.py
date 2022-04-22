from django.core.validators import RegexValidator


def phone_validation():
    phone_regex = RegexValidator(
        regex=r"^\+\d{2,3}\-\d{9,11}$",
        message="format: '+999-999999'. Up to 17 digits allowed.",
    )
    return phone_regex
