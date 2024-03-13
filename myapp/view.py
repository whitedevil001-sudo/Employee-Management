from django.http import HttpResponse
from django.shortcuts import render

import datetime
def home(request):

    return render(request,"home.html",{})

def about(request):
    # return HttpResponse("about webpage")
    return render(request,"about.html")