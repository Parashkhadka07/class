from django.shortcuts import render
from main.models import Project,Skills
# Create your views here.


projects=Project.objects.all()



def home(request):
    context={"project":projects}
    
    return render(request,"main/index.html",context)



def project(request,id):
    skills=Skills.objects.all()
    context={"project":projects[id-1],"skill":skills}
    return render(request,"main/project.html",context)