from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import Compte


User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        return redirect('compte')        
    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')
    

def compte_user(request):
	compte = get_object_or_404(Compte, user=request.user)
	return render (request,'accounts/compte.html', context={"compte": compte})


def users_list_view (request):
		user = User.objects.all()
		context = {'users': user}
		return render (request,'accounts/users_list.html', context)
