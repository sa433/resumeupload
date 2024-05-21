from django import forms
from myapp.models import Resume

GENDER_CHOICE = [
    ('Male','Male'),
    ('Female','Female')
]

JOB_CITY_CHOICE = [
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune'),
    ('Chennai', 'Chennai'),
    ('Bengalore', 'Bangalore')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Location', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = "__all__"

        labels = {'dob':'Date of Birth'}

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }