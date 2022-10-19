from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserTable.objects.get(email=email, password=password)
            if user.user_role == "Admin":
                messages.success(request, f'Welcome {str(user.name)}', 'alert-success')
                return render(request, 'userapp/admin.html', {'user':user})
            elif user.user_role == "Student":
                messages.success(request, f'Welcome {str(user.name)}', 'alert-success')
                return render(request, 'userapp/student.html', {'user':user})
            elif user.user_role == "Staff":
                messages.success(request, f'Welcome {str(user.name)}', 'alert-success')
                return render(request, 'userapp/staff.html', {'user':user})
            else:
                messages.success(request, f'Welcome {str(user.name)}', 'alert-success')
                return render(request, 'userapp/editor.html', {'user':user})
        except:
            return render(request, 'userapp/login.html', {"message": "invalid username or password"})
    return render(request, 'userapp/login.html')


def user_creation(request):
    template_name = 'userapp/user_creation.html'
    form = UserRegForm()
    context = {'form': form}
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            confirm_password = request.POST.get('confirm-password')
            password = str(data.password)
            if password == confirm_password:
                data.save()
                messages.success(request, 'User Details Successfully Added.', 'alert-success')
                return redirect('user_login')
            else:
                context = {'form': form, 'message':'Re Type Your Passsword'}
                messages.success(request, "Your Password Didn't Match", 'alert-danger')
                return render(request, template_name, context)

        else:
            context = {'form': form}
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    return render(request, template_name, context)