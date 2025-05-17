from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.

def Reg(request):
    dis=District.objects.all()
    pl=Place.objects.all()
    if request.method=="POST":
        re=User.objects.filter(user_email__icontains=request.POST.get("txt_email"))
        if re:
            return render(request,"Guest/Registration.html",{'dis':dis,'pl':pl,'msg':"Email id already in use"})
        else:
            p=Place.objects.get(id=request.POST.get('ddl_place'))
            User.objects.create(user_name=request.POST.get('txt_name'),user_gender=request.POST.get('rad_gender'),user_contact=request.POST.get('txt_num'),user_email=request.POST.get('txt_email'),user_photo=request.FILES.get('file_photo'),user_proof=request.FILES.get('file_proof'),user_password=request.POST.get('txt_pass'),user_address=request.POST.get('txt_address'),place=p)
            return render(request,"Guest/Registration.html",{'dis':dis,'pl':pl,'msg':"Registered"})

    else:
        return render(request,"Guest/Registration.html",{'dis':dis,'pl':pl})

def Ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('disd'))
    pl=Place.objects.filter(district=dis)
    return render(request,"Guest/Ajaxplace.html",{'pl':pl})

def login(request):
    if request.method=="POST":
        usercount=User.objects.filter(user_email=request.POST.get('txt_ename'),user_password=request.POST.get('txt_pass')).count()
        techniciancount=Technician.objects.filter(technician_email=request.POST.get('txt_ename'),technician_password=request.POST.get('txt_pass')).count()
        admincount=Admin.objects.filter(admin_email=request.POST.get('txt_ename'),admin_password=request.POST.get('txt_pass')).count()
        collectorcount=EwasteCollector.objects.filter(EwasteCollector_email=request.POST.get('txt_ename'),EwasteCollector_password=request.POST.get('txt_pass')).count()
        if usercount>0:
            user=User.objects.get(user_email=request.POST.get('txt_ename'),user_password=request.POST.get('txt_pass'))
            request.session["uid"]=user.id
            request.session["uname"]=user.user_name
            return redirect("webuser:userhome")
        if techniciancount>0:
            technician=Technician.objects.get(technician_email=request.POST.get('txt_ename'),technician_password=request.POST.get('txt_pass'))
            request.session["tid"]=technician.id
            request.session["tname"]=technician.technician_name
            return redirect("technician:technicianhome")     
        if admincount>0:
            admin=Admin.objects.get(admin_email=request.POST.get('txt_ename'),admin_password=request.POST.get('txt_pass'))
            request.session["aid"]=admin.id
            request.session["aname"]=admin.admin_name
            return redirect("webadmin:adminhome")
        if collectorcount>0:
            ecol=EwasteCollector.objects.get(EwasteCollector_email=request.POST.get('txt_ename'),EwasteCollector_password=request.POST.get('txt_pass'))
            request.session["eid"]=ecol.id
            request.session["ename"]=ecol.EwasteCollector_name
            return redirect("webcollector:ewastecolhome")

    return render(request,"Guest/Login.html")
        

def ForgotPass(request):
    if request.method=="POST":
        otp=(random.randint(100000,999999))
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txt_email')
        send_mail(
            'Respected Sir/Madam '+" ",#subject
            "Your Otp is "+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txt_email')],
        )
        return redirect('guest:validateotp')
    else:
        return render(request,"Guest/ForgotPassword.html")
    
def ValidateOtp(request):
    if request.method=="POST":
        otp=request.POST.get("txt_otp")
        ce=str(request.session["otp"])
        if otp==ce:
            return redirect("guest:createpass")
    return render(request,"Guest/ValidateOTP.html")

def CreatePass(request):
    if request.method=="POST":
        if request.POST.get("txt_pass")==request.POST.get("txt_confirm"):
            usercount=User.objects.filter(user_email=request.session["femail"]).count()
            techniciancount=Technician.objects.filter(technician_email=request.session["femail"]).count()
            ecollectorcount=EwasteCollector.objects.filter(EwasteCollector_email=request.session["femail"]).count()
            if usercount>0:
                user=User.objects.get(user_email=request.session["femail"])
                user.user_password=request.POST.get("txt_pass")
                user.save()
                return render(request,"Guest/CreatePassword.html",{'msgu':"User Password Changed Successfully"})
            elif techniciancount>0:
                  technician=Technician.objects.get(technician_email=request.session["femail"])
                  technician.technician_password=request.POST.get("txt_pass")
                  technician.save()
                  return render(request,"Guest/CreatePassword.html",{'msgt':"Technician Password Changed Successfully"})
            elif ecollectorcount>0:
                  ecollector=EwasteCollector.objects.get(EwasteCollector_email=request.session["femail"])
                  ecollector.EwasteCollector_password=request.POST.get("txt_pass")
                  ecollector.save()
                  return render(request,"Guest/CreatePassword.html",{'msgec':"Ewaste Collector Password Changed Successfully"})         
        else:
            return render(request,"Guest/CreatePassword.html",{'msg':" Passwords are not same"})
    else:
        return render(request,"Guest/CreatePassword.html")



def home(request):
    return render(request,"Guest/Home.html")