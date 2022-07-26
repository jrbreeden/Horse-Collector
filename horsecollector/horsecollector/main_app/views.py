from django.shortcuts import render, redirect

# Create your views here.
from .models import Horse
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

def add_feeding(request, horse_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the horse_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.horse_id = horse_id
    new_feeding.save()
  return redirect('detail', horse_id=horse_id)


class HorseCreate(CreateView):
  model = Horse
  fields = '__all__'
  
class HorseUpdate(UpdateView):
  model = Horse
  fields = ['breed', 'description', 'age']

class HorseDelete(DeleteView):
  model = Horse
  success_url = '/horses/'