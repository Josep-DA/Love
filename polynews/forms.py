from django import forms


class LoveFrom(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    your_email = forms.EmailField(label="Your email", max_length=100)
    to_name = forms.CharField(label="To name", max_length=100)
    OPTIONS = (
        ("g", "Girl"),
        ("b", "Boy"),
    )
    gender = forms.ChoiceField(choices=OPTIONS)