from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
        else:
            messages.error(request, "Invalid username or password.")
        return redirect("home")
    else:
        records = Record.objects.all()
        return render(request, "home.html", {"records": records})


def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")


def user_register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            raw_password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f"Account created for {username}!")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})


def record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, "record.html", {"record": record})
    else:
        messages.error(request, "You must be logged in to view that page.")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record deleted successfully.")
        return redirect("home")
    else:
        messages.error(request, "You must be logged in to delete a record.")
        return redirect("home")


def add_record(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect("home")
        return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Has Been Updated!")
                return redirect("home")
        return render(request, "update_record.html", {"form": form, 'record': record})
    else:
        messages.error(request, "You Must Be Logged In...")
        return redirect("home")