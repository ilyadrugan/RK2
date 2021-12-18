from django.shortcuts import render
from .models import Orchestra, Musician

def GetOrchestra(request, id):
    return render(request, 'main/orchestra.html', {'data' : {
        'orchestra': Orchestra.objects.filter(id=id)[0],
        'musicians': Musician.objects.filter(orchestra_id=id),
        'orchestras': Orchestra.objects.all(),
    }})

def index(request):
    return render(request, 'main/index.html', {'data' : {
        'orchestras': Orchestra.objects.all()
    }})
