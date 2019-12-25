from django.urls import path
from festival import views

app_name = 'festival'
urlpatterns = [  
    path('', views.Index.as_view(template_name='index.html'), name='index'),
    path('requests/', views.ManageRequests.as_view(), name='requests'),
    path('request/', views.RequestView.as_view(), name='request'),
]