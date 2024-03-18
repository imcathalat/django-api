from django.urls import path
from snippets import views

urlspatterns = [
    path('snippets/', views.snippet_list),
    path('snippet/<int:pk>', views.snippet_detail)
]