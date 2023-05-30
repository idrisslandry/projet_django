from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from computerApp.forms import Add_commu_form, Add_routeur_form
from computerApp.models import Commu, Routeur


def index(request):	
	context = {}
	return render(request, 'index.html', context)


def commu_list_view (request):
		commu = Commu.objects.all()
		context = {'commus': commu}
		return render (request,'computerapp/commu_list.html', context)
			

def routeur_list_view (request):
	routeur = Routeur.objects.all()
	context = {'routeurs': routeur}
	return render (request,'computerapp/routeur_list.html', context)


def commu_detail (request, slug):
	commu = get_object_or_404(Commu, slug=slug)
	return render(request, 'computerapp/commu_detail.html', context={"commu": commu})


def routeur_detail (request, slug):
	routeur = get_object_or_404(Routeur, slug=slug)
	return render(request, 'computerapp/routeur_detail.html', context={"routeur": routeur})


def add_commu (request):
	if request.method == "POST":
		form = Add_commu_form(request.POST).save()
		return redirect('/computerApp/commus')
	else:
		form = Add_commu_form() #instansiation
		return render(request, 'computerapp/add_commu.html', context={"form": form})



def add_routeur (request):
	if request.method == "POST":
		form = Add_routeur_form(request.POST).save()
		return redirect('/computerApp/routeurs')
	else:
		form = Add_routeur_form() #instansiation
		return render(request, 'computerapp/add_routeur.html', context={"form": form})


def delete_commu (request, pk):
	commu = get_object_or_404(Commu, id=pk)
	if request.method == "POST":
		commu.delete()
		return redirect('commu')
	context = {'commu':commu}
	return render(request, 'computerapp/delete_commu.html', context)


def delete_routeur (request, pk):
	routeur = get_object_or_404(Routeur, id=pk)
	if request.method == "POST":
		routeur.delete()
		return redirect('routeur')
	context = {'routeur':routeur}
	return render(request, 'computerapp/delete_routeur.html', context)


