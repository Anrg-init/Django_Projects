from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def user_by_id(request, id):
    return HttpResponse(f"User ID is: {id}")

def user_by_name(request, username):
    return HttpResponse(f"Username is: {username}")

def post(request, slug):
    return HttpResponse(f"Post slug: {slug}")

def archive(request, yyyy):
    return HttpResponse(f"Archive year: {yyyy}")
