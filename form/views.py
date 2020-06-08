from django.shortcuts import render
from .forms import MarkyticsForms
from django.http import HttpResponseRedirect
from django.urls import reverse


def createForm(request):   
    if request.method == 'POST':
        form = MarkyticsForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('create-form'))
        else:
            return render(request, 'form/create_form.html', {'form': form})
    else:
        form = MarkyticsForms()
        return render(request, 'form/create_form.html' , {'form': form})
  