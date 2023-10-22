from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

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
    
    date = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', date)