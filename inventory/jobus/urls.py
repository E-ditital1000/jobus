from django.urls import path
from .views import *

app_name = 'jobus'

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('about/', about_us, name='about'),
    path('service/', service, name='service'),
    path('job-post/', job_post, name='job-post'),
    path('job-listing/', job_listing, name='job-listing'),
    path('job-single/<int:id>/', job_single, name='job-single'),
    path('search/', SearchView.as_view(), name='search'),
    path('apply/', apply_job, name='apply'),
    path('make-payment/', make_payment, name='make_payment'),
    path('payment-success/', payment_success_view, name='payment_success'),
    
]