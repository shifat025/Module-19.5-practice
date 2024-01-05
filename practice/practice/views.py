from django.shortcuts import render
from album.models import albums

# Create your views here.

def home(request):
    data = albums.objects.all()
    return render(request,'home.html', {'data':data})
    # data = albums.objects.filter(author = request.user)
    # return render(request, 'home.html', {'data' : data})