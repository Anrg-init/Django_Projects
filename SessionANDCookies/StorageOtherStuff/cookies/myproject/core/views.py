from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request, "core/setcookie.html")
    response.set_cookie('payid', 't1233333', max_age=36000)
    return response

def getcookie(request):
    # pay_id = request.COOKIES['payid']
    pay_id = request.COOKIES.get('payid')
    return render(request, "core/getcookie.html" , context = {'payid' : pay_id})

def delcookie(request):
    response = render(request, "core/delcookie.html")
    response.delete_cookie('payid')
    return response


def setsignedcookie(request):
    response =  render(request, 'core/setsignedcookie.html')
    response.set_signed_cookie('token', 't12412', salt='tk')
    return response

def getsignedcookie(request):
    signedcookie = request.get_signed_cookie('token', salt='tk')
    return render(request, 'core/getsignedcookie.html', {'s_cookie': signedcookie})