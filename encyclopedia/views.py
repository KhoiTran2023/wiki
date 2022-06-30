from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

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
    if get_entry(title) is not None:
        return render(request, "encyclopedia/entry.html", {
            "title":title,
            "content":markdown2.markdown(get_entry(title)),
        })
    return HttpResponseRedirect(reverse('encyclopedia:search_results'))

def displayResults(request):
    return render(request, "encyclopedia/search.html", {
        "content":list_entries(),
    })