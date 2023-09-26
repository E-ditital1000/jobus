from django.db import models
import os

def resume_cv_directory_path(instance, filename):
    # Customize this function according to your needs.
    # This function determines the upload path for the thumbnail field.
    return os.path.join('thumbnails', filename)

class CV(models.Model):
    # Header Section
    thumbnail = models.ImageField(blank=True, null=True, upload_to=resume_cv_directory_path)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    # Experience Section
    experience_title = models.CharField(max_length=100, null=True, blank=True)
    experience_company = models.CharField(max_length=100, null=True, blank=True)
    experience_start_date = models.DateField(null=True, blank=True)
    experience_end_date = models.DateField(null=True, blank=True)
    experience_description = models.TextField(null=True, blank=True)

    # Education Section
    education_degree = models.CharField(max_length=100, null=True, blank=True)
    education_institution = models.CharField(max_length=100, null=True, blank=True)
    education_start_date = models.DateField(null=True, blank=True)
    education_end_date = models.DateField(null=True, blank=True)

    # Skills Section
    skills = models.TextField(null=True, blank=True)

    # Summary Section
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name