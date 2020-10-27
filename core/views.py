from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views import View


class HomePage(View):
    def get(self,request):
        return render(request,'core/home.html')