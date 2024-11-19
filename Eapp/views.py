from django.shortcuts import render
from django.http import HttpResponse
import logging

# Create your views here.
posts=[
        {'id':1,'title':'post 1','content':'content of post 1'},
        {'id':2,'title':'post 2','content':'content of post 2'},
        {'id':3,'title':'post 3','content':'content of post 3'},
        {'id':4,'title':'post 4','content':'content of post 4'},
        
    ]
def demo(request):
    
    return render(request,'index.html',{'posts':posts})

def detail(request,id):
    post = next((item for item in posts if item['id'] == id),None)
    # logger=logging.getLogger("testing")
    # logger.debug(f'post variable is {post}')
    return render(request,'detail.html',{'post':post})

def new(request,course):
    return HttpResponse(course)

