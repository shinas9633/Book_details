from django import forms
from work.models import Emp
from work.models import Book
from work.models import Movies
from work.models import Person
from work.models import Student

class Empform(forms.Form):
    name = forms.CharField(max_length=20)
    place = forms.CharField()
    salary = forms.CharField()
    contact = forms.CharField() 

class Bookform(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    publication_year = forms.IntegerField()
    genre = forms.CharField()

class MoviesForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields='__all__'


class PersonForm(forms.ModelForm):
    class Meta():
        model=Person
        fields='__all__'

class StudentForm(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'
