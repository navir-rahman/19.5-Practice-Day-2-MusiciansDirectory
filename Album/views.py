from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.decorators import login_required

# @method_decorator(login_required, name='dispatch')
class AlbumView(CreateView):
    model = models.AlbumModel
    form_class = forms.Album_from
    template_name = 'all_form.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        # form.instance.album = self.request.user
        return super().form_valid(form)
    
class UpdateAlbum(UpdateView):
    model = models.AlbumModel
    form_class = forms.Album_from
    template_name = 'all_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    
class DeleteAlbum(DeleteView):
    model = models.AlbumModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')