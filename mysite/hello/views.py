from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myview(request):
    oldval = request.COOKIES.get('zap', None)
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4:
        del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    if oldval:
        resp.set_cookie('zap', int(oldval)+1)   # No expired date = until browser close
    else:
        resp.set_cookie('zap', 42)  # No expired date = until browser close
        resp.set_cookie('sakaicar', 42, max_age=1000)   #seconds until expire
    resp.set_cookie('dj4e_cookie', '1f00a892', max_age=1000)
    return resp

