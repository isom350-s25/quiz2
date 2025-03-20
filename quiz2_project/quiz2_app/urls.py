from django.urls import path
from quiz2_app.views import static_view, list_view, dynamic_view

urlpatterns = [
    path('static/', static_view, name='static'),
    path('list/', list_view, name='list'),
    path('dynamic/', dynamic_view, name='dynamic'),
]