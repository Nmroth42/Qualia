from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from taskerapp.forms import UserForm, ProfileForm, UserFormForEdit, GigForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Gig, Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return redirect(task_home)

@login_required(login_url='/task/sign-in/' )
def task_home(request):
    gigs = Gig.objects.all().order_by("-create_time")
    paginator = Paginator(gigs, 9) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    
    return render(request, 'task/home.html', {"gigs": queryset})



@login_required(login_url='/task/sign-in/' )
def task_account(request):
    user_form = UserFormForEdit(instance = request.user)
    task_form = ProfileForm(instance = request.user.profile)

    return render(request, 'task/account.html', {
        "user_form": user_form,
        "task_form": task_form
    })

def task_sign_up(request):
    user_form = UserForm()
    task_form = ProfileForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        task_form = ProfileForm(request.POST, request.FILES)

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

def gig_detail(request, id):
    try:
        gig = Gig.objects.get(id=id)
    except Gig.DoesNotExist:
        return redirect('/')
    return render(request, 'task/gig_detail.html', {"gig":gig})

@login_required(login_url='/task/sign-in/' )
def create_gig(request):
    gig_form = GigForm()
    error = ''
    if request.method == "POST":
        gig_form = GigForm(request.POST, request.FILES )
        if gig_form.is_valid():
            gig = gig_form.save(commit=False)
            gig.user = request.user
            gig.save()
            return redirect(my_gigs)
        else:
            error = 'Data is not valid'
    return render(request, 'task/create_gig.html', {"gig_form":gig_form, "error":error})
      

@login_required(login_url='/task/sign-in/' )
def my_gigs(request):
    gigs = Gig.objects.filter(user = request.user)
    return render(request, 'task/my_gigs.html', {"gigs":gigs })

@login_required(login_url='/task/sign-in/' )
def profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        return redirect('/')
    return render(request, 'task/profile.html', {"profile":profile})


