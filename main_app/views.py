from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = "about.html"


class AlbumsList(TemplateView):
    template_name = "albums_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
                context['albums'] = Album.objects.filter(name__icontains=name)
                context["header"] = f"Searching for {name}"
        else:
                context['albums'] = Album.objects.all()
                context["header"] = "Matt's Favorite Albums"
        return context


class AlbumCreate(CreateView):
    model = Album
    fields = ['name', 'artist', 'image', 'info']
    template_name = "album_create.html"
    def get_success_url(self):
        return reverse('album_detail', kwargs={'pk': self.object.pk})

class AlbumDetail(DetailView):
    model = Album
    template_name = "album_detail.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['name', 'artist', 'image', 'info']
    template_name = "album_update.html"
    def get_success_url(self):
        return reverse('album_detail', kwargs={'pk': self.object.pk})

class AlbumDelete(DeleteView):
    model = Album
    template_name = "album_delete_confirmation.html"
    success_url = '/albums/'
