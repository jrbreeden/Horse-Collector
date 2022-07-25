from django.shortcuts import render

# Create your views here.


# Add the Horse class & list and view function below the imports
class Horse:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

horses = [
  Horse('Paint', 'American Paint', 'friendly', 3),
  Horse('Spot', 'Appaloosa', 'fiery', 0),
  Horse('Blacky', 'American Quarter', 'runner', 4)
]





def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def horses_index(request):
  return render(request, 'horses/index.html', { 'horses': horses })