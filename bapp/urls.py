from django.urls import path,include
from bapp import views

app_name='bapp'

urlpatterns = [
    path('service/',views.service,name='service'),
    path('client/',views.client,name='client'),
    path('enquiry/',views.enquiry,name='enquiry')
]