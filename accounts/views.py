from django.shortcuts import render, HttpResponse

# Create your views here.
def home (request):
    return render(request, 'login.html')

def wet(request):
    return render(request, 'pussy.html')    