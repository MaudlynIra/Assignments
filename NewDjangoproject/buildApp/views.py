from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Maudlyn has created a new Django project named NewProject and create an app in the project called “buildApp”. Your project must contain a requirements.txt file housing all the pinned dependencies from your project. Push the project to GitHub and submit your public GitHub repository link. Note: Always create a virtual environment anytime you're working on a new Django project. You can get your requirements.txt file from your virtual environment Mode of submission - Public GitHub repository link")