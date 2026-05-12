# ENTORNO Y GLOBALES

from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_ROOT = BASE_DIR.parent

env = environ.Env(
    DEBUG=(bool, False),
)

ENV_FILE = PROJECT_ROOT / '.env'

if ENV_FILE.exists():
    environ.Env.read_env(ENV_FILE)
else:
    raise RuntimeError(f'.env not found at {ENV_FILE}')

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'