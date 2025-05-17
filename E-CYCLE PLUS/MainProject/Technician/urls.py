from django.urls import path
from Technician import views 
app_name="technician"
urlpatterns = [
   
     path('technicianhome/', views.homepagetechnician,name="technicianhome"),
     path('technicianprofile/', views.TechnicianMyProfile,name="technicianprofile"),   
     path('technicianedit/', views.TechnicianEditProfile,name="technicianedit"), 
     path('technicianchangepassword/', views.TechnicianChangePass,name="technicianchangepassword"),  
     path('Myassignedservice/', views.TechnicianAssignedService,name="Myassignedservice"), 
     path('confservice/<int:cid>',views.ConfirmServ,name="confservice"),
     path('delservice/<int:cid>',views.DeleteServ,name="delservice"),
     path('viewconfimedservice/', views.ConfirmedServices,name="viewconfimedservice"), 
      path('servbill/<int:bid>', views.ServiceBill,name="servbill"),
      path('logout/', views.logout,name="logout"), 
       
]
