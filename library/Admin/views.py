from django.shortcuts import render,redirect
from librarian.models import regform
from . models import logform
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        obj=logform.objects.filter(email=email,passw=password)
        if obj:
            request.session['em']=email
            request.session['ps']=password
            for ls in obj:
                idno=ls.id
                request.session['idn']=idno
            return render(request,'home.html')
        else:
            request.session['em']=""
            request.session['ps']=""
            return render(request,'log.html')
    else:
        return render(request,'log.html')


def detail(request):
    obj=regform.objects.all()
    return render(request,"details.html",{"data":obj})

#.......................................................................

def edit(request):
    idno=request.GET.get('idn')
    obj=regform.objects.filter(id=idno)
    return render(request,"detail2.html",{"data":obj})

def update(request):
    if request.method=="POST":
        idn=request.POST.get("idl")
        bnm=request.POST.get("bn")
        aut=request.POST.get("au")
        dis=request.POST.get("di")
        price=request.POST.get("pi")
        obj=regform.objects.get(id=idn)
        obj.book=bnm
        obj.author=aut
        obj.disc=dis
        obj.price=price
        obj.save()
        return redirect("/Admin/detail")
def delete(request):
    idno=request.GET.get('idn')
    obj=regform.objects.filter(id=idno) 
    obj.delete()
    return redirect("/Admin/detail")  
        

