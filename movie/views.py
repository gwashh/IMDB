from django.shortcuts import render

# Create your views here.
from django.view.generics import ListView , DetailView
from .models import Movie

class MovieLIstList(ListView):
    model = Movie
    # context_object_name = ''
    # template_name=''


class MovieDetail(DetailView):
    model = Movie
    # template_name=''