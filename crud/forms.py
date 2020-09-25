from django.forms import models
from .models import PersonalDetails

class PersonalDetailsForm(models.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ['name','email','number','address']
