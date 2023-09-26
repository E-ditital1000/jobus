from django import forms
from .models import CV

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = (
            "name", "email", "phone", "address",
            "experience_title", "experience_company", "experience_start_date", "experience_end_date", "experience_description",
            "education_degree", "education_institution", "education_start_date", "education_end_date",
            "skills", "summary", "thumbnail",  # Include "thumbnail" field here
        )