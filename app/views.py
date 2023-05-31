from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'SRAVANI','age':21}
    return render(request,'wish.html',context=d)
def conditions(request):
    d={'a':1000,'b':1200,'c':400}
    return render(request,'conditions.html',context=d)
def loop(request):
    d={'name':''}
    return render(request,'loop.html',context=d)