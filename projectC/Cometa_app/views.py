from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from Titan_app.forms import CustomUserCreationForm, RegistrationCodeForm
from .models import UserProfileCometa
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'cometa/home/home.html')

@login_required
def home_admin(request):
    return render(request, 'cometa/mid/home_admin.html')


def registration_code(request):
    if request.method == 'POST':
        form = RegistrationCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['registration_code']

            if code == 'orion369':  # Verifica se o código é correto
                request.session['registration_code_verified'] = True
                messages.success(request, 'Código de registro verificado com sucesso.')
                return redirect('Cometa_app:signup')  # Redirecione para a página de registro
            else:
                messages.error(request, 'Código de registro incorreto. Tente novamente.')
    else:
        form = RegistrationCodeForm()

    return render(request, 'cometa/validation/registration_code.html', {'form': form})



def signup(request):
    if not request.session.get('registration_code_verified'):
        return redirect('Cometa_app:registration_code')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = form.save()
            
            # Criação do UserProfile para o novo usuário
            UserProfileCometa.objects.create(user=user)
            
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            #messages.success(request, "Sucesso!", extra_tags='success-message')

            return redirect('Cometa_app:login')  # Adapte conforme necessário
    else:
        form = CustomUserCreationForm()

    return render(request, 'cometa/validation/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print("User:", user)
            print("Username:", username)
            print("Password:", password)
        
            if user:
                login(request, user)
                return redirect('Cometa_app:home_admin')


    else:
        form = AuthenticationForm()

    return render(request, 'cometa/validation/login.html', {'form': form})
