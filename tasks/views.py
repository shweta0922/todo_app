from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
current_task= ['Creating a django project',
              'Learn the various template',
              'Learn how to deploy projects']

def index(request):
    return render(request,'index.html',context={
        'cur_date': str(datetime.now()),
        'tasks': current_task,
    })
