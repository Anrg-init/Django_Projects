from django.shortcuts import render
from datetime import datetime, timedelta, timezone


def setsession(request):
    request.session['fname'] = 'Sonam'
    request.session['lname'] = 'trump'

    return render(request, 'core/setsession.html')


def getsession(request):
    fname = request.session['fname']
    lname = request.session['lname']
    return render(request, 'core/getsession.html', {'fname': fname, 'lname': lname})


def delsession(request):
    if 'fname' in request.session:
        del request.session['fname']
    return render(request, 'core/delsession.html')


def flushsession(request):
    request.session.flush() 
    return render(request, 'core/flushsession.html')


def sessionmethodsinview(request):
    data = {
        'keys': request.session.keys(),
        'items': request.session.items(),
        'expiry': request.session.get_expiry_age(),
        'expiry_date': request.session.get_expiry_date(),
        'session_key': request.session.session_key,
    }
    return render(request, 'core/sessionmethodinview.html', data)


def sessionmethodsintemplate(request):
    keys = request.session.keys()
    items = request.session.items
    return render(request, 'core/sessionmethodintemplate.html', {'keys': keys, 'items': items})


def sessionclear(request):
    request.session.clear()
    return render(request, 'core/sessionclear.html')


def settestcookie(request):
    response = render(request, 'core/settestcookie.html')
    response.set_cookie('testcookie', 'Django')
    return response


def checktestcookie(request): 
    test = request.COOKIES.get('testcookie')
    return render(request, 'core/checktestcookie.html', {'test': test})


def deltestcookie(request):
    response = render(request, 'core/deltestcookie.html')
    response.delete_cookie('testcookie')
    return response
