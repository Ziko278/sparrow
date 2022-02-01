from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic.detail import DetailView
from sparrow_admin.models import SchoolsModel
from user.models import UserRoleModel


# Create your views here.
def user_create_view(request, pk):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        pk = request.POST['pk']

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters')
            return redirect(f'../create/{pk}')

        if password != confirm_password:
            messages.error(request, 'Password do not match')
            return redirect(f'../create/{pk}')

        user = User.objects.create_user(username=username, password=password)
        user.is_active = True
        user.save()

        if user.id:
            school = SchoolsModel.objects.get(pk=pk)
            school.status = 'active'
            school.save()

            user_role = UserRoleModel.objects.create(user=user, role='school_super_admin', school=school)
            user_role.save()
            if user_role.id:
                messages.success(request, 'Your School Account Has been Successfully Activated')
                return redirect('../sign-in')
            else:
                messages.warning(request, 'success')
                return redirect('../sign-in')
        else:
            messages.error(request, 'failed')

    context = {
        'pk': pk
    }
    return render(request, 'user/create.html', context=context)


def user_sign_in_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_role = UserRoleModel.objects.filter(user=user)[0]
            request.session['user_school_id'] = user_role.school.id
            request.session['user_role'] = user_role.role
            messages.success(request, 'welcome back ' + user_role.school.name)
            return redirect(f'../../admin/{user_role.school.id}')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('user:login')

    return render(request, 'user/sign_in.html')


def logoutUser(request):
    logout(request)
    return redirect('user:login')


