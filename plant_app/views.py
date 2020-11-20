from django.shortcuts import render, redirect
from .models import Plant
from .models import Water
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WaterForm

class PlantCreate(CreateView):
  model = Plant
  fields = "__all__"

class PlantDelete(DeleteView):
  model = Plant
  success_url = "/plants/"

class PlantUpdate(UpdateView):
  model = Plant
  fields = "__all__"


def home(request):
    return render(request, "about.html")

def about(request):
    return render(request, "about.html",)

def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', { 'plants': plants })


def plant_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)

  water_sets = plant.water_set.all()

  water_form = WaterForm()
  
  return render(request, 'plants/detail.html', 
  {'plant': plant, 'water_form': water_form})

def add_water(request, plant_id):
  # create a ModelForm instance using the data in request.POST
  form = WaterForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_water = form.save(commit=False)
    new_water.plant_id = plant_id
    new_water.save()
  return redirect('detail', plant_id=plant_id)