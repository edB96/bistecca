from .models import UserRole

def user_role(request):
    user = request.user
    if user.is_authenticated:
        user_role = UserRole.objects.filter(user=request.user.id).first()
        if user_role.role=='seller':
            return {'user_role': 'seller'}
        elif user_role.role=='buyer':
            return {'user_role': 'buyer'}
        elif user_role.role=='partner':
            return {'user_role': 'partner'}
    return {}

def user_name(request):
    if request.user.is_authenticated:
        return {'user_name': request.user.username}
    return {}