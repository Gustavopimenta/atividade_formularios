from django import forms
from .models import Question

class QuestionForm(forms.Form):
   question_text = forms.CharField(label="Enquete")