python manage.py makemigrations api
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py loaddata user, sensor, location, device, reading, recording
