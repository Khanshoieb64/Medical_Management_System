from django.shortcuts import redirect, render
from django.views import View

from .forms import AddMedicineForm,RegisterForm,LoginForm
from .models import AddMedicine,Register,LoginModel
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from django.contrib import messages



# Create your views here.

class AddMedicineDetail(View):
    def get(self,request):
        form=AddMedicineForm()
        d={'form':form}
        return render(request,'addmedicine.html',d)
    def post(self,request):
        form=AddMedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addmd')
            # d={'form':form}
            # return render(request,'addmedicine.html',d)
        

def home(request):
    if request.method=='POST':
        mdname=request.POST['name']
        query=Q(name__icontains=mdname) | Q(company__icontains=mdname) | Q(rate__icontains=mdname) | Q(mrp__icontains=mdname) | Q(quantity__icontains=mdname)  | Q(type__icontains=mdname) | Q(purchase_date__icontains=mdname) | Q(expiry_date__icontains=mdname) 
        detail=AddMedicine.objects.filter(query)
        d={'detail':detail}
        return render(request,'index.html',d)
    detail=AddMedicine.objects.all()
    d={'detail':detail}
    return render(request,'index.html',d)
    

def updatepage(request):
    if request.method=='POST':
        mdname=request.POST['name']
        query=Q(name__icontains=mdname) | Q(company__icontains=mdname) | Q(rate__icontains=mdname) | Q(mrp__icontains=mdname) | Q(quantity__icontains=mdname) | Q(type__icontains=mdname) | Q(purchase_date__icontains=mdname) | Q(expiry_date__icontains=mdname) 
        detail=AddMedicine.objects.filter(query)
        d={'detail':detail}
        return render(request,'updatepage.html',d)
    detail=AddMedicine.objects.all()
    d={'detail':detail}
    return render(request,'updatepage.html',d)

# delete.html page
def deletepage(request):
    if request.method=='POST':
        mdname=request.POST['name']
        query=Q(name__icontains=mdname) | Q(company__icontains=mdname) | Q(rate__icontains=mdname) 
        detail=AddMedicine.objects.filter(query)
        d={'detail':detail}
        return render(request,'deletepage.html',d)
    detail=AddMedicine.objects.all()
    d={'detail':detail}
    return render(request,'deletepage.html',d)

def deletemd(request,mid):
    obj=AddMedicine.objects.get(id=mid)
    obj.delete()
    return redirect('updatepage')

# delete.html 
def deletemd2(request,mid):
    obj=AddMedicine.objects.get(id=mid)
    obj.delete()
    return redirect('deletepage')

def updatemd(request,pk):
    obj=AddMedicine.objects.get(id=pk)
    form=AddMedicineForm(instance=obj)
    if request.method=='POST':
        form=AddMedicineForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('updatepage')
    d={'form':form}
    return render(request,'addmedicine.html',d)





# view code for  signup 

class Signup(View):
    def get(self,request):
        form=RegisterForm()
        d={'form':form}
        return render(request,'signup.html',d)

    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            messages.success(request, 'Detail submitted successfully.')

        user=User.objects.create_user(username=username,password=password,email=email)
        user.first_name=name
        form.save()
        return redirect('/')
        

# Login 
class Login(View):
    def get(self,request):
        form=LoginForm()
        d={'form':form}
        return render(request,'login.html',d)   
    
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return redirect('/')
        # d={'form':form}
        # return render(request,'index.html',d) 


# logout
def logout(request):
    auth_logout(request)
    return redirect('/')