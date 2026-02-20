from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def show_user_data(request):
    return render(request, 'core/user.html')

def show_page_data(request):
    return render(request, 'core/page.html')

def show_post_data(request):
    return render(request, 'core/post.html')

def show_song_data(request):
    return render(request, 'core/song.html')

