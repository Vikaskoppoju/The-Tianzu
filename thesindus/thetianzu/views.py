from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StatesData,Loc
import folium
import geocoder
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
    return render(request,'thetianzu/home.html',context)

def state(request, id):
    data = StatesData.objects.get(id=id)
    return render(request,'thetianzu/state.html',{'record':data})