from django import forms
from .models import *
from .models import Payment

class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['Email'].widget.attrs['placeholder'] = 'Enter a valid E-mail'

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'Email',
            'subject',
            'message'
        ]


class JobListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobListingForm, self).__init__(*args, **kwargs)
        self.fields['job_location'].widget.attrs['placeholder'] = 'Monrovia,Liberia'
        self.fields['Salary'].widget.attrs['placeholder'] = '60k-80k BDT, 4k-5k USD, Negotiable'
        self.fields['title'].widget.attrs['placeholder'] = 'Software Engineer, Web Designer'
        self.fields['application_deadline'].widget.attrs['placeholder'] = '2023-8-11'

    class Meta:
        model = JobListing
        exclude = ('user', 'image')
        labels = {
            "job_location": "Job Location",
            "published_on": "Publish Date"
        }


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = '__all__'
        labels = {
            "file": "CV (pdf format)",
            "name": "Full Name",
            "cover_letter": "Cover Letter",  # Custom label for the cover_letter field
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'screenshot']
        labels = {
            'amount': 'Payment Amount',
            'screenshot': 'Payment Screenshot',
        }
        help_texts = {
            'amount': 'Enter the payment amount in decimal format (e.g., 100.00).',
            'screenshot': 'Upload a screenshot of your payment receipt.',
        }

   
