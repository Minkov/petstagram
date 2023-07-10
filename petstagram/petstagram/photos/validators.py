from django.core.validators import ValidationError


def image_size_validator_5mb(image_object):
    max_size = 5 * 1024 * 1024

    if image_object.size > max_size:
        return ValidationError('Image size can not be larger than 5MB')


def text_underscore_validator(value):
    if '_' in value:
        raise forms.ValidationError('Text cannot contain underscore')


# validator - check if bad data
# clean_%s -
#       1. additional logic upon clean data - second validation (modify)
#               - now my value is ok
#               - do some stuff
#       2. additional operations upon clean data


# XSS, DB injection, CSRF, cookies