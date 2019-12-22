from django.urls import path
from festival.views import Index

app_name = 'festival'
urlpatterns = [  
    path('', Index.as_view(template_name='index.html'), name='index'),
]