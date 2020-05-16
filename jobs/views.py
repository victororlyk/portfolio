from django.shortcuts import render
from .models import Job


# Create your views here.

def home(req):
    jobs = Job.objects
    options = {
        'jobs': jobs
    }
    return render(req, 'jobs/home.html', options)
