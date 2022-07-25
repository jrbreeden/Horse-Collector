from django.db import models

# Create your models here.
# Add the Cat class & list and view function below the imports
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