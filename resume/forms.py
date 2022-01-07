# forms.py создал отдельно
from django.forms import ModelForm
from .models import ProgrammingLanguages


class ProgramLangForm(ModelForm):
    class Meta:
        model = ProgrammingLanguages
        fields = ('title', 'content')
