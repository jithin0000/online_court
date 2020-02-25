from django.shortcuts import render

# Create your views here.

def witness_home(request):
    """ home view of witness """

    return render(request, 'witness/witness_home.html', { })
