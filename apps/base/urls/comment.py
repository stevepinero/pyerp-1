"""The store routes
"""
# Librerias Django
from django.urls import path

# Librerias en carpetas locales
from ..views.comment import (
    CommentCreateView, CommentDeleteView, CommentDetailView, CommentListView,
    CommentUpdateView)

app_name = 'PyComment'

urlpatterns = [
    path('', CommentListView.as_view(), name='list'),
    path('add/', CommentCreateView.as_view(), name='add'),
    path('<int:pk>/', CommentDetailView.as_view(), name='detail'),
    path('<int:pk>/update', CommentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='delete'),
]
