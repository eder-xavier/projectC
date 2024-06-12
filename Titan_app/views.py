from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
#from .forms import CustomUserCreationForm, RegistrationCodeForm, UserProfileForm, NewsForm
#from .models import UserProfileTitan, News
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'titan/home/home.html')

def publications(request):
    return render(request, 'titan/mid/publications.html')

def extensions(request):
    return render(request, 'titan/mid/extensions.html')

def award_articles(request):
    return render(request, 'titan/mid/award_articles.html')
def team(request):
    return render(request, 'titan/mid/team.html')

#def registration_code(request):
#    if request.method == 'POST':
#        form = RegistrationCodeForm(request.POST)
#        if form.is_valid():
#            code = form.cleaned_data['registration_code']
#
#            if code == 'orion369':  # Verifica se o código é correto
#                request.session['registration_code_verified'] = True
#                messages.success(request, 'Código de registro verificado com sucesso.')
#                return redirect('Titan_app:signup')  # Redirecione para a página de registro
#            else:
#                messages.error(request, 'Código de registro incorreto. Tente novamente.')
#    else:
#        form = RegistrationCodeForm()
#
#    return render(request, 'titan/validation/registration_code.html', {'form': form})
#
#
#
#def signup(request):
#    if not request.session.get('registration_code_verified'):
#        return redirect('Titan_app:registration_code')
#
#    if request.method == 'POST':
#        form = CustomUserCreationForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            raw_password = form.cleaned_data.get('password1')
#            user = form.save()
#            
#            # Criação do UserProfile para o novo usuário
#            UserProfileTitan.objects.create(user=user)
#            
#            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#            #messages.success(request, "Sucesso!", extra_tags='success-message')
#
#            return redirect('Titan_app:login')  # Adapte conforme necessário
#    else:
#        form = CustomUserCreationForm()
#
#    return render(request, 'titan/validation/signup.html', {'form': form})
#
#
#def user_login(request):
#    if request.method == 'POST':
#        form = AuthenticationForm(data=request.POST)
#
#        if form.is_valid():
#            username = form.cleaned_data.get('username')
#            password = form.cleaned_data.get('password')
#            user = authenticate(username=username, password=password)
#    
#            if user:
#                login(request, user)
#                return redirect('Titan_app:view_profile', username=user.username)
#
#
#    else:
#        form = AuthenticationForm()
#
#    return render(request, 'titan/validation/login.html', {'form': form})
#
#
#@login_required
#def user_logout(request):
#    logout(request)
#    return redirect('Titan_app:home')
#
#
#
#@login_required
#def view_profile(request, username):
#    user_profile = get_object_or_404(UserProfileTitan, user__username=username)
#    is_owner = user_profile.user == request.user
#    user_news_list = News.objects.filter(user=user_profile.user).order_by('-created_at')
#
#    context = {
#        'user_profile': user_profile,
#        'is_owner': is_owner,
#        'user_news_list': user_news_list
#    }
#
#    return render(request, 'titan/home_admin/view_profile.html', context)
#
#@login_required
#def edit_profile(request):
#    user_profile, created = UserProfileTitan.objects.get_or_create(user=request.user)
#
#    if request.method == 'POST':
#        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
#        if form.is_valid():
#            form.save()
#            return redirect('Titan_app:view_profile', username=request.user.username)
#    else:
#        form = UserProfileForm(instance=user_profile)
#
#    return render(request, 'titan/home_admin/edit_profile.html', {'form': form})
#
#
#
#
#
#@login_required
#def create_news(request):
#    if request.method == 'POST':
#        form = NewsForm(request.POST, request.FILES)
#        if form.is_valid():
#            news = form.save(commit=False)
#            news.user = request.user
#            news.save()
#            return redirect('Titan_app:view_profile', username=request.user.username)
#    else:
#        form = NewsForm()
#
#    return render(request, 'titan/news/create_news.html', {'form': form})
#
#@login_required
#def edit_news(request, news_id):
#    news = get_object_or_404(News, id=news_id, user=request.user)
#
#    if request.method == 'POST':
#        form = NewsForm(request.POST, request.FILES, instance=news)
#        if form.is_valid():
#            form.save()
#            return redirect('Titan_app:view_profile')
#    else:
#        form = NewsForm(instance=news)
#
#    return render(request, 'titan/news/edit_news.html', {'form': form, 'news': news})
#
#@login_required
#def delete_news(request, news_id):
#    news = get_object_or_404(News, id=news_id, user=request.user)
#    news.delete()
#
#    # Adicione esta linha para redirecionar para a view_profile com o username correto
#    return redirect('Titan_app:view_profile', username=request.user.username)
#
#
#
#def public_news(request):
#    news_list = News.objects.all()
#
#    context = {
#        'news_list': news_list,  
#    }
#    return render(request, 'titan/mid/news.html', context)
