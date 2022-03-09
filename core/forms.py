from django import forms
from django.core.validators import RegexValidator

class FeedbackForm(forms.Form):
    phoneNumberRegex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
        message='Введите корректный номер телефона')
    name = forms.CharField(max_length=25, label='Ваше имя',
        widget=forms.TextInput(attrs={'class': 'order-inner__input'}))
    phone = forms.CharField(max_length=16, label='Ваш телефон',
        widget=forms.TextInput(attrs={'class': 'order-inner__input'}),
        validators=[phoneNumberRegex])
    email = forms.EmailField(label='Email адрес',
        widget=forms.TextInput(attrs={'class': 'order-inner__input'}))
    text = forms.CharField(label=' Ваше сообщение',
        widget=forms.Textarea(attrs={'class': 'order-inner__text-area'}))
