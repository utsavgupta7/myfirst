from django.shortcuts import render
from myfirst.books.models import books
from django.http import HttpResponse

def search_form(request):
    return render(request,'search_form.html')

def search(request):
    errors=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append("enter a search term")
        elif len(q)>20:
            errors.append("enter at most 20 characters")
        else:
            Books=books.objects.filter(title__icontains=q)
            return render(request,'search_results.html',{'Books':Books,'query':q})
    return render(request,'search_form.html',{'errors':errors})
