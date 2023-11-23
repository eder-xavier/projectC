from .models import CustomUserTitan

def user_profile(request):
    if request.user.is_authenticated:
        user_profile = CustomUserTitan.objects.get(username=request.user.username)
        return {'user_profile': user_profile}
    return {}