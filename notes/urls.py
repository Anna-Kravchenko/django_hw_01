from django.urls import path
from .views import NoteListView,NoteDetailView,NoteCreateView,NoteUpdateView,NoteDeleteView, login_view, register_view, logout_view

urlpatterns = [
    path('', NoteListView.as_view(), name='notes_list'),
    path('create/', NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]