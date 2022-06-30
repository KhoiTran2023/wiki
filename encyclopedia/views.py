from django.shortcuts import render

from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def displayEntry(request, title):
    mdfile = 
    return