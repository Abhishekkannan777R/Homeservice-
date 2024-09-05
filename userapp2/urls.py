from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
    path('logoutt',views.logouttt,name='logouttt'),
    path('adminprofile',views.adminprofile),
    path('adminedit',views.adminedit),
    path('adminupdate',views.adminupdate),
    path('adminserviceman',views.adminserviceman),
    path('adminuser',views.adminuser),
    path('adminorder',views.adminorder),
    path('adminmessage',views.adminmessage),
    path('delete1/<int:id>/',views.deleteuser),
    path('delete2/<int:id>/',views.deleteservice),
    path('delete3/<int:id>/',views.deleteorder),
    path('delete4/<int:id>/',views.deletemessage),
    path('confirmadminorder/<int:id>/',views.confirmadminorder),
    path('search',views.search),
    path('servicedetails/<int:id>/',views.servicedetails),
    path('adminuserdetails/<int:id>/',views.adminuserdetails),
    path('bill/<int:id>/',views.bill),
    path('updatebill/<int:id>/',views.updatebill),
    path('billview/<int:id>/',views.billview),
    path('adminalert',views.adminalert),
    path('adminalert/<int:id>/',views.adminaler),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    