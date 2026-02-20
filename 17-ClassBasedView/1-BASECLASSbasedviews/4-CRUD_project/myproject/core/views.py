from django.shortcuts import render, redirect
from .models import Book
from .form import BookForm
from django.views.generic import TemplateView, RedirectView
from django.contrib import messages
from django.views import View

# Create your views here.

class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'core/book_form.html', {'form':form})
    
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "book created succesfully")
            return redirect('book-create')
        return render(request, 'core/book_form.html', {'form':form})
    
    

class BookListView(TemplateView):
    template_name = 'core/book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        genre = self.request.GET.get('genre')

        books = Book.objects.all().order_by('-created_at')

        if genre:
            books = books.filter(genre=genre)

        context['books'] = books
        return context



class BookDetailView(TemplateView):
    template_name = 'core/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['books'] = Book.objects.get(pk=pk)
        return context
    


class BookUpdateView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        form = BookForm(instance=book)
        return render(request, 'core/book_form.html', {"form": form})
    

    def post(self, request, pk):
        book = Book.objects.get(pk = pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "form update successfullly")
            return redirect('book-detail', pk=pk )
        return render(request, 'core/book_form.html', {'form': form})

    
    

class BookDeleteView(RedirectView):
    pattern_name = 'book-list'

    def get_redirect_url(self, *args, **kwargs):
        pk = kwargs.get('pk')
        book = Book.objects.get(pk = pk)
        book.delete()
        messages.success(self.request, "book deleted successfully")
        return super().get_redirect_url()