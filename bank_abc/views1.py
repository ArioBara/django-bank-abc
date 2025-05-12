from django.shortcuts import render, redirect
from .forms import Transferform, Nasabahform
from .models import Nasabah, Cabangbank, Rekening, Transaksi

# Create your views here.
def index(request):
    return render(request, 'signin.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Nasabah.nasabah.get(username=username, password=password)
            if user is not None:
                return render(request, 'dash.html')
            else:
                msg = 'username/password anda salah'
                return redirect('/', msg=msg)
        except Exception as identifier:
            return redirect('/')
    else:
        return redirect(request, 'signin.html')

def dash(request):
    rekening = Rekening.objects.all()
    return render(request, 'dash.html', {'rekening': rekening})

def pembelian(request):
    return render(request, 'pembelian.html')

def transfer(request):
    return render(request, 'transfer.html')
    

def simpandata(request):
    if request.method == "POST":
        form = Transferform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('dash') #Lihat Pada urls.py saat ingin men-redirect setelah aksi save.
            except:
                pass
    else:
        form = Transferform()
    return render(request,'transfer.html', {'form':form})

def transaksi(request):
    transaksi = Transaksi.transaksi.all()
    return render(request, 'transaksi.html', {'transaksi': transaksi})

def akun(request):
    akun = Nasabah.objects.all()
    return render(request, 'akun.html', {'nasabah': akun})

def editakun(request, id):
    edit = Nasabah.objects.get(id=id)
    return render(request, 'update_akun.html', {'edit': edit})

def struk(request):
    return render(request, 'struk.html')

def updateakun(request, id):
    update_data = Nasabah.objects.get(id=id)
    formupdatedata = Nasabahform(request.POST, instance=update_data)
    if formupdatedata.is_valid():
        formupdatedata.save()
        return redirect('/')
    return render(request,'update_akun.html',{'update_data': update_data})