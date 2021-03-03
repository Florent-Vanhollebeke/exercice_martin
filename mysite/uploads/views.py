from django.shortcuts import render, get_object_or_404
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


def index(request):

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "index.html", {"form": form})
    else:
        form = PersonForm()
    return render(request, "index.html", {"form": form})


def upload(request):

    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, "list_file.html", {"form": form})
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


def list_person(request, uuid):
    
    if uuid < 1:
        return 0
    listing = [] 
    for person in uuid:
        listing.append(person.listing)
    return (request, "list_person.html")

def get_queryset(self):
    return Person.objects.all()


def list_file(request):
    return HttpResponseRedirect("list_file")
