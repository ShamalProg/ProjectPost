from django import forms
from .models import Lead, Contact, SalesPipeline

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'source']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'company']

# class SalesPipelineForm(forms.ModelForm):
#     class Meta:
#         model = SalesPipeline
#         fields = ['lead', 'stage', 'progress']
        
class SalesPipelineForm(forms.ModelForm):
    class Meta:
        model = SalesPipeline
        fields = ['lead', 'stage']  # Fields to create/update the sales pipeline records

        # Optional: Add validation or custom widgets
        widgets = {
            'lead': forms.Select(attrs={'class': 'form-control'}),
            'stage': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(SalesPipelineForm, self).__init__(*args, **kwargs)
