from django.urls import path
from . import views
urlpatterns =[
    path('members',views.members,name='members'),
    path('details/<int:id>', views.details, name='details'),
    path('',views.main,name='main'),
    path('test/',views.testing, name = 'testpage')

]