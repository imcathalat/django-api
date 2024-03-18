from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippet/<int:pk>', views.snippet_detail)
]

urlspatterns = format_suffix_patterns(urlpatterns)