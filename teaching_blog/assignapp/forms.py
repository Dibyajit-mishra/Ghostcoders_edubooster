from django import forms
from .models import User

class StudentRegistration (forms.ModelForm):
  class Meta:
      model = User
      fields = ['Task', 'description']
      widgets = {
          'Task': forms.TextInput(attrs = {'class':'form-control'}),
          'description': forms.Textarea(attrs={'class': 'form-control'}),
                }

