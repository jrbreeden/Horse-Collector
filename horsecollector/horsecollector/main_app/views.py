from django.shortcuts import render, redirect

# Create your views here.
from .models import Horse, Toy
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def horses_index(request):
  horses = Horse.objects.all()
  return render(request, 'horses/index.html', { 'horses': horses })

def horses_detail(request, horse_id):
  horse = Horse.objects.get(id=horse_id)
  feeding_form = FeedingForm()
  return render(request, 'horses/detail.html', { 'horse': horse, 'feeding_form': feeding_form })


class HorseCreate(CreateView):
  model = Horse
  fields = ['name', 'breed', 'description', 'age']
  
class HorseUpdate(UpdateView):
  model = Horse
  fields = ['breed', 'description', 'age']

class HorseDelete(DeleteView):
  model = Horse
  success_url = '/horses/'

def add_feeding(request, horse_id):
  # create a ModelForm instance using the data in the posted form
  form = FeedingForm(request.POST)
  # validate the data
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.horse_id = horse_id
    new_feeding.save()
  return redirect('detail', horse_id=horse_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'