from django import forms
from .models import Feedback


class Feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'