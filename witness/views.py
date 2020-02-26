from django.shortcuts import render,get_object_or_404

# Create your views here.
from case.models import Case


def witness_home(request):
    """ home view of witness """
    case_list = Case.objects.filter(witness=request.user)

    return render(request, 'witness/witness_home.html', {
        'case_list' : case_list
    })


def witness_case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)

    return render(request, 'witness/witness_case_detail.html', {
        'case' : case
    })