# djando_second_project
Assistant for beginners

django-admin startproject mysite 
python manage.py runserver 192.168.1.1:5000 
python manage.py startapp news
python manage.py makemigrations     "migration to the list migrations"
python manage.py sqlmigrate news 0001   "show migrates"
python manage.py migrate    "migration to the database"
python manage.py shell      "python shell in venv"



Django ORM

Create
from news.models import News        "import model"
News(title='Новость 1', content = 'Контент новости 1' )     "create content"
news1 = _       "Алдыңғы командаға теңестіру"
news1.save()        "save content"
from django.db import connection        "import for show contents"
connection.queries          "command for show contents"
news2 = News.objects.create(title = 'Новость 3', content = 'Контент новости 3')        "immediately save content"  

Read 
News.objects.all()          "select  all contents in database"
News.objects.filter(title="News 5")         "select after filtering"
News.objects.get(pk=5)              "select only one content "

Update
News.objects.get(pk=4)
news4=_
news4.title="News 4"        "update title"
news4.save()                "Save the updated"

Delete
news4=News.objects.get(pk=4)    "select 1 content"  
news4.delete()                  "delete selected"






