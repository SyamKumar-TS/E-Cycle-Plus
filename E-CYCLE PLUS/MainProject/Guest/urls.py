from django.urls import path
from Guest import views 
app_name="guest"
urlpatterns = [
   
    path('Registration/', views.Reg,name="Registration"), 
    path('Ajaxplace/', views.Ajaxplace,name="Ajax-Place"), 
    path('login/', views.login,name="login"), 
    path('forgotpass/', views.ForgotPass,name="forgotpass"),
    path('validateotp/', views.ValidateOtp,name="validateotp"),
    path('createpass/', views.CreatePass,name="createpass"),

    path('', views.home,name="Home"),

   

]
