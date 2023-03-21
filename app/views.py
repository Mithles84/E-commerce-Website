from django.shortcuts import render

# Create your views here.
def IndePage(request):
    return render(request,"app/index.html")
