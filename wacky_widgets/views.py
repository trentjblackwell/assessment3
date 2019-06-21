from django.shortcuts import render
from .models import Widget
from .forms import WidgetForm
from django.shortcuts import render, redirect

def home(request):
  if request.method == 'POST':
    form = WidgetForm(request.POST)
    if form.is_valid():
      user = form.save()
      return redirect('home')
  widgets = Widget.objects.all()
  form = WidgetForm()
  context = {'widgets': widgets, 'form': form}
  return render(request, 'home.html', context)

def Delete(request, widget_id):
   Widget.objects.get(id=widget_id).delete()
   return redirect('home') 

