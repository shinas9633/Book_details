from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import Empform
from work.models import Emp
from work.models import Book
from work.forms import Bookform
from work.models import Movies
from work.forms import MoviesForm
from work.forms import PersonForm
from work.forms import StudentForm
from work.models import Student



class Employee(View):
   def get(self,request):
      form=Empform()
      return render(request,"add.html", {"form":form})
  
   def post(self,request):
      form=Empform(request.POST)

      if form.is_valid():
         print(form.cleaned_data)
         Emp.objects.create(**form.cleaned_data)
         return render(request,"add.html", {"form":form})
      
      else:
         return render(request,"add.html", {"form":form})
      
class BookView(View):
   def get(self,request):
      form=Bookform()
      return render(request,"book.html",{"form":form})
   
   def post(self,request):
      form=Bookform(request.POST)

      if form.is_valid():
         print(form.cleaned_data)
         Book.objects.create(**form.cleaned_data)
         return render(request,"book.html",{"form":form})
      
      else:
         return render(request,"book.html",{"form":form})
      
class MoviesView(View):
   def get(self,request):
      form=MoviesForm()
      return render(request,"movie.html",{"form":form})
   
   def post(self,request):
      form=MoviesForm(request.POST)

      if form.is_valid():
         print(form.cleaned_data)
         Movies.objects.create(**form.cleaned_data)
         return render(request,"movie.html",{"form":form})
      else:
         return render(request,"movie.html",{"form":form})


class Booklist(View):
   def get(self,request):
      qs=Book.objects.all()
      return render(request,"booklist.html",{"qs":qs})
   

class PersonView(View):
   def get(self,request):
      form=PersonView()
      return render(request,"person.html",{"form":form})
   
   def post(self,request):
      form=PersonForm(request.POST)

      if form.is_valid():
         form.save()
         print("created")

         return render(request,"person.html",{"form":form})
      else:
         return render(request,"person.html",{"form":form})
      
class Book_detailView(View):

   def get(self,request,*args,**kwargs):
      print(kwargs)

      id=kwargs.get("pk")
      qs=Book.objects.get(id=id)
      return render(request,"bookd.html",{"data":qs})
   
class StudentView(View):

   def get(self,request):
      form=StudentForm()
      return render(request,"student.html",{"form":form})
   
   def post(self,request):
      form=StudentForm(request.POST)
      
      if form.is_valid():
         print(form.cleaned_data)
         Student.objects.create(**form.cleaned_data)
         return render(request,"student.html",{"form":form})
      else:
         return render(request,"student.html",{"form":form})
      

class Student_detailView(View):

   def get(self,request,*args,**kwargs):
      print(kwargs)

      id=kwargs.get("pk")
      qs=Student.objects.get(id=id)
      return render(request,"studentd.html",{"data":qs})
   

class Book_delete(View):
   def get(self,request,*args,**kwargs):
      id=kwargs.get("pk")
      Book.objects.get(id=id).delete()
      return redirect('book-al')
      



