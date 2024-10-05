from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/posts')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error':'username or password is wrong'})
    else:    
        return render(request, 'accounts/login.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {'error':'This Username Is Already Exist'})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'accounts/register.html', {'error':'This Email Is Already Exist'})
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    return redirect('/accounts/login')
        else:
            return render(request, 'accounts/register.html', {'error':'Please Enter Your Password Carefully'})
    else:
        return render(request, 'accounts/register.html')
        

def logout_user(request):
    logout(request)
    return redirect('/accounts/login')
                

