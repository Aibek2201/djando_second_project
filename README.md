# djando_second_project
Assistant for beginners

django-admin startproject mysite 
python manage.py runserver 192.168.1.1:5000 
python manage.py startapp news
python manage.py makemigrations
python manage.py sqlmigrate news 0001
python manage.py migrate

>>> news2 = News(title='Новость 2', content = 'Контент новости 2' )
>>> news2.save()
from django.db import connection
connection.queries
News.objects.create(title = 'Новость 3', content = 'Контент новости 3') 

