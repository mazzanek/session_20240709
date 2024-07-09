from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import OrdersForm
from django.shortcuts import render

def home(request):
  template = loader.get_template('all_orders.html')
  return HttpResponse(template.render())

def water_order(request):
  template = loader.get_template('water_order.html')
  if request.method == 'POST':
    form = OrdersForm(request.POST)
    if form.is_valid():
      firstname = form.cleaned_data['firstname']
      lastname = form.cleaned_data['lastname']
      address = form.cleaned_data['address']
      form.save()
    return render(request, 'master.html')
  else:
    form = OrdersForm()
  return render(request, 'water_order.html', {'form': form})

def list_orders(request):
  template = loader.get_template('list_orders.html')
  return HttpResponse(template.render())