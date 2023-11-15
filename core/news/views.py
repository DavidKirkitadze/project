from django.forms import model_to_dict
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
        w = Articles.objects.all()
        return Response({'posts': ArticlesSerializer(w, many=True).data})

    def post(self, request):
        serializer = ArticlesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        post_new = Articles.objects.create(
            title=request.data['title'],
            anons=request.data['anons'],
            full_text=request.data['full_text'],
            them_id=request.data['them_id']
        )
    
        return Response({'post': ArticlesSerializer(post_new).data})



def news_home(request):
    news = Articles.objects.order_by("-date")
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