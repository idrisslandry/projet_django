from django.shortcuts import render,get_object_or_404
from computerApp.models import Machine, Personnel

def index(request) :
    
    context = { }
    return render(request, 'index.html', context)
    # Create your views here.
def machine_list_view(request) :
    machines =  Machine.objects.all()
    context = {'machines':machines}
    return render(request,
        'computerApp/machine_list.html',
        context)
def personnel_list_view(request) :
    personnels =  Personnel.objects.all()
    context = {'personnels':personnels}
    return render(request,
        'computerApp/personnel_list.html',
        context)

def machine_detail_view(request,pk):
    machine = get_object_or_404(Machine,id=pk)
    context ={'machine': machine}
    return render(request,'computerApp/machine_detail.html',context)