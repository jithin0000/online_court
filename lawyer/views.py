from django.shortcuts import render

# Create your views here.

def lawyer_home(request):
    
    return render(request, 'lawyer/lawyer_home.html', {})
