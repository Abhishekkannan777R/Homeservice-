from django.shortcuts import render,redirect
from . models import adtb3
from userapp.models import regtb3,booktb3,servicetb3,emtb3
from django.conf import settings
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def adminlogin(request):    
  
  if request.method=='POST':
        m=request.POST.get('username')
        p=request.POST.get('password')        
               
        obj=adtb3.objects.filter(username=m,password=p) 
        
        if (obj):
            
             for i in obj:
                id_value=i.id
                request.session['idno']=id_value
                messages.success(request,'Login successfully')
                return redirect('/adminhome') 
        else:
             messages.success(request,'invalid username or password')
             return render(request,'adminlogin.html') 
  else:    
        return render(request,"adminlogin.html")
           
def logouttt(request) :
     logout(request) 
     messages.success(request,'Logout successfull')
     return redirect('/adminlogin')      
                                    
                    
   
     

def adminhome(request):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)    
       count = regtb3.objects.filter(option='servicemen').count()
       count2 = regtb3.objects.filter(option='customer').count()   
       count3 = regtb3.objects.filter(verified='False').count()   
       return render(request,'adminhome.html',{"data":obj,"da":count,"dat":count2,"d":count3})

def adminprofile(request):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)    
       return render(request,'adminprofile.html',{"data":obj})   

def adminedit(request):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)    
       return render(request,'adminedit.html',{"data":obj})  

def adminupdate(request):
    se=request.session.get('idno')
    if request.method=='POST' :
         name1=request.POST.get('name')  
         email1=request.POST.get('email')
         username1=request.POST.get('username')
         phone1=request.POST.get('phone')        
         image1=request.FILES.get('image')
         address1=request.POST.get('address')         
         obj=adtb3.objects.get(id=se)       
         obj.name=name1
         obj.email=email1  
         obj.username=username1  
         obj.contact=phone1         
         obj.image=image1 
         obj.address=address1          
         obj.save()
         return redirect('/adminprofile')    
       

def adminserviceman(request):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)  
       ob=servicetb3.objects.all()              
          
       return render(request,'adminserviceman.html',{"data":obj,"da":ob})        

def servicedetails(request,id):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)  
       ob=servicetb3.objects.get(id=id)              
          
       return render(request,'admiservicmoredetail.html',{"data":obj,"da":ob}) 


def adminuserdetails(request,id):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)  
       ob=regtb3.objects.get(id=id)              
          
       return render(request,'admiusermoredetail.html',{"data":obj,"da":ob})    

def adminuser(request):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)  
       ob=regtb3.objects.filter(option="customer")              
          
       return render(request,'adminuser.html',{"data":obj,"da":ob})      

def adminorder(request):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)  
       ob=booktb3.objects.all()              
          
       return render(request,'adminorder.html',{"data":obj,"da":ob})
    
def adminmessage(request):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)  
       ob=emtb3.objects.all()                    
          
       return render(request,'adminmessage.html',{"data":obj,"da":ob})    

def confirmadminorder(request,id):
    order = booktb3.objects.get(id=id)    
    if order.status == 'pending':         
         order.status = 'accepted'      
    elif order.status == 'accepted':
        order.status = 'completed'
    order.save()
    return redirect('/adminorder') 


def deleteuser(request,id):      
    se=request.session.get('idno')  
    if se:
        ob=adtb3.objects.get(id=se)      
        obj=regtb3.objects.filter(id=id)
        obj.delete()
        return redirect('/adminhome')
         
def deleteservice(request,id):      
    se=request.session.get('idno')  
    if se:
        ob=adtb3.objects.get(id=se)      
        obj=servicetb3.objects.filter(id=id)
        obj.delete()
        return redirect('/adminserviceman')

def deleteorder(request,id):      
    se=request.session.get('idno')  
    if se:
        ob=adtb3.objects.get(id=se)      
        obj=booktb3.objects.filter(id=id)
        obj.delete()
        return redirect('/adminorder')    
 
def deletemessage(request,id):      
    se=request.session.get('idno')  
    if se:
        ob=adtb3.objects.get(id=se)      
        obj=emtb3.objects.filter(id=id)
        obj.delete()
        return redirect('/adminmessage') 
    
def search(request):
     se=request.session.get('idno')
     if(request.method=='POST'):
          search=request.POST.get('date','').strip() 
          if (search):
               obj = booktb3.objects.filter(Q(date__iexact=search)) 
               if(obj):
                    ob=adtb3.objects.get(id=se)
                    return render(request,"search.html",{'search':search,'da':obj,'data':ob})
               else:
                    messages.error(request,'No result...?')
                    return redirect ("/adminhome")
          else:
               return redirect("/adminhome")    

def bill(request,id):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)   
       ob=booktb3.objects.get(id=id)   
       return render(request,'bill.html',{"data":obj,"da":ob})

def updatebill(request,id):
    se=request.session.get('idno')    
    if request.method=='POST' :
         subtotal=request.POST.get('subtotal')  
         total=(int(subtotal))+40        
                  
         obj=booktb3.objects.get(id=id)       
         obj.subamount=subtotal
         obj.billamount=total                    
         obj.save()
         return redirect('/adminorder')
        #  return redirect('/bill/id=obj.id/')       
    else:
        return redirect('/adminorder')

def billview(request,id):
    se=request.session.get('idno')    
    if se:                 
       ob=booktb3.objects.get(id=id)
       return render(request,'billview.html',{"da":ob}) 

def adminalert(request):  
    se=request.session.get('idno')    
    if se:      
       obj=adtb3.objects.get(id=se)  
       ob=regtb3.objects.filter(verified="False")            
          
       return render(request,'adminalert.html',{"data":obj,"da":ob})          

def adminaler(request,id):
    se=request.session.get('idno')    
    if se:             
         
       ob=regtb3.objects.get(id=id)
       if ob:
            ob.verified="True"
            ob.save()                                       
            return redirect('/adminalert')   
        
        