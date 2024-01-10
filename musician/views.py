from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from . import forms
from .models import MusicianModel
from django.urls import reverse_lazy
# Create your views here.

# add musicians
class Add_musicianView(CreateView):
    model = MusicianModel
    form_class = forms.Musician_form
    template_name = 'all_form.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        # form.instance.music = self.request.user
        return super().form_valid(form)
    

# edit music
class Update_musicianView(UpdateView):
    model = MusicianModel
    form_class = forms.Musician_form
    template_name = 'all_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')