web: gunicorn Alto.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn Alto.wsgi