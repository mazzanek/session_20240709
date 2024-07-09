from django import forms
from .models import order

class OrdersForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ["firstname", "lastname", "address"]