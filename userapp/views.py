from django.shortcuts import render,redirect
from . models import regtb3,servicetb3,booktb3,emtb3
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.


def home(request):
    return render(request,"home.html")
def login(request): 
     if request.method=='POST':
        m=request.POST.get('username')
        p=request.POST.get('password')
        o=request.POST.get('option')
        print(o)
        
        obj = regtb3.objects.filter(username=m,password=p,option=o) 
        
        if (obj):
            
            
             for i in obj:
                id_value=i.id
                request.session['idno']=id_value
                if o=="customer":
                     messages.success(request,'Login successfully')
                     return redirect("/customerhome")
                else:
                       
                                    
                    new= regtb3.objects.get(id=id_value) 
                    
                    try:
                        service=servicetb3.objects.get(owner=new)
                        messages.success(request,'Login successfully')
                        if service :                         
                            
                            return redirect("/servicehome") 
                    except:
                          
                        
                        
                        # if  service.is_complete: 
                        #     print("inside if")                    
                        #     return redirect("/servicehome")
                       
                            messages.success(request,'Update Profile then continue service')
                            return redirect("/addservice")
        else: 
            messages.success(request,'invalid username or password')
             
            return render(request,"login.html") 
     else:    
        return render(request,"login.html")
def register(request):       
    if request.method=='POST' :
         name1=request.POST.get('name')  
         email1=request.POST.get('email')
         username1=request.POST.get('username')
         password1=request.POST.get('password')
         phone1=request.POST.get('phone')
         date1=request.POST.get('date')
         gender1=request.POST.get('gender')
         image1=request.FILES.get('image')
         address1=request.POST.get('address')
         option1=request.POST.get('option')
         check=regtb3.objects.filter(username=username1)
         if(check):
              messages.success(request,'username alredy exists ')
              return render(request,"register.html")
         obj=regtb3.objects.create(name=name1,email=email1,username=username1,password=password1,contact=phone1,date=date1,gender=gender1,image=image1,address=address1,option=option1)
         obj.save()
         subject="Thank You"+ name1
         message="Account Registered Succesfull"
         send_mail(subject,message,settings.EMAIL_HOST_USER,[email1],fail_silently=False) 
         
        #  subject="New user registerd" + name1
        #  message=" Daily Fix"
        #  email="abhishekkannan777@gmail.com"
        #  send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False) 
         if obj:
                messages.success(request,'Account registered succesful ')
                return redirect("/login")
         else:
                return render(request,"register.html")                 
    return render(request,"register.html")
def about(request):          
    return render(request,"about.html")
def contact(request):          
    if request.method=='POST':
         ename=request.POST.get('name')
         email1=request.POST.get('email')
         phone=request.POST.get('phone')
         emsg=request.POST.get('message')
         obj=emtb3.objects.create(name=ename,email=email1,contact=phone,message=emsg)
         obj.save()
         subject="Thank You"+ ename
         message="Thank you for the enquiry..."
         send_mail(subject,message,settings.EMAIL_HOST_USER,[email1],fail_silently=False)           
         messages.success(request,"email send succesfully")
         return redirect("/contact")

    else:
      return render(request,"contact.html")
def service(request):          
    return render(request,"service.html")
def customerhome(request):
    se=request.session.get('idno')    
    if se:      
       obj=regtb3.objects.get(id=se)              
       return render(request,"customerhome.html",{"data":obj})
    
    else:
        return redirect("/login")
         
def servicehome(request):      
    se=request.session.get('idno')   
    if se:           
             obj=regtb3.objects.get(id=se)    
             return render(request,"servicehome.html",{"data":obj})

def logoutt(request) :
     logout(request) 
     messages.success(request,'Logout successfull')
     return redirect("/login")

def custservice(request):
    se=request.session.get('idno')    
    if se:      
       obj=regtb3.objects.get(id=se)              
       return render(request,"custservice.html",{"data":obj})

def profile(request):
    se=request.session.get('idno')              
    obj=regtb3.objects.get(id=se)              
    return render(request,"profile.html",{"data":obj})
    
def edit(request):
    se=request.session.get('idno')    
    if se:      
       obj=regtb3.objects.get(id=se)              
       return render(request,"edit.html",{"data":obj})    

def update(request):
    se=request.session.get('idno')
    bb=regtb3.objects.get(id=se)
    if request.method=='POST' :
         name1=request.POST.get('name')  
         email1=request.POST.get('email')
         username1=request.POST.get('username')
         password1=request.POST.get('password')
         phone1=request.POST.get('phone')
         date1=request.POST.get('date')         
         image1=request.FILES.get('image')
         address1=request.POST.get('address')         
         obj=regtb3.objects.get(id=se)       
         obj.name=name1
         obj.email=email1  
         obj.username=username1    
         obj.password=password1  
         obj.contact=phone1
         obj.date=date1  
         obj.image=image1 
         obj.address=address1          
         obj.save()
         if bb.option=="customer":
               return redirect('/profile')
         else:
             return redirect('/servicepro')

def updateservice(request):
    se=request.session.get('idno')    
    if request.method=='POST' :
         service=request.POST.get('service')  
         experiance=request.POST.get('date')        
                  
         obj=servicetb3.objects.get(owner=se)       
         obj.service=service
         obj.date=experiance                    
         obj.save()
         return redirect('/servicepro')

def servicepro(request):     
     se=request.session.get('idno')    
     if se:    
       objj=regtb3.objects.get(id=se)   
       obj=servicetb3.objects.get(owner=se)                         
       return render(request,"servicepro.html",{"data":objj,"ls":obj })    
     
def serviceedit(request):
    se=request.session.get('idno')    
    if se:     
       objj=regtb3.objects.get(id=se)                   
       return render(request,"serviceedit.html",{"data":objj})  
          
# def explore(request):
#      se=request.session.get('idno')     
#      if se:      
#        obj=regtb3.objects.get(id=se) 
#        objj=servicetb3.objects.all()    
         
#        print(service)        
#        return render(request,"explore.html",{"dataa":objj,"data":obj})    
     
def addservicedet(request):
    se=request.session.get('idno')   
    if se:           
             
        if request.method=='POST'  :
           
            work=request.POST.get('work')            
            service=request.POST.get('service')            
            idd=request.POST.get('id')            
            image=request.FILES.get('image')              
            owner=regtb3.objects.get(id=se)           
            obj=servicetb3.objects.create(owner=owner,date=work,service=service,idd=idd,image=image)
            
            obj.save()
            if obj:
                    ob=servicetb3.objects.get(owner=owner)
                    if ob:
                            obj.is_complete=True
                            obj.save()
                            return redirect("/servicehome")
                    else:
                         return redirect("/addservice")
            else:
                
                  return redirect('/login')
        else:
               obj=regtb3.objects.get(id=se)              
               return render(request,"addservicedet.html",{"data":obj})     
                
def book(request,id):
     se=request.session.get('idno')     
     
     if se:  
        ob=regtb3.objects.get(id=se) 
        # obj=regtb3.objects.get(id=id)
         #    ob=servicetb3.objects.get(id=id)       
         

        if request.method=='POST'  :
            print(id)
            bname1=request.POST.get('name')            
            bmobile1=request.POST.get('mobile')      
            busername1=request.POST.get('username')      
            baddress1=request.POST.get('address')
            bdate=request.POST.get('date')
            bdays=request.POST.get('days')  
            service=servicetb3.objects.get(id=id).service
            serviceman=servicetb3.objects.get(id=id).owner.name
            cusername=servicetb3.objects.get(id=id).owner.username
            contact=servicetb3.objects.get(id=id).owner.contact           

                        
                     
            obj=booktb3.objects.create(bname=bname1,bmobile=bmobile1,usename=busername1,baddress=baddress1,date=bdate,days=bdays,service=service,serviceman=serviceman,cusername=cusername,contact=contact)            
            obj.save()
            if obj:              
               return redirect('/mybook')
            else:
               return redirect('/book')
        else:

            return render(request,"book.html",{"data":ob})    
           
                






       
             
def elect(request):
     se=request.session.get('idno')    
     ob=regtb3.objects.get(id=se) 
     if se:        
       obj=servicetb3.objects.filter(service="electrician")                
                
       return render(request,"elect.html",{"dat":obj,"data":ob})  
     
def carp(request):
     se=request.session.get('idno')    
     ob=regtb3.objects.get(id=se) 
     if se:        
       obj=servicetb3.objects.filter(service="carpenter")               
                
       return render(request,"carp.html",{"dat":obj,"data":ob})      

def plum(request):
     se=request.session.get('idno')    
     ob=regtb3.objects.get(id=se) 
     if se:        
       obj=servicetb3.objects.filter(service="plumber")              
                
       return render(request,"plum.html",{"dat":obj,"data":ob})     

def paint(request):
     se=request.session.get('idno')    
     ob=regtb3.objects.get(id=se) 
     if se:        
       obj=servicetb3.objects.filter(service="painter")              
                
       return render(request,"paint.html",{"dat":obj,"data":ob})       

def fit(request):
     se=request.session.get('idno')    
     ob=regtb3.objects.get(id=se) 
     if se:        
       obj=servicetb3.objects.filter(service="fitter")              
                
       return render(request,"fit.html",{"dat":obj,"data":ob})       

def weld(request):
     se=request.session.get('idno')    
     ob=regtb3.objects.get(id=se) 
     if se:        
       obj=servicetb3.objects.filter(service="welder")              
                
       return render(request,"weld.html",{"dat":obj,"data":ob})  
def mybook(request):
     se=request.session.get('idno')
     if se:
           ob=regtb3.objects.get(id=se)      
           obj = booktb3.objects.filter(usename=ob.username)              
        #    obj=booktb3.objects.all()  
           return render(request,"mybook.html",{"data":ob,"da":obj})   


def myorder(request):
     se=request.session.get('idno')
     if se:
           ob=regtb3.objects.get(id=se)      
           obj = booktb3.objects.filter(cusername=ob.username)                       
        #    obj=booktb3.objects.all()  
           return render(request,"myorder.html",{"data":ob,"da":obj}) 

def delete(request,id):      
    se=request.session.get('idno')  
    if se:
        ob=regtb3.objects.get(id=se)      
        obj=booktb3.objects.filter(id=id)
        obj.delete()
        if ob.option=="customer":       
             return redirect('/mybook')   
        else:
             return redirect('/myorder')   

def confirm_order(request,id):
    order = booktb3.objects.get(id=id)    
    if order.status == 'pending':         
         order.status = 'accepted'      
    elif order.status == 'accepted':
        order.status = 'completed'
    order.save()
    return redirect('/myorder')
   
    
                