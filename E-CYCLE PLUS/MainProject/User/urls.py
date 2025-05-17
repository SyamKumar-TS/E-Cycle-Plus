from django.urls import path
from User import views 
app_name="webuser"

urlpatterns = [
    path('userhome/', views.homepageuser,name="userhome"),
    path('userprofile/', views.UserMyProfile,name="userprofile"),  
    path('useredit/', views.EditProfile,name="useredit"), 
    path('userchangepass/', views.UserChangePass,name="userchangepass"),  
    path('usercomp/', views.UserComplaint,name="usercomp"),
    path('userfeed/', views.UserFeedback,name="userfeed"),  
    path('delcomplaint/<int:cid>',views.DelComp,name="delcomplaint"),
    path('servicebook/', views.ServiceBooking,name="servicebook"),
    path('requestedservice/', views.MyServiceBooking,name="requestedservice"),
    path('delservice/<int:sid>',views.DelServ,name="delservice"),
    path('viewbill/<int:bid>', views.ViewServiceBill,name="viewbill"),
    path('viewpay/<int:blid>', views.PaymentService,name="viewpay"),
    path('userewastereq/', views.UserEWaste,name="userewastereq"), 
    path('viewuserewastereq/', views.ViewUserEWaste,name="viewuserewastereq"), 
    path('product/', views.Prodview,name="product"),
    path('logout/', views.logout,name="logout"), 
]   