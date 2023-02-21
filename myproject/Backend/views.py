from django.shortcuts import render,redirect
from Backend.models import staffdb
from Backend.models import cdb
from Backend.models import pdb
from frontend.models import contact,booking,billing
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def acontactpage(request):
    data = contact.objects.all()
    return render(request,"contact1.html",{'data':data})

def deletecontactdata(request, dataid):
    data = contact.objects.filter(id=dataid)
    data.delete()
    return redirect(acontactpage)

def abookpage(request):
    data = booking.objects.all()
    return render(request,"booking1.html",{'data':data})

def deletebookingdata(request, dataid):
    data = booking.objects.filter(id=dataid)
    data.delete()
    return redirect(abookpage)

def staffpage(request):
    return render(request,'Add_Staff.html')

def savedata(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ph = request.POST.get('mobile')
        un = request.POST.get('uname')
        ps = request.POST.get('pwd')
        cs = request.POST.get('cpwd')
        img =request.FILES['image']
        obj = staffdb(Name=na,Email=em,Mobile=ph,Username=un,Password=ps,Confirm_Password=cs,Image=img)
        obj.save()
        return redirect(staffpage)

def displaystaffpage(request):
    data = staffdb.objects.all()
    return render(request,"Display_Staff.html",{'data':data})

def editstaffpage(request,dataid):
    data = staffdb.objects.get(id=dataid)
    print(data)
    return render(request,"Edit_Staff.html",{'data':data})

def updatestaffdata(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ph = request.POST.get('mobile')
        un = request.POST.get('uname')
        ps = request.POST.get('pwd')
        cs = request.POST.get('cpwd')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = staffdb.objects.get(id=dataid).Image
        staffdb.objects.filter(id=dataid).update(Name=na,Email=em,Mobile=ph,Username=un,Password=ps,Confirm_Password=cs,Image=file)
        return redirect(displaystaffpage)

def deletestaffdata(request, dataid):
    data = staffdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaystaffpage)

def categorypage(request):
    return render(request,'add_category.html')

def savedata2(request):
    if request.method == "POST":
        cn = request.POST.get('category')
        de = request.POST.get('description')
        img = request.FILES['image']
        obj = cdb(Category_Name=cn,Description=de,Image=img)
        obj.save()
        return redirect(categorypage)

def displaycategory(request):
    data = cdb.objects.all()
    return render(request,"display_category.html",{'data':data})

def editcategory(request,dataid):
    data = cdb.objects.get(id=dataid)
    print(data)
    return render(request,"edit_category.html",{'data':data})

def updatecategory(request,dataid):
    if request.method=="POST":
        cn = request.POST.get('category')
        de = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = cdb.objects.get(id=dataid).Image
        cdb.objects.filter(id=dataid).update(Category_Name=cn, Description=de, Image=file)
        return redirect(displaycategory)

def deletecategory(request, dataid):
    data = cdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)

def productpage(request):
    data = cdb.objects.all()
    return render(request, 'Add_pdt.html',{'data':data})


def datasave(request):
    if request.method == "POST":
        ca = request.POST.get('category')
        pn = request.POST.get('pname')
        pc = request.POST.get('price')
        qn = request.POST.get('quantity')
        img = request.FILES['image']
        obj = pdb(Category_Name=ca, Product_Name=pn,Product_Price=pc,Quantity=qn,Image=img)
        obj.save()
        return redirect(productpage)

def displayproduct(request):
    data = pdb.objects.all()
    return render(request,"display_pdt.html",{'data':data})

def editproduct(request,dataid):
    data = pdb.objects.get(id=dataid)
    da = cdb.objects.all()
    print(data)
    return render(request,"edit_pdt.html",{'data':data,'da':da})

def updateproduct(request,dataid):
    if request.method == "POST":
        ca = request.POST.get('category')
        pn = request.POST.get('pname')
        pc = request.POST.get('price')
        qn = request.POST.get('quantity')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = pdb.objects.get(id=dataid).Image
        pdb.objects.filter(id=dataid).update(Category_Name=ca,Product_Name=pn,Product_Price=pc,Quantity=qn,Image=file)
        return redirect(displayproduct)

def deleteproduct(request, dataid):
    data = pdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)


def adminloginpage(request):
    return render(request, "adminlogin.html")

def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('uname')
        password_r = request.POST.get('pwd')
        email_r = request.POST.get('emailid')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,email=email_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['uname']=username_r
                request.session['pwd']=password_r
                request.session['emailid']=email_r
                return redirect(indexpage)
            else:
                return redirect(adminloginpage)
        else:
            return redirect(adminloginpage)

def adminlogout(request):
    del request.session['uname']
    del request.session['pwd']
    del request.session['emailid']
    return redirect(adminloginpage)

def abillingpage(request):
    data = billing.objects.all()
    return render(request,"billing.html",{'data':data})


def deletebillingdata(request, dataid):
    data = billing.objects.filter(id=dataid)
    data.delete()
    return redirect(abillingpage)