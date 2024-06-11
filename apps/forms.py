from django.core.exceptions import ValidationError
from django.forms import ModelForm

from apps.models import NewsReceiver


class EmailForm(ModelForm):
    class Meta:
        model = NewsReceiver
        fields = ('email',)

    def clean_email(self):
        email = self.data.get('email')
        if NewsReceiver.objects.filter(email=email):
            raise ValidationError('This email has already been registered!')
        return email
