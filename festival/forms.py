from django import forms
from festival.models import Voice

class VoteForm(forms.ModelForm):

    class Meta:
        model = Voice
        fields = '__all__'