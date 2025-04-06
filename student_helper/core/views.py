import calendar
from django.shortcuts import render, redirect
from django.http import HttpResponse
print("Importing Task model")
from .models import Task
from core.models import Task
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})
@login_required
def home(request):
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Helper - Home</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #f4f9ff;
            color: #333;
            text-align: center;
            padding: 60px;
            margin: 0;
            box-sizing: border-box;
        }

        h1 {
            font-size: 2.5em;
            color: #0066cc;
        }

        p {
            font-size: 1.2em;
            margin-bottom: 30px;
        }

        a {
            display: inline-block;
            background: #007bff;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            margin-top: 20px;
        }

        a:hover {
            background: #0056b3;
        }

        .icon-container {
            margin-top: 50px;
        }

        .icon-container a {
            display: inline-block;
            margin: 0 20px;
            font-size: 1.5em;
            padding: 15px;
            background-color: #007bff;
            border-radius: 50%;
            color: white;
            transition: background-color 0.3s ease;
        }

        .icon-container a:hover {
            background-color: #0056b3;
        }

        .image-container {
            margin-bottom: 40px;
        }

        .header {
            font-size: 1.5em;
            background-color: #0066cc;
            color: white;
            padding: 10px 0;
            margin-bottom: 40px;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #0066cc;
            color: white;
            padding: 20px 0;
            text-align: center;
            z-index: 1000;
        }

        /* Notification Icon Styles */
        .notification-icon {
            font-size: 1.5em;
            position: absolute;
            top: 20px;
            right: 20px; /* Adjust right position as needed */
            color: white;
            transition: color 0.3s ease;
            text-decoration: none;
        }

        .notification-icon:hover {
            color: #ffeb3b; /* Change color on hover */
        }
    </style>
    <!-- Include Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>

    <!-- Header Section -->
    <div class="header">
        🎓 Student Helper
        <!-- Notification Icon in Header -->
        <a href="/notifications/" class="notification-icon" title="View Notifications">
            <i class="fas fa-bell"></i> <!-- Notification Icon -->
        </a>
    </div>

    <!-- Main Content Section -->
    <h1>Welcome!</h1>
    <p>Let’s help you stay organized and on top of your tasks.</p>

    <!-- Image Section -->
    <div class="image-container">
        <img src="/static/images/my-image.jpg" alt="Your Image Description">
    </div>

    <!-- Icon Navigation Section -->
    <div class="icon-container">
        <a href="/create-task/" title="Create Task"><i class="fas fa-plus-circle"></i></a>
        <a href="/help/" title="Help"><i class="fas fa-question-circle"></i></a>
        <a href="/calendar/" title="Calendar"><i class="fas fa-calendar-alt"></i></a>
        
        <!-- Wellness Check-in Icon -->
        <a href="/wellness-checkin/" title="Wellness Check-in" class="wellness-icon">
            <i class="fas fa-heartbeat"></i> <!-- Wellness Icon -->
        </a>
    </div>

</body>
</html>



    """
    return HttpResponse(html_content)


def create_task(request):
    return render(request, 'core/create_task.html')

def help_view(request):
    return render(request, 'core/help.html')

def calendar_view(request):
   
    today = datetime.today()
    
    month = today.month
    year = today.year

    month_calendar = calendar.monthcalendar(year, month)
    
    tasks = Task.objects.filter(due_date__month=month, due_date__year=year)
    
    task_data = {}
    for task in tasks:
        task_data[task.due_date.day] = task.title  

    context = {
        'calendar': month_calendar,
        'task_data': task_data,
        'current_month': today,
        'current_year': year,
    }
    
    return render(request, 'core/calendar.html', context)
def task_view(request):
    task_data = {
        '01/04/2025': {'title': 'Task 1', 'description': 'Description for task 1'},
        '02/04/2025': {'title': 'Task 2', 'description': 'Description for task 2'}
    }
    return render(request, 'task_page.html', {'task_data': task_data})

def wellness_checkin(request):
    if request.method == 'POST':

        mood = request.POST.get('mood')
        energy = request.POST.get('energy')
        comments = request.POST.get('comments')

        messages.success(request, 'Your wellness check-in has been recorded!')

        return redirect('home')  

    return render(request, 'core/wellness_checkin.html')

def notifications(request):
    return render(request, 'core/notification.html')