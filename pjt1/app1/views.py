from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def sr (request):
   return HttpResponse("name")



def odd (request,num):

    if num == 0:
        return HttpResponse("enter a valid number")
    elif(num % 2) == 0:
    
        return HttpResponse("%d is even "%num)
    else:
        return HttpResponse(" %d is odd "%num)
    
def str (request,n):
      a = n[::-1]
      return HttpResponse(a)
  
def abc(request,n,m):
      c =m+n
      return HttpResponse(c)
  
  
def index(request):
    return render(request,'index.html')

def ind(request):
    return render(request,'index1.html')


def vowel(request, v):
    vowels = ["a", "e", "i", "o", "u"]
    if v in vowels:
        return HttpResponse("%s is a vowel" % v)
    else:
        return HttpResponse("%s is not a vowel" % v)
    
def indo(request):
    return render(request,'index3.html')