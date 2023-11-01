from django.views.generic import ListView
from .models import Movie
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-list')
    else:
        form = ContactForm()

    return render(request, 'add_contact.html', {'form': form})



