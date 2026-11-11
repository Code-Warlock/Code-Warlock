import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings") 
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
USERNAME = 'admin'            
NEW_PASSWORD = 'Krampusa_Kradonga123'

try:
    user = User.objects.get(username=USERNAME)
    user.set_password(NEW_PASSWORD)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"Password updated successfully for {USERNAME}!")
except User.DoesNotExist:
    print(f"User {USERNAME} does not exist. Creating new superuser...")
    User.objects.create_superuser(USERNAME, 'dessymichaeltgp123@gmail.com', NEW_PASSWORD)
    print("New superuser created successfully!")