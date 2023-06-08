from django.shortcuts import render
from .models import Question, Developer, Choice

def index(request):
    developers = Developer.objects.all()
    
    context = {
        'developers' : developers,
    }
    
    return render(request, 'index.html', context=context)

def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions' : questions,
    }
    
    return render(request, 'form.html', context=context)
    
