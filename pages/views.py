from django.shortcuts import render
from .models import Post
import datetime
from django.core.mail import send_mail
# Create your views here.
from django.http import HttpResponse
def index(request):
	#return HttpResponse("<h1>The MeanDoc Homepage</h1>")
	return render(request,'pages/page.html')

#def index(request,pagename):
def heading(request):
	return render(request,'pages/contact.html')

