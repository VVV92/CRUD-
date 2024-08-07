from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            return HttpResponse(f'<h2>Hello, {name}</h2>')
        else:
            return HttpResponse('Invalid data')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})