from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('student/', views.StudetGenericApiView.as_view(), name='students'),
    path('student/<int:id>/', views.StudetGenericApiView.as_view(), name='student')
]