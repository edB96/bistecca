from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from .forms import RegistrationForm, AdeguataForm, AnagraficaForm
from .models import UserRole
from django.contrib import messages



# Create your views here.


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Login the user and redirect to the appropriate page
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_after(request):
    auth.logout(request)
    return redirect('index')

def logout_view(request):
    return render(request, 'logout.html')

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_role = UserRole.objects.create(user_id=user.id, role=request.POST['role'])
            user_role.save()

            # Redirect to success page
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)

def add_deal_adeguata(request):
    form = AdeguataForm()
    context = {'form': form}
    return render(request, 'add_deal/add_deal_adeguata.html', context)

def add_deal_anagrafica(request):
    form = AnagraficaForm()
    context = {'form': form}
    return render(request, 'add_deal/add_deal_anagrafica.html', context)

def registration_success(request):
    return render(request, 'registration_success.html')

def upload_files(request):
    return render(request, 'upload_files.html')


def search_results(request):
    messages.info('CIAO CIAO')
    return render(request, 'search_results.html')