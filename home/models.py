from django.db import models

# -> python manage.py makemigrations (make file for changes in DB/models)
# -> for detection of changes do 2 things register admin in (proj/admin.py) second in app.py copy name and paste into setting.py
# -> python mange.py migrate (impliment migration file into db)
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=112)
    email = models.EmailField(max_length=112)
    phone=models.PositiveIntegerField(max_length=12)
    msg=models.CharField(max_length=300)
    date=models.DateField()

    def __str__(self):
        return self.name

