from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.displayEntry, name = "display_entry"),
    path("wiki/<str:title>/edit", views.editEntry, name = "edit_entry"),
    path("edit", views.saveEntry, name = "save_entry"),
    path("search-results", views.displayResults, name = "display_results"),
    path("new-entry", views.newEntry, name = "new_entry"),
    path("new-entry/response", views.addEntry, name = "add_entry"),
    path("random-page", views.randomPage, name = "random_page"),
]
