from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all()
    return JsonResponse({'users': list(users.values())})
