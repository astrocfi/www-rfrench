To clean up migrations:

python manage.py migrate --fake <app> zero
[Remove migration files except __init__.py]
python manage.py makemigrations
python manage.py migrate --fake-initial
