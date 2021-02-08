from django.shortcuts import render

# Create your views here.
from mainapp.models import Colors


def autosearch(request):
    result = Colors.objects.all()
    return render(request, 'main.html', {'results': result})
