import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'registro_control_eventos.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = 'admin'
password = 'useradmin'
email = 'admin@example.com'

u = User.objects.filter(username=username).first()
if not u:
    User.objects.create_superuser(username, email, password)
    print(f'Usuario "{username}" creado con password "{password}"')
else:
    u.set_password(password)
    u.is_superuser = True
    u.is_staff = True
    u.save()
    print(f'Usuario "{username}" actualizado con password "{password}"')
