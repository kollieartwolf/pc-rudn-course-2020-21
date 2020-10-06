import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rudnpc_edu_2021.settings')

application = get_asgi_application()
