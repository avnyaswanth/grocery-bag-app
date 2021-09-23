from django import forms
from django.forms import ModelForm
from django.forms.models import fields_for_model
from .models import GroceryItems
from django import forms
from django.conf import settings
from django.forms import ModelForm

class GroceryAddItemForm(ModelForm):
    class Meta:
        model = GroceryItems
        fields = ['itemName','itemQuantity','flag','dateAdded']