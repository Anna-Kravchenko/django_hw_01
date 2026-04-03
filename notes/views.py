from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Note
from .forms import NoteForm, LoginForm, RegisterForm


class NoteListView(ListView):
    model = Note
    template_name = 'index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(user=self.request.user)
        else:
            return Note.objects.none()

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'
    context_object_name = 'note'


class NoteCreateView(CreateView):
    model = Note
    template_name = 'note_form.html'
    # fields = ['title', 'text', 'reminder', 'category']
    form_class = NoteForm
    success_url = reverse_lazy('notes_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'note_form.html'
    # fields = ['title', 'text', 'reminder', 'category']
    form_class = NoteForm
    success_url = reverse_lazy('notes_list')


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    context_object_name = 'note'
    success_url = reverse_lazy('notes_list')

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Hello, {username}')
                return redirect('notes_list')
            else:
                messages.error(request, 'Wrong login or password')

        return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration success')
            return redirect('notes_list')

        return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')
