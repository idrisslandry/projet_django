
from django.urls import path
from computerApp import views
from computermngt import settings
from django.conf.urls.static import static
from accounts.views import signup, login_user, logout_user, compte_user, users_list_view

urlpatterns = [
	path ('', views.index, name ='index'),
	path ('signup/', signup, name ='signup'),
	path ('users_list/', users_list_view, name ='users_list'),
	path ('login/', login_user, name ='login'),
	path ('logout/', logout_user, name ='logout'),
	path ('compte/', compte_user, name ='compte'),
	path ('commus/', views.commu_list_view, name ='commus'),
	path ('routeurs/', views.routeur_list_view, name ='routeurs'),
	path ('commus/<str:slug>', views.commu_detail, name ='commu_detail'),
	path ('routeurs/<str:slug>', views.routeur_detail, name ='routeur_detail'),
	path ('add_commu/', views.add_commu, name='add_commu'),
	path ('add_routeur/', views.add_routeur, name='add_routeur'),
	
]