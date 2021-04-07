from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from Component.models import Notes
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
def Home(request):
    return HttpResponse("<h1>hello world</h1>");


def Create(request):
    if(request.method=="POST"):
        n=Notes()
        n.title=request.POST['title']
        n.description=request.POST['description']
        n.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  
    else:   
        dic={'Objects':Notes.objects.all()}
        return render(request,"Create.html",dic);


def Delete(request,id):
        if(request.method=="POST"):
            obj=get_object_or_404(Notes,id=id)  # another method is Notes.objects.get(id=id) but it will give ObjectDoesNotExist exception
            obj.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # remember this to redirect to same page!! 0
        else:
            return HttpResponse("<h1>hello world</h1>")
    

def Update(request,id):
    if(request.method=="POST"):
        obj=get_object_or_404(Notes,id=id)
        dic={'obj':obj}
    return render(request,"Delete.html",dic)
def UpdatePro(request,id,id2):    
    if(request.method=="GET"):
          obj=get_object_or_404(Notes,id=id2)
          obj.title=request.GET['title']
          obj.description=request.GET['description']
          obj.save()
    return redirect("http://127.0.0.1:8000/")
   # return HttpResponse("<h1>Object is saved</h1>")

