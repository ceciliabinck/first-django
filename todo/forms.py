from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        # will gives our form some information about itself.
        model = Item
        fields = ['name', 'done']

# The idea of creating this form in Django is that rather than writing an
# entire form ourselves in HTML.
# We can simply render it out as a template variable.
