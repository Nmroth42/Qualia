from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from taskerapp.forms import UserForm, TaskForm, UserFormForEdit
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return redirect(task_home)

@login_required(login_url='/task/sign-in/' )
def task_home(request):
    return render(request, 'task/home.html', {})

@login_required(login_url='/task/sign-in/' )
def task_account(request):
    user_form = UserFormForEdit(instance = request.user)
    task_form = TaskForm(instance = request.user.task)

    return render(request, 'task/account.html', {
        "user_form": user_form,
        "task_form": task_form
    })

def task_sign_up(request):
    user_form = UserForm()
    task_form = TaskForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        task_form = TaskForm(request.POST, request.FILES)

        if user_form.is_valid() and task_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_task = task_form.save(commit=False)
            new_task.user = new_user
            new_task.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(task_home)

    return render(request, 'task/sign_up.html', {
        "user_form": user_form,
        "task_form": task_form
    })
    
