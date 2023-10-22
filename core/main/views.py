from django.shortcuts import render



def index(request):
    date = {
        'title': 'Home page',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'nissan',
            'age': '20',
            'nobby': 'Music'
        }
    }
    return render(request, 'main/index.html', date)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')
    