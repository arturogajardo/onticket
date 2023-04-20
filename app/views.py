from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already taken'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })
    
@login_required 
def signout(request):
    logout(request)
    return redirect('home')

def events(request):
    events = Event.objects.all()
    return render(request, "events.html", {"events": events})

def create_event(request):
    if request.POST:
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('events')
    return render(request, "create_event.html", {"form": EventForm})

def cart(request):
    return render(request, "cart.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
