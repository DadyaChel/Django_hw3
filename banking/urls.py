from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientListView.as_view(), name='index'),
    path('<int:pk>/detail/', views.ClientDetailView.as_view(template_name='dt.html'), name='detail'),
    # path('<int:pk>/result/', views.ClientResultView.as_view(template_name='result.html'), name='result'),
]