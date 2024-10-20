from django.shortcuts import render

# Create your views here.
def home(request):
    #request is used to navigate the command to our html page
    # for navigation we need to use a keyword called as render

    return render(request,'home1.html')

def Login(request):
    return render(request, 'login.html')

def Register(request):
    return render(request, 'register.html')
