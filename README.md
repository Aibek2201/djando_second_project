# djando_second_project
Assistant for beginners

django-admin startproject mysite 
python manage.py runserver 192.168.1.1:5000 
python manage.py startapp news
python manage.py makemigrations     "migration to the list migrations"
python manage.py sqlmigrate news 0001   "show migrates"
python manage.py migrate    "migration to the database"
python manage.py shell      "python shell in venv"



from news.models import News        "import model"
News(title='Новость 1', content = 'Контент новости 1' )     "create content"
news1 = _       "Алдыңғы командаға теңестіру"
news1.save()        "save content"
from django.db import connection        "import for show contents"
connection.queries          "command for show contents"
news2 = News.objects.create(title = 'Новость 3', content = 'Контент новости 3')        "immediately save content"  

