from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'nama': 'Wanti anak GOD',
    }
    return render(request, 'index.html', context)
