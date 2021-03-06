from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
# Create your views here.



class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username= data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only comntain alphanumeric character'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Sorry username is  use,choose another one'},status=409)    
        return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')        
        