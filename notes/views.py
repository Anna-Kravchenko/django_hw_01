from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = 'index.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'
    context_object_name = 'note'


class NoteCreateView(CreateView):
    model = Note
    template_name = 'note_form.html'
    fields = ['title', 'text', 'reminder', 'category']
    success_url = reverse_lazy('notes_list')


class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'note_form.html'
    fields = ['title', 'text', 'reminder', 'category']
    success_url = reverse_lazy('notes_list')


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    context_object_name = 'note'
    success_url = reverse_lazy('notes_list')