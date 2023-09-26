# resume_cv/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CVForm
from .models import CV
import os
from django.conf import settings
from .models import CV

# Inside resume_cv/views.py
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def create_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_cv:cv_list')
    else:
        form = CVForm()
    return render(request, 'resume_cv/create_cv.html', {'form': form})

def cv_list(request):
    cvs = CV.objects.all()
    return render(request, 'resume_cv/cv_list.html', {'cvs': cvs})

def download_cv(request, cv_id):
    cv = CV.objects.get(pk=cv_id)

    # Generate the PDF content using ReportLab
    doc = SimpleDocTemplate(f"{cv.name}.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    cv_data = [
        f"CV Name: {cv.name}",
        f"Email: {cv.email}",
        f"Phone: {cv.phone}",
        f"Address: {cv.address}",
        # Add more CV details here based on your desired format
    ]

    elements = []
    for data in cv_data:
        elements.append(Paragraph(data, styles['Normal']))
        elements.append(Spacer(1, 12))  # Add some space between each paragraph

    doc.build(elements)

    # Create a temporary directory for storing generated PDFs
    temp_directory = os.path.join(settings.MEDIA_ROOT, 'temp_pdfs')
    os.makedirs(temp_directory, exist_ok=True)

    # Save the generated PDF to the temporary directory
    temp_pdf_path = os.path.join(temp_directory, f"{cv.name}.pdf")
    with open(temp_pdf_path, 'wb') as temp_pdf_file:
        doc.build(elements, onFirstPage=lambda c, d: c.save())

    # Serve the generated PDF as a download
    with open(temp_pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{cv.name}.pdf"'

    # Clean up the temporary PDF file after serving
    os.remove(temp_pdf_path)

    return response