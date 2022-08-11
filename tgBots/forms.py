from django import forms
from tgBots.models import *

class IdUser(forms.Form):
    id_works = forms.CharField(max_length=255)
    url_name = forms.CharField(max_length=255)