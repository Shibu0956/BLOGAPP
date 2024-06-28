from django.shortcuts import render,redirect
from Blogapp.models import Myblog
from Blogapp.form import Blogform



# Create your views here.

def demo(request):
    Blogs2 = Myblog.objects.all()
    return render(request,'demo.html',{'Blogs2':Blogs2})

def home(request):
    print("entered")
    if request.method == "POST":
        form = Blogform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except:
                pass
            print("form submitd")
    else:
             form = Blogform()
    return render(request,'index.html')  

def show(request):
    Blogs = Myblog.objects.all()
    return render(request,'show.html',{'Blogs':Blogs})  

def edit(request, id):
    Blogs1 = Myblog.objects.get(id=id)
    return render(request,'edit.html', {'Blogs1': Blogs1})

def update(request,id):
    Blogs1 = Myblog.objects.get(id=id)
    form = Blogform(request.POST, instance = Blogs1)
    print("entred")
    if form.is_valid(): 
       form.save() 
       return redirect("/show")
    print("form sumbtd")
    return render(request, 'edit.html', {'Blogs1': Blogs1})

def destroy(request,id):
   Blogs1 = Myblog.objects.get(id=id)
   Blogs1.delete()
   return redirect("/show")   
 
       
