from django import forms

""" user order form """
class UserOrderForm(forms.Form):
    product_id=forms.IntegerField(
        widget=forms.HiddenInput()
    )
    count=forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1
    )