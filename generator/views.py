from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def rangen(request):
    rannumber= random.randint(1,100)
    return rannumber

rannumber = rangen(0)

def index(request):

    return render(request,'generator/index.html')

def checker(request):

    print(rannumber)
    if request.method=='POST':
        innum = int(request.POST['inputnumber'])
        print(innum)
        if (rannumber==innum):
            flag = 'Congratulation!!! Number Matched'
            return render(request,'generator/index.html',{'flag':flag})
        elif(innum>rannumber):
            flag = 'Oops!!! You Entered a High Value, Try Again!!!'
            return render(request,'generator/index.html',{'flag':flag})
        else:
            flag = 'Oops!!! You Entered a Low Value, Try Again!!!'
            return render(request,'generator/index.html',{'flag':flag})
