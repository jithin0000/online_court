from django.shortcuts import render, get_object_or_404

# Create your views here.

from customuser.models import MyUser
from case.models import Case

def lawyer_home(request):

    case_list = Case.objects.filter(first_lawyer = request.user)
    
    return render(request, 'lawyer/lawyer_home.html', {
        "case_list" : case_list
        })


def register_laywer(request):

    return render(request, 'lawyer/lawyer_register.html',{})


def case_deatils(request, pk):
    """ lawyer case details view """
    case = get_object_or_404(Case, pk = pk)

    return render(request, 'lawyer/lawyer_case_detail.html', { 'case' : case  })
