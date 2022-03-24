import os


def is_production():
    return os.getenv('APP_ENVIRONMENT') == 'Production'


def is_development():
    return os.getenv('APP_ENVIRONMENT') == 'Development'
