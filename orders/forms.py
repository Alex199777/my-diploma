

from django import forms

class CreateOrderForm(forms.Form):
    username = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    pay = forms.ChoiceField(choices=[("0", "False"),
                                   ("1", "True")
                                   ])