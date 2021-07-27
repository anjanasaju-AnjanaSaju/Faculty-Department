from typing import ItemsView
from django.http import response
from django.shortcuts import render,redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from xlwt.Column import Column
from .models import FacDepartment
import datetime
import xlwt

def home(request):
	
	
	if request.method=="POST":
	
		name=request.POST['name']
		dep_type1=request.POST['name1']
		dep_type2=request.POST['name2']
		print(dep_type2)
		if(dep_type1):
			
			if(dep_type1=="IT"):
				deplist = FacDepartment(IT=name)
				deplist.save()
			elif(dep_type1=="Mechanical"):
				deplist = FacDepartment(Mechanical=name)
				deplist.save()
			elif(dep_type1=="Electrical"):
				deplist = FacDepartment(Electrical=name)
				deplist.save()
			elif(dep_type1=="Teachers"):
				deplist = FacDepartment(Teachers=name)
				deplist.save()
		if(dep_type2):
			if(dep_type2=="IT"):
				deplist = FacDepartment(IT=name)
				deplist.save()
			elif(dep_type2=="Mechanical"):
				deplist = FacDepartment(Mechanical=name)
				deplist.save()
			elif(dep_type2=="Electrical"):
				deplist = FacDepartment(Electrical=name)
				deplist.save()
			elif(dep_type2=="Teachers"):
				deplist = FacDepartment(Teachers=name)
				deplist.save()
		
				

		
	return render(request,'index.html')

