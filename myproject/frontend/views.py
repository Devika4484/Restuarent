from django.shortcuts import render,redirect



# Create your views here.

from Backend.models import cdb
from Backend.models import pdb
from frontend.models import login,contact,booking,billing
from django.contrib import messages



def webpage(request):
    data = cdb.objects.all()
    return render(request,"home.html",{'data':data})


def aboutpage(request):
    return render(request,"about.html")

def cart(request,dataid):
    datas = pdb.objects.get(id=dataid)
    data = cdb.objects.all
    return render(request,"cart.html",{'dat':datas,'data':data})

def cbillingpage(request):
    return render(request, "cbilling.html")


def savebiling(request):
    if request.method == "POST":
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        un = request.POST.get('uname')
        em = request.POST.get('email')
        ad = request.POST.get('address')
        obj = billing(Fname=fn,Lname=ln,Uname=un,Email=em,Address=ad)
        obj.save()
        return redirect(webpage)


# def pdtdetails(request,dataid):
#     datas = pdb.objects.get(id=dataid)
#     data = cdb.objects.all
#     return render(request,"productdetails.html",{'dat':datas,'data':data})


def discategory(request, itemcatg):
    data=cdb.objects.all()
    print('===itemcatg===',itemcatg)
    catg=itemcatg.upper()
    products=pdb.objects.filter(Category_Name=itemcatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request, "categorydisplay.html", context)


def signpage(request):
    return render(request, "login.html")

def savelogin(request):
    if request.method == "POST":
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        un = request.POST.get('uname')
        em = request.POST.get('email')
        ps = request.POST.get('pwd')
        cs = request.POST.get('cpwd')
        if ps==cs:
            obj = login(Name=fn,Lname=ln,Uname=un,Email=em,Password=ps,Cpassword=cs)
            obj.save()
            return redirect(signpage)
        else:
            return render(request,'login.html',{'msg':"Password Not Matched"})


def customerlogin(request):
    if request.method == 'POST':
        username_r = request.POST.get("uname")
        password_r = request.POST.get("pwd")
        if login.objects.filter(Uname=username_r,Password=password_r).exists():
            data = login.objects.filter(Uname=username_r,Password=password_r).values('id').first()
            request.session['uname'] = username_r
            request.session['pwd'] = password_r
            # request.session['email'] =data['email']
            request.session['userid']=data['id']

            return redirect(cbillingpage)
        else:
            return render(request,'login.html',{'msg':"Invalid Username or password"})

def customerlogout(request):
    del request.session['uname']
    del request.session['pwd']
    # del request.session['email']
    return redirect(webpage)

def contactpage(request):
    return render(request,"contact.html")


def savedata5(request):
    if request.method == "POST":
        con = request.POST.get('name')
        e = request.POST.get('email')
        s = request.POST.get('subject')
        ms = request.POST.get('message')
        obj = contact(Name=con,Email=e,Subject=s,Message=ms)
        obj.save()
        return redirect(webpage)

def bookpage(request):
    return render(request,"book.html")


def savedata6(request):
    if request.method == "POST":
        bon = request.POST.get('name')
        bph = request.POST.get('phone')
        bem = request.POST.get('email')
        np = request.POST.get('person')
        bd = request.POST.get('book')
        obj = booking(Name=bon,Phone=bph, Email=bem,NPersons=np,Date=bd)
        obj.save()
        return redirect(webpage)

