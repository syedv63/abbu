from app2.views import rahul
from django.urls import path
app_name='app2'
urlpatterns=[
    path('rahul/',rahul,name='rahul'),
]
