from django.shortcuts import render

# Create your views here.
def static_view(request):
    welcome = "Welcome to my page"
    context = {"message" : welcome} 

    return render(request, 'static.html',context)
def list_view(request):
    my_list = ["apple", "banana", "cherry"]
    context = {"list" : my_list}
    return render(request, 'list.html', context)
def dynamic_view(request, name):
    others = request.GET.get('x')
    context = {"name" : name , "names" : others}
    return render(request, 'dynamic.html', context)