from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticlesSerializer



class ArticlesAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Ford RS200'})

#class ArticlesAPIView(generics.ListAPIView):
    #queryset = Articles.objects.all()
    #serializer_class = ArticlesSerializer



def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "form wasn't corrected"

    form = ArticlesForm()
    
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)