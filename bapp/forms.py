from django import forms
from .models import fenquiry


class enquiryform(forms.ModelForm):

    class Meta:
        model=fenquiry
        fields=('first_name','last_name','phone_no','email_Id','city_name','state_name','your_enquiry')


