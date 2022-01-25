from django.shortcuts import render,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.core.paginator import Paginator

# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$100000$5rt6sWwFiXnU$dW12/xmcfNoTyrqCc1rURZE4MOCmLu7OSD6IdF+JYxA='))

# Create your views here.
## add data and show all data ##
def Registerpage(request):
    if request.method == 'POST':
        fm = StudentRegistrations(request.POST)
        if fm.is_valid():
            nme=fm.cleaned_data['Name']
            em=fm.cleaned_data['Email']
            pswd=fm.cleaned_data['Password']
            data=Register(Name=nme,Email=em,Password=pswd)
            data.Password = make_password(data.Password)
            data.save()
            
            messages.add_message(request,messages.SUCCESS, 'Your Account has been Created!!!') ##or
            # messages.success(request, "Your Account has been created!!!")
            messages.info(request, "Now You can login!!!")

            #//debug message  //##
            # print(messages.get_level(request))  ## unset debugg
            # messages.debug(request, 'This is Debug')
            # messages.set_level(request, messages.DEBUG)  ## set debugg
            # messages.debug(request, 'This is New Debug')
            # print(messages.get_level(request))
            fm = StudentRegistrations()
    else:
       fm = StudentRegistrations()
    stud = Register.objects.all().order_by('id')
    paginator = Paginator(stud, 3)#(stud, 3,orphans=1)//orphanse=-->used last page is 1 item then privious page added not only show one data
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"app/registershow.html",{'form':fm,'page_obj':page_obj})
## Update and edit data ##
def Update(request,id):
    if request.method == 'POST':
        pi =Register.objects.get(pk=id)
        fm = StudentRegistrations(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
           
    else:
        pi = Register.objects.get(pk=id)
        fm = StudentRegistrations(instance=pi)
    return render(request,"app/update.html",{'form':fm})

## delete data ##
def Deletedata(request,id):
    if request.method == 'POST':
        deletedatastu= Register.objects.get(pk=id)
        deletedatastu.delete()
        return HttpResponseRedirect('/')

def Search(request):
    return HttpResponse("this is search")



    




