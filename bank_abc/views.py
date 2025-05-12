from django.shortcuts import render, redirect
from .forms import Transferform, Nasabahform
from .models import Nasabah, Cabangbank, Rekening, Transaksi

def tampildata(request):        
    return render(request,"index.html",{'tampilkandata':Nasabah.objects.all()})

def inputdata(request):
    return render(request, "inputdata.html")

def simpandata(request):
    if request.method == "POST":
        form = Nasabahform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/') #Lihat Pada urls.py saat ingin men-redirect setelah aksi save.
            except:
                pass
    else:
        form = Nasabahform()
    return render(request,'inputdata.html',{'form':form})

def hapusdata(request, id):
    Nasabah.objects.get(id=id).delete()
    return redirect('/')

def editdata(request, id):
    return render(request, "editdata.html", {'editdatanya':Nasabah.objects.get(id=id)})

def updatedata(request, id):
    formupdatedata = Nasabahform(request.POST, instance=Nasabah.objects.get(id=id))
    if formupdatedata.is_valid():
        formupdatedata.save()
        return redirect('/')
    return render(request,'editdata.html',{'updatedatanya':Nasabah.objects.get(id=id)})