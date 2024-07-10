from django.shortcuts import render, redirect
from datetime import datetime
import random
from .models import FormSubmission

def index(request):
    current_datetime = datetime.now()
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Do not watch the clock. Do what it does. Keep going.",
        "Keep your face always toward the sunshine—and shadows will fall behind you."
    ]
    random_quote = random.choice(quotes)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        FormSubmission.objects.create(name=name, email=email)
        return redirect('submissions')

    context = {
        'current_datetime': current_datetime,
        'random_quote': random_quote
    }
    return render(request, 'webpage/index.html', context)

def submissions(request):
    submissions = FormSubmission.objects.all()
    return render(request, 'webpage/submissions.html', {'submissions': submissions})
