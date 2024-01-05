from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_album(request):
    if request.method == 'POST':
        album_form = forms.albumForm(request.POST)
        if album_form.is_valid():
            album_form.instance.author = request.user
            album_form.save()
            return redirect('post')
    
    else:
        album_form = forms.albumForm()
    return render(request, 'album.html', {'form' : album_form})

def edit(request, id):
    posts = models.albums.objects.get(pk=id)
    album_form = forms.albumForm(instance=posts)
    if request.method == 'POST':
        album_form = forms.albumForm(request.POST, instance=posts)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request, 'album.html', {'form' : album_form})

def delete(request,id):
    posts = models.albums.objects.get(pk=id)
    posts.delete()
    return redirect('home')