from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('',views.home),
    path('home',views.home),
    path('login',views.login),
    path('register',views.register),
    path('about',views.about),
    path('contact',views.contact),
    path('service',views.service),
    path('customerhome',views.customerhome),
    path('servicehome',views.servicehome),
    path('logout',views.logoutt,name='logout'),
    path('custservice',views.custservice),
    path('profile',views.profile),
    path('edit',views.edit),
    path('update',views.update),
    path('updateservice',views.updateservice),
    path('serviceedit',views.serviceedit),
    path("servicepro",views.servicepro),
    # path("explore",views.explore),
    path("addservice",views.addservicedet,name='addservice'),
    path("book/<int:id>/",views.book),
    path("elect",views.elect),
    path("carp",views.carp),
    path("plum",views.plum),
    path("paint",views.paint),
    path("weld",views.weld),
    path("fit",views.fit),
    path("mybook",views.mybook),
    path("myorder",views.myorder),
    path('delete/<int:id>/',views.delete),
    path('confirm_order/<int:id>/',views.confirm_order),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
