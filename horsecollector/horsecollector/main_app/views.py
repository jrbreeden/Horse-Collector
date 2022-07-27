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
  # Get the toys the horse doesn't have...
  # First, create a list of the toy ids that the horse DOES have
  id_list = horse.toys.all().values_list('id')
  # Now we can query for toys whose ids are not in the list using exclude
  toys_horse_doesnt_have = Toy.objects.exclude(id__in=id_list)
  # instantiate FeedingForm to be rendered in the detail.html template
  feeding_form = FeedingForm()
  return render(request, 'horses/detail.html', { 
    'horse': horse, 
    'feeding_form': feeding_form, 
    'toys': toys_horse_doesnt_have
    })


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

def assoc_toy(request, horse_id, toy_id):
  Horse.objects.get(id=horse_id).toys.add(toy_id)
  return redirect('detail', horse_id=horse_id)