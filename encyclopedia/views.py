from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages

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

class newEntryForm(forms.Form):
    title = forms.CharField(label = "New Entry Title", max_length = 100)
    content = forms.CharField(label = "New Entry Content", widget = forms.Textarea)

def newEntry(request):
    return render(request, "encyclopedia/newEntry.html", {
        "form":newEntryForm(),
    })

def addEntry(request):
    if request.method == "POST":
        form = newEntryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title):
                messages.error(request, f'{title} already exists!')
                return render(request, "encyclopedia/newEntry.html", {
                    "form":newEntryForm(),
                })
            util.save_entry(title,content)
            messages.success(request, f'{title} was successfully saved!')
        else:
            messages.error("Form request not valid. Try again.")
            return render(request, "encyclopedia/newEntry.html", {
                "form":newEntryForm(),
            })
    return redirect(reverse('display_entry', args = [title]))

def editEntry(request, title):
    return render(request, "encyclopedia/editEntry.html")

def randomPage(request):
    title = random.choice(util.list_entries())
    return redirect(reverse('display_entry', args = [title]))