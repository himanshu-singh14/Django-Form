from django import forms
from .models import MarkyticsForm


# we make form from existing model
class MarkyticsForms(forms.ModelForm):
    
    class Meta:
        model = MarkyticsForm

        # fields that will be see in the form
        fields = ('location','description','date','time','incident_location','initial_severity','suspected_cause',
            'immediate_actions_taken','is_environmental_incident','is_injury','is_property_damage','is_vehicle',
            'reported_by')

        # we add properties to each tags
        widgets = {
            'location': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':"3"}),
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'time': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'incident_location': forms.Textarea(attrs={'class':'form-control', 'rows':"3"}),
            'initial_severity': forms.Select(attrs={'class':'form-control'}),
            'suspected_cause': forms.Textarea(attrs={'class':'form-control', 'rows':"3"}),
            'immediate_actions_taken': forms.Textarea(attrs={'class':'form-control', 'rows':"3"}),
            'reported_by': forms.TextInput(attrs={'class':'form-control'}),
        }