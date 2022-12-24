from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StatesData,Loc
import folium
import geocoder
from django.core.mail import send_mail
from django.contrib import messages
def home(request):
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    obj = Loc.objects.all()
    for i in obj:

        v=i.lat
        l=i.lon
        #print(v)
        #print(l)
        folium.Marker(
        location=[v,l],
        popup='<a href="http://127.0.0.1:8000/state/'+str(i.id)+'" target="blank">'+str(i.statnam)+'</a>',icon=folium.Icon(color='green',prefix='glyphicon',icon='off'),max_bound=True).add_to(m)
        # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,

            
    }
    return render(request,'thetianzu/index.html',context)

def new_func():
    obj = Loc.objects.all()
    return obj

def state(request, id):
    data = StatesData.objects.get(id=id)
    return render(request,'thetianzu/game.html',{'record':data})

def signup(request):
	if request.method =="POST":
		emai=request.POST['User']
		passw=request.POST['password']
		print(emai,passw)
		
		send_mail("Thankyou For visiting our site","Welcome to etantri","etantri2k22@gmail.com",[emai],fail_silently=False)
		return HttpResponse("your data submitted successfully")

	else:
		return render(request,'thetianzu/signup.html')

def contact(request):
    if request.method =="POST":
        ename=request.POST['ename']
        emai=request.POST['email']
        feed=request.POST['feedback']
        send_mail("Thankyou For visiting our site","Welcome to Etantri","etantri2k22@gmail.com",[emai],fail_silently=False)
        send_mail("Hey new supporter!"+ename,feed,"etantri2k22@gmail.com",["koppojuvikaskumar@gmail.com"],fail_silently=False)
        messages.success(request, 'Your Data is Taken')

	
    
    return render(request,'thetianzu/contactus.html')
    
    