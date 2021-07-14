from django.shortcuts import render

# Create your views here.
import folium
def home(request):
    mapFolium=folium.Map([35.3369, 127.7306], zoom_start=10)
    mapFolium = mapFolium.__repr_html_()
    result = {'mapfolium':mapFolium}
    return render(request, template_name='maps/home.html',context=result)
