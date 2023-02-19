from django import forms
from .models import ProviderMessage,AdminMessage



class ProviderMessageForm(forms.ModelForm):
    class Meta:
        model = ProviderMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your query about service ...'}),
        }

    def clean_subject(self):
        return "Query about service %s" % self.cleaned_data['subject']
    labels = {
            'subject': '',
        }
    widgets = {
            'subject': forms.HiddenInput(),
        }


class AdminMessageForm(forms.ModelForm):
    class Meta:
        model = AdminMessage
        fields = ['name', 'subject', 'email', 'message']
        widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Full name'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
        'message': forms.Textarea(attrs={'placeholder': 'Description message about service and attach your profile in any social media to prove authenticity of your service ...'}),
        }





