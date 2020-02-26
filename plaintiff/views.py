from django.shortcuts import render,get_object_or_404

# Create your views here.
from case.models import Case

def user_home(request):
    case_list = Case.objects.filter(registered_by=request.user)
    return render(request, "plaintiff/plaintiff_home.html", {
        'case_list' : case_list
    })

def user_case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)

    return render(request, 'plaintiff/plaintiff_case_detail.html', {
        'case' : case
    })