from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class LoginView(View):
    def get(self,request):

        pass

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse('Logged In')
        else:
            return HttpResponse('Logged In Failed')

    # Return an 'invalid login' error message.

