from django.shortcuts import render
from django.views.generic import ListView
from .models import Finch

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class FinchList(ListView):
  model = Finch
  template_name = 'finches/index.html'

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', {'finch': finch})
