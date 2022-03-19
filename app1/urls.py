from app1.views import viratkohli
from django.urls import path
app_name='app1'
urlpatterns=[
    path('viratkohli/',viratkohli,name='viratkohli'),
]