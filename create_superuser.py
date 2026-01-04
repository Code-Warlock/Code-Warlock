import os
import django
from django.contrib.auth import get_user_model


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


User = get_user_model()
USERNAME = 'Warlock'           
EMAIL = 'code@warlock.com'  
PASSWORD = 'Krampusa_kradonga123'   

if not User.objects.filter(username=USERNAME).exists():
    print(f"Creating superuser: {USERNAME}")
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superuser created successfully!")
else:
    print("Superuser already exists. Skipping.")