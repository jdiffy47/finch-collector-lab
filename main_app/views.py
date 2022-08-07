from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, color, sound, age):
    self.name = name
    self.color = color
    self.sound = sound
    self.age = age

finches = [
  Finch('Lolo', 'tabby', 'Kinda rude.', 3),
  Finch('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Finch('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Finch('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]



# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })