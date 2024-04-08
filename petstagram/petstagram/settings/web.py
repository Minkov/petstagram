import os

# Example env variable: `ALLOWED_HOSTS=localhost 127.0.0.1`
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(" ")
CSRF_TRUSTED_ORIGINS = [f'https://{host}' for host in ALLOWED_HOSTS]