from django.urls import path
from first_app import views

appname = 'first_app'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative',views.relative,name='rrelative'),
]