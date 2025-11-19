from django import forms

from app1.models import employe

class employe_forms(forms.ModelForm):
    class Meta:
        model = employe
        fields = '__all__'

