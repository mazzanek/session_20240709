from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('all_orders.html')
  return HttpResponse(template.render())