#file created by user, was not created automatically after runnig 'python manage.py startapp polls'


from django.urls import path,include

from . import views

urlpatterns= [ #name of this list should not be changed
    path('',views.index,name='index_'),
    
]

