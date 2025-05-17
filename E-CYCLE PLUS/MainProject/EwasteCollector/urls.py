from django.urls import path
from EwasteCollector import views 
app_name="webcollector"

urlpatterns = [
    path('ewastecolhome/', views.EWHome,name="ewastecolhome"), 
    path('collectorprofile/', views.ECprofile,name="collectorprofile"), 
    path('CollectorChangePassword/', views.CollectorChangePass,name="CollectorChangePassword"), 
    path('ViewmyAllocEC/', views.ViewAllocatedEC,name="ViewmyAllocEC"), 
    path('confewasteb/<int:cid>',views.ConfirmEbook,name="confewasteb"),
    path('delewasteb/<int:cid>',views.DeleteEbook,name="delewasteb"),
    path('viewconfimedeb/', views.ConfirmedEWCollection,name="viewconfimedeb"), 
    path('ecyard/<int:cid>', views.Yardselect,name="ecyard"), 
     path('logout/', views.logout,name="logout"), 
]