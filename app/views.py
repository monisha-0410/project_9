from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':'200','b':'500','c':'700'}
    return render(request,'condition.html',d)

def condition2(request):
    d={'a':'200','b':'500','c':'700'}
    return render(request,'condition2.html',d)

def condition3(request):
    d={'a':'200','b':'500','c':'700'}
    return render(request,'condition3.html',d)