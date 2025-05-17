from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from Technician.models import Servicebill
# Create your views here.

def homepagetechnician(request):
 if 'tid' in request.session:
    techn=Technician.objects.get(id=request.session["tid"])
    return render(request,"Technician/Technicianhomepage.html",{'data':techn})
 else:
        return redirect('guest:Home')

def TechnicianMyProfile(request):
 if 'tid' in request.session:
    techn=Technician.objects.get(id=request.session["tid"])
    return render(request,"Technician/TechnicianMyProfile.html",{'data':techn})
 else:
        return redirect('guest:Home')

def TechnicianEditProfile(request):
     if 'tid' in request.session:
        techn=Technician.objects.get(id=request.session["tid"])
        if request.method=="POST":
            techn.technician_name=request.POST.get('txt_name')
            techn.technician_contact=request.POST.get('txt_contact')
            techn.technician_address=request.POST.get('txt_address')
            techn.save()
            return redirect("technician:technicianprofile")
        else:
            return render(request,"Technician/TechnicianEditProfile.html",{'data':techn})
     else:
        return redirect('guest:Home')
    
def TechnicianChangePass(request):
     if 'tid' in request.session:
        if request.method=="POST":
            techcount=Technician.objects.filter(id=request.session["tid"],technician_password=request.POST.get('txt_curr')).count()
            if techcount>0:
                techn=Technician.objects.get(id=request.session["tid"],technician_password=request.POST.get('txt_curr'))
                techn.technician_password=request.POST.get('txt_new')
                techn.save()
                return redirect("technician:technicianhome")
        else:
            return render(request,"Technician/TechnicianChangePassword.html")   
     else:
        return redirect('guest:Home')

def TechnicianAssignedService(request):
    if 'tid' in request.session:
        serv=Assignservicebook.objects.filter(technician=request.session["tid"])
        return render(request,"Technician/ViewAllocatedServices.html",{'res':serv})   
    else:
        return redirect('guest:Home')     

def ConfirmServ(request,cid):
    if 'tid' in request.session:
        serv=Assignservicebook.objects.get(id=cid)  
        serv.asb_status=2
        serv.save()
        return redirect('technician:Myassignedservice') 
    else:
        return redirect('guest:Home')     

def DeleteServ(request,cid):
    if 'tid' in request.session:
        serv=Assignservicebook.objects.get(id=cid) 
        bokid=serv.servicebooking_id
        sbok=Servicebook.objects.get(id=bokid)
        sbok.Servicebook_status=1
        sbok.save()

        serv.delete()
        return redirect('technician:Myassignedservice') 
    else:
        return redirect('guest:Home')   

def ConfirmedServices(request):
    if 'tid' in request.session:
        serv=Assignservicebook.objects.filter(technician=request.session["tid"])
        return render(request,"Technician/ViewConfirmedServices.html",{'res':serv})  
    else:
        return redirect('guest:Home')   
    

def ServiceBill(request,bid):
     if 'tid' in request.session:
        serv=Assignservicebook.objects.get(id=bid)
        if request.method=="POST":
            Servicebill.objects.create(servicebill_amount=request.POST.get('txt_amount'),servicebill_noofdays=request.POST.get('txt_days'),servicebill_partamount=request.POST.get('txt_parts'),servicebill_additionaldetails=request.POST.get('txt_replaced'),servicebill_details=request.POST.get('txt_issue'),assignedservicebooking=serv)
            serv.asb_status=3
            serv.save()
            bokid=serv.servicebooking_id
            sbok=Servicebook.objects.get(id=bokid)
            sbok.Servicebook_status=4
            sbok.save()
            return redirect('technician:viewconfimedservice')
        else:

         return render(request,"Technician/GenerateBill.html",{'data':serv})
     else:
        return redirect('guest:Home')   
     
def logout(request):
    
    del request.session['tid']
    return redirect('guest:Home')


       
  