from django.urls import path
from .views import (
	NoteCreateView, 
	NoteDeleteView, 
	NoteDetailView, 
	NoteListView,
	NoteUpdateView,

)

app_name = 'notes'
urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('<int:id>/', NoteDetailView.as_view(), name='note-detail'),
    path('<int:id>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('<int:id>/delete', NoteDeleteView.as_view(), name='note-delete'),
]
