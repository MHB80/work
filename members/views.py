from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'Mmembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'Mmember': mymember,
  }
  return HttpResponse(template.render(context, request))
def main(request):
    maintempalte = loader.get_template('main.html')
    return HttpResponse(maintempalte.render())
def testing(request):
  mydata = Member.objects.all().order_by('firstname','id')
  template = loader.get_template('template.html')
  context = {
    'Mmembers': mydata,
  }
  return HttpResponse(template.render(context, request))