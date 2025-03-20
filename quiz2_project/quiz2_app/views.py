from django.shortcuts import render


# Create your views here.
def static_view(request):
    return render(request,'static.html',)

def list_view(request):
    shopping_list = ['apple', 'banana', 'cherry']
    return render(request, 'list.html', {'shopping_list': shopping_list})

def dynamic_view(request,name):
    return render(request, 'dynamic.html', {'name': name})