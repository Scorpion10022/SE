from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/<str:r1>/<str:r2>/<str:r3>/<str:r4>/<str:r5>/', views.result, name='result')
]
