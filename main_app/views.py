from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Finch

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class FinchList(ListView):
  model = Finch
  template_name = 'finches/index.html'

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', {'finch': finch})
