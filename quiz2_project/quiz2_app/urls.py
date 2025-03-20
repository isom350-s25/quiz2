
from django.urls import path
from quiz2_app import views
urlpatterns = [
    path('static/', views.static_view),
    path('list/', views.list_view),
    path('dynamic/<str:name>/', views.dynamic_view),
]
