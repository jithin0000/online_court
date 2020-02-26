from django.shortcuts import render,get_object_or_404
from django.db.models import Q
# Create your views here.
from case.models import Case

def user_home(request):
    case_list = Case.objects.filter(
        Q(registered_by=request.user) | Q(defendent=request.user)
    )
    return render(request, "plaintiff/plaintiff_home.html", {
        'case_list' : case_list
    })

def user_case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)

    return render(request, 'plaintiff/plaintiff_case_detail.html', {
        'case' : case
    })