from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm, DeleteBookForm


def xhr_test(request):
    if request.is_ajax():
        message = "Hello AJAX"
    else:
        message = "Hello"
    return HttpResponse(message)


def home(request):
    return render(request, 'index.html')


def books_list(request):
    books_list = Book.objects.all()
    paginator = Paginator(books_list, 4)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render_to_response('books_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=True)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book_edit.html', {'form': form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_edit.html', {'form': form})


def delete(request, pk):
    book_to_delete = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        form = DeleteBookForm(request.POST, instance=book_to_delete)
        if form.is_valid():
            book_to_delete.delete()
            return HttpResponseRedirect("/")
    else:
        form = DeleteBookForm(instance=book_to_delete)
    return render(request, 'books_list.html', {'form': form})
