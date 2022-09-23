from django.shortcuts import render
from . models import regform

# Create your views here.
# def reg(request):
#     return render(request,'libreg.html')
def reg(request):
    if request.method=="POST":
        book=request.POST.get('book')
        author=request.POST.get('author')
        disc=request.POST.get('disc')
        price=request.POST.get('price')
        obj=regform.objects.create(book=book,author=author,disc=disc,price=price)
        
        if obj:
            obj.save()
            return render(request,"libreg.html",{'msg':'success'})
        else:
            return render(request,"libreg.html",{'msg':'not '})
    else:
        return render(request,"libreg.html",{'msg':''})