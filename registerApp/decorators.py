from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_function):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else: return view_function(request,*args,**kwargs)
    return wrapper