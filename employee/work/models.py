from django.db import models

class Employee(models.Model):
    uname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.uname


# env\Scripts\activate.bat

# django-admin staartproject  projectname

#python manage.py runserver

# #python manage.py startapp appname 

# python manage.py makemigrations

# python manage.py migrate

# django default db sqlite3

# python manage.py shell

# from work.models import Employee

# Employee.objects.create(name="",age="")

# Models: which is used to perform certain using data. eg;CRUD (create,read/retrieve,update,delete)

class Student2(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    email=models.EmailField(unique=True,null=True)
    place=models.CharField(max_length=30)    
    gender=models.CharField(max_length=6)

    def __str__(self):
        return self.name
    def __str__(self):
        return self.age
    def __str__(self):
        return self.place
    


class Emp(models.Model):

    name=models.CharField(max_length=20)
    place=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()
    contact=models.CharField(max_length=30)




class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publication_year=models.PositiveIntegerField()
    genre=models.CharField(max_length=30)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.author
    
    def __str__(self):
        return self.genre
    

    

class Movies(models.Model):
    Movie=models.CharField(max_length=30)
    Year=models.PositiveIntegerField()
    Genre=models.CharField(max_length=30)


class Person(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=False,null=True)
    course=models.CharField(max_length=30)

class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=False,null=True)
    course=models.CharField(max_length=30)


    

# python manage.py shell

# s=modelname.objects.all()
# s
