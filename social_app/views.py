from django.shortcuts import render,redirect
from .models import Avaliable,Busy
from dateutil.parser import parse
import datetime
# Create your views here.
def login(request):
    return render(request,'social_app/login.html')

def manage(request):
    return render(request, 'index.html')

def dashboard(request):
    return  render(request,'dashboard.html')
def getsdata(request):
    date = request.POST['dates']
    #dt=parse(date)
    #date=dt.strftime('%B %d, %Y')
    avaliable=Avaliable.objects.all()
    busy=Busy.objects.all()
    print(avaliable)
    print(busy)

    context = {'avaliable': avaliable, 'busy': busy,'date':date}
    return render(request,'getsdata.html',context)

def getinfo(request):

    return render(request,'getinfo.html')

def getcollect(request):
    name = request.POST.get('name')
    date = request.POST.get('date')
    From = request.POST.get('from')
    To = request.POST.get('to')
    print(name, date, From, To)
    f=0
    en=Busy(name=name,date=date,From=From,To=To,ids=str(date))
    try:
        check1=Busy.objects.filter(date=date,ids=str(date))
        check=check1.values()
    except Busy.DoesNotExist:
        check=None
    if check==None:
        en.save()
    else:
        for i in check:
            print(i)
            print(datetime.time(int(From[0:2]),int(From[3:5])))
            if i['From']<datetime.time(int(From[0:2]),int(From[3:5])) and i['To']>datetime.time(int(To[0:2]),int(To[3:5])):
                f=1
                break
        if f==1:
            return redirect('dashboard')
        else:
            en.save()


    return redirect('dashboard')
