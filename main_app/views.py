from django.shortcuts import render
from django.views.generic import ListView
from .models import Finch


# Add the Cat class & list and view function below the imports
# class Finch:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, description, age):
#     self.name = name
#     self.description = description
#     self.age = age

# finches = [
#     Finch('Fred', 'Speedy little thing', 3),
#     Finch('Marco', 'Tiny little Yellow Finch', 0),
# ]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def finches_index(request):
#     return render(request, 'finches/index.html', {"finches": finches})

class FinchList(ListView):
  model = Finch
  template_name = 'finches/index.html'

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', {'finch': finch})
