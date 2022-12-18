from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

finches = [
    Finch('Fred', 'Speedy little thing', 3),
    Finch('Marco', 'Tiny little guy', 0),
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Finch Collector Home PAge!</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {"finches": finches})
