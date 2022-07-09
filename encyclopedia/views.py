from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms

from . import util
import markdown2

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
        entries = []
        for i in util.list_entries():
            if title in i:
                entries.append(title)
    return render(request, "encyclopedia/search.html", {
        "content":entries,
    })