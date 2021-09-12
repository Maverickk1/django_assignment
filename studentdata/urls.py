from . import views
from django.urls import path
from .views import StudentList

urlpatterns = [
    path('',views.home),
    path('byid/<id>',views.byid,name='byid'),
    path('studentlist/', StudentList.as_view(),name='studentlist' ),
]
