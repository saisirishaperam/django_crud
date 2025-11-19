from django.shortcuts import render,redirect
from app1.forms import employe_forms
# Create your views here.
from app1.models import employe

def details(request):
    data = employe.objects.all()
    context = {
        'data' : data
    }

    return render(request, 'home.html', context)

def emp_form(request):
    form = employe_forms()
    if request.method == 'POST':
        form = employe_forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = employe_forms()
    context = {
        'form' : form
    }
    return render(request, 'from.html', context)