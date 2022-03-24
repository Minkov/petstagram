import os
import sys


def is_production():
    return os.getenv('APP_ENVIRONMENT') == 'Production'


def is_development():
    return os.getenv('APP_ENVIRONMENT') == 'Development'


def is_test():
    return len(sys.argv) > 1 and sys.argv[1] == 'test'
