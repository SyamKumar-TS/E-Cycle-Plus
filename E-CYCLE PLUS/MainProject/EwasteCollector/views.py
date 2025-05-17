from django.shortcuts import render,redirect
from Admin.models import *
from User.models import Ewastebooking
from EwasteCollector.models import *
from django.shortcuts import render, redirect
from Admin.models import Yard
from EwasteCollector.models import  CollectedEwaste
from User.models import Ewastebooking
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.utils import timezone

# Create your views here.

def EWHome(request):
  if 'eid' in request.session:
    ecol=EwasteCollector.objects.get(id=request.session["eid"])
    return render(request,"EwasteCollector/CollectorHomePage.html",{'data':ecol})   
  else:
        return redirect('guest:Home')  

def ECprofile(request):
  if 'eid' in request.session:
    ecol=EwasteCollector.objects.get(id=request.session["eid"])
    return render(request,"EwasteCollector/EcollectorMyProfile.html",{'data':ecol}) 
  else:
        return redirect('guest:Home') 
 
def CollectorChangePass(request):
    if 'eid' in request.session:
        if request.method=="POST":
            ecolcount=EwasteCollector.objects.filter(id=request.session["eid"],EwasteCollector_password=request.POST.get('txt_curr')).count()
            if ecolcount>0:
                ecol=EwasteCollector.objects.get(id=request.session["eid"],EwasteCollector_password=request.POST.get('txt_curr'))
                ecol.EwasteCollector_password=request.POST.get('txt_new')
                ecol.save()
                return redirect("webcollector:ewastecolhome")
        else:
            return render(request,"EwasteCollector/EcollectorChangePassword.html") 
    else:
        return redirect('guest:Home')     

def ViewAllocatedEC(request):
 if 'eid' in request.session:
    ecol=Assignewastebooking.objects.filter(collector=request.session["eid"])
    return render(request,"EwasteCollector/AllocatedEwasteCollectionRequests.html",{'data':ecol})   
 else:
        return redirect('guest:Home')         

def ConfirmEbook(request,cid):
      if 'eid' in request.session:
        wbook=Assignewastebooking.objects.get(id=cid)  
        wbook.aeb_status=2
        wbook.save()
        return redirect('webcollector:ViewmyAllocEC') 
      else:
        return redirect('guest:Home')

def DeleteEbook(request,cid):
      if 'eid' in request.session:
        eb=Assignewastebooking.objects.get(id=cid) 
        bokid=eb.ewastebooking_id
        sbok=Ewastebooking.objects.get(id=bokid)
        sbok.ewastebooking_status=0
        sbok.save()

        eb.delete()
        return redirect('webcollector:ViewmyAllocEC') 
      else:
        return redirect('guest:Home')

def ConfirmedEWCollection(request):
     if 'eid' in request.session:
        eb=Assignewastebooking.objects.filter(collector=request.session["eid"])
        return render(request,"EwasteCollector/ConfirmedEwasteCollectionReq.html",{'res':eb}) 
     else:
        return redirect('guest:Home')
from django.shortcuts import render, redirect
from Admin.models import *  # Import Yard from the admin app
from EwasteCollector.models import  CollectedEwaste
from User.models import Ewastebooking
def generate_pdf_bill(request, collected_ewaste):
    # Prepare data for PDF
    context = {
        'collected_ewaste': collected_ewaste,
        'date': timezone.now().strftime("%d/%m/%Y"),
        'invoice_number': f"INV-{collected_ewaste.id}",
        'ewaste_booking': collected_ewaste.Ewaste.ewastebooking,
        'user': collected_ewaste.Ewaste.ewastebooking.user,
        'yard': collected_ewaste.yard,
    }
    
    # Render template to string
    template = get_template('EwasteCollector/bill_template.html')
    html = template.render(context)
    
    # Create PDF
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        # Generate response with PDF
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        filename = f"ewaste_bill_{collected_ewaste.id}.pdf"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    
    # If error occurred during PDF generation
    return HttpResponse("Error generating PDF", status=400)
def Yardselect(request, cid):
    if 'eid' in request.session:
        yar = Yard.objects.all()
        eb = Assignewastebooking.objects.get(id=cid)
        
        if request.method == "POST":
            yardd = Yard.objects.get(id=request.POST.get('ddl_yard'))
            
            # Get the form data
            total_weight = request.POST.get('txt_weight')
            recyclable_weight = request.POST.get('txt_recyclable_weight')
            nonrecyclable_weight = request.POST.get('txt_nonrecyclable_weight')
            rate_per_kg = request.POST.get('txt_rate')
            total_amount = float(total_weight) * float(rate_per_kg)
            
            # Create CollectedEwaste record with new fields
            collected_ewaste = CollectedEwaste.objects.create(
                collectedewaste_weight=total_weight,
                recyclable_weight=recyclable_weight,
                nonrecyclable_weight=nonrecyclable_weight,
                rate_per_kg=rate_per_kg,
                total_amount=total_amount,
                yard=yardd,
                Ewaste=eb
            )
            
            # Update booking status
            eb.aeb_status = 3
            eb.save()
            
            bokid = eb.ewastebooking_id
            ebok = Ewastebooking.objects.get(id=bokid)
            ebok.ewastebooking_status = 2
            ebok.save()
            
            # Generate PDF bill
            return generate_pdf_bill(request, collected_ewaste)
        else:
            return render(request, "EwasteCollector/YardSelection.html", {'res': eb, 'y': yar})
    else:
        return redirect('guest:Home')

    
def logout(request):
    
 del request.session['eid']
 return redirect('guest:Home')

