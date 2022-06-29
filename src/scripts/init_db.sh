SUPERUSER_USERNAME=sabbir1021
SUPERUSER_EMAIL=sabbir@gmail.com
SUPERUSER_PASSWORD=sabbireti1021

source venv/bin/activate
python manage.py makemigrations
python manage.py migrate

python manage.py shell -c "from django.contrib.auth.models import User; super_user = User.objects.create_superuser('$SUPERUSER_USERNAME', '$SUPERUSER_EMAIL', '$SUPERUSER_PASSWORD');"
