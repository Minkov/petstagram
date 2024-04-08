from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Directories on the file system
STATICFILES_DIRS = (
    BASE_DIR / "staticfiles",
)

STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

# URL prefix in the client
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / 'mediafiles'

MEDIA_URL = "/media/"
