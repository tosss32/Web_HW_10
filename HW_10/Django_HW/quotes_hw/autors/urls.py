
from .views import list_authors
from django.urls import path


urlpatterns = [
    # ...
    path('', list_authors),
    # ...
]