from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms

from . import util
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

class EditText(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={
      "placeholder": "Your entry goes here"
    }))

def displayEntry(request, title):
    if util.get_entry(title) is not None:
        return render(request, "encyclopedia/entry.html", {
            "title":title,
            "content":markdown2.markdown(util.get_entry(title)),
        })
    return render(request, "encyclopedia/error.html")

def displayResults(request):
    if request.method == "POST":
        title = request.POST["q"]
        if util.get_entry(title):
            return redirect(reverse('display_entry', args = [title]))
        else:
            entries = []
            for i in util.list_entries():
                if title.lower() in i.lower():
                    entries.append(i)
    return render(request, "encyclopedia/search.html", {
        "content":entries,
    })

def newEntry(request):
    return render(request, "encyclopedia/newEntry.html")

def editEntry(request, title):
    return render(request, "encyclopedia/editEntry.html")

def randomPage(request):
    title = random.choice(util.list_entries())
    return redirect(reverse('display_entry', args = [title]))