from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# When user sends http request at endpoint (URL), index function = returns response
def index(request):
    return HttpResponse("Hello There")
