from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.displayEntry, name = "display_entry"),
    path("search-results", views.displayResults, name = "display_results"),
]
