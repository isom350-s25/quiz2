from django.shortcuts import render

# Create your views here.
def static_view(request):
    x = 'Welcome to the Quiz 2 Application!'
    context = {'x': x}
    return render(request, 'static.html', context)

def list_view(request):
    shopping_list = ['apple', 'banana', 'cherry']
    context = {'shopping_list': shopping_list}
    return render(request, 'list.html', context)

def dynamic_view(request):
    name = request.GET.get('name', 'Guest')
    context = {'name': name}
    return render(request, 'dynamic.html', context)


