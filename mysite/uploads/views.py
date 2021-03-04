from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.files.storage import FileSystemStorage
import ipdb

from .forms import FileForm, PersonForm
from .models import Person, File


# class IndexView(generic.ListView):
#     model = Person
#     template_name = 'index.html'
#     context_object_name = 'Home page du site Upload de fichiers'


"""
Page d'accueil et de connexion pour une personne, ce qui l'ajoute à l'admin.
"""


def index(request):

    if request.method == "POST":
        form = PersonForm(request.POST)
        person = Person()
        if form.is_valid():
            form.save()
        return render(request, "index.html", {"form": form})
    else:
        form = PersonForm()
    return render(request, "index.html", {"form": form})


def list_person(request):
    person = Person()
    list_person = []
    list_person = get_list_or_404(Person)
    return render(request, "list_person.html", {'person': person})


"""
Page d'upload des fichiers avec modèle POST obligatoire. Si c'est GET, renvoi un formulaire vide et retourne le gabarit pour recommencer.
"""


def upload(request):

    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, "list_upload.html", {"form": form})
    else:
        form = FileForm()
    return render(request, "upload.html", {"form": form})


"""
    def upload(request):
        context = {}
        if request.method == 'POST':
            uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        return render(request, 'upload.html', context)"""


def list_file(request):
    
    return render(request, "list_file.html")