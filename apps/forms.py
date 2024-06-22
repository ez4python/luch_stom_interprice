from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form, CharField, EmailField

from apps.models import NewsReceiver


class EmailForm(ModelForm):
    class Meta:
        model = NewsReceiver
        fields = ['email']

    def clean_email(self):
        email = self.data.get('email')
        if NewsReceiver.objects.filter(email=email):
            raise ValidationError('This email has already been registered!')
        return email


class ContactForm(Form):
    name = CharField(max_length=100)
    email = EmailField()
    phone = CharField(max_length=20)
    subject = CharField(max_length=200)
    message = CharField()
