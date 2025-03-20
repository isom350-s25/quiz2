from django.urls import path
from quiz2_app.views import static_view,list_view,dynamic_view

urlpatterns = [
    path('static/', static_view,),
    path('dynamic/<str:name>', dynamic_view,),
    path('list/', list_view,),
]