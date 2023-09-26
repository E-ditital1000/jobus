from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import *
from .models import *
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.views.generic import ListView
from .forms import PaymentForm
from .models import Payment


def home(request):
    qs = JobListing.objects.all()
    jobs = JobListing.objects.all().count()
    user = User.objects.all().count()
    company_name = JobListing.objects.filter(company_name__startswith='P').count()
    paginator = Paginator(qs, 5)  # Show 5 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': jobs,
        'company_name': company_name,
        'candidates': user
    }
    return render(request, "home.html", context)


def about_us(request):
    return render(request, "jobus/about_us.html", {})


def service(request):
    return render(request, "jobus/services.html", {})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "jobus/contact.html", context)


@login_required
def job_listing(request):
    query = JobListing.objects.all().count()

    qs = JobListing.objects.all().order_by('-published_on')
    paginator = Paginator(qs, 3)  # Show 3 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': query

    }
    return render(request, "jobus/job_listing.html", context)


##@login_required
##def job_post(request):
##    form = JobListingForm(request.POST or None)
##    if form.is_valid():
##        instance = form.save()
##        instance.save()
##        return redirect('/jobus/job-listing/')
##    context = {
##        'form': form,
#
#    }
#    return render(request, "jobus/job_post.html", context)


def job_single(request, id):
    job_query = get_object_or_404(JobListing, id=id)

    context = {
        'q': job_query,
    }
    return render(request, "jobus/job_single.html", context)


@login_required
def apply_job(request):
    form = JobApplyForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/')
    context = {
        'form': form,

    }
    return render(request, "jobus/job_apply.html", context)


class SearchView(ListView):
    model = JobListing
    template_name = 'jobus/search.html'
    context_object_name = 'jobus'

    def get_queryset(self):
        return self.model.objects.filter(title__contains=self.request.GET['title'],
                                         job_location__contains=self.request.GET['job_location'],
                                         employment_status__contains=self.request.GET['employment_status'])


def payment_success_view(request):
    return render(request, 'jobus/payment_success.html')

def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobus:payment_success') # Redirect to a success page after payment
    else:
        form = PaymentForm()
    return render(request, 'jobus/payment.html', {'form': form})

from .models import Payment

@login_required
def job_post(request):
    user = request.user

    # Check if the user has a verified payment
    has_verified_payment = Payment.objects.filter(user=user, is_verified=True).exists()

    if not has_verified_payment:
        # Display an error message or redirect to a payment verification page
        return render(request, 'jobus/payment_verification_required.html')

    form = JobListingForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/jobus/job-listing/')

    context = {
        'form': form,
    }
    return render(request, "jobus/job_post.html", context)