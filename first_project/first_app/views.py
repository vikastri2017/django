from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    #return HttpResponse("Hello World!")
    #return HttpResponse("Hello World!")
    my_dict = {'insert_me':"Hello I am free from views.py!"}
    return render(request, 'index.html', context=my_dict)
