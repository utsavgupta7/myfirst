from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello");

def time(request):
    now=datetime.datetime.now()
    html="""<html><head><title>TIME</title></head>
            <body> <h1>CURRENT TIME</h1>the current time is %s</body></html>""" %now
    return HttpResponse(html)    
    
def multiplication(request,nob1,nob2):
    nob1=int(nob1)
    nob2=int(nob2)
    mul=nob1*nob2
    html="""<html><head><title>multiplication</title></head>
            <body> <h1>product</h1>the product of %s and %s is %s </body></html>""" %(nob1,nob2,mul)
    return HttpResponse(html)
    
def greetings(request,name1,name2):
    return render_to_response('greetings.html',{'name1':name1,'name2':name2})

def report(request):
    return render_to_response('report.html',{'referer':request.META.get('HTTP_REFERER','unkonwn'),'user_agent':request.META['HTTP_USER_AGENT'],'remote_addr':request.META['REMOTE_ADDR'],'host':request.get_host(),'full_path':request.get_full_path(),'is_secure':request.is_secure()})
