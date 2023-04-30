from django.forms import ModelForm, Textarea
from .models import Review
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control mt-3'})
    
    class Meta:
        model = Review
        fields = ['text']
    
        widgets = {
            'text': Textarea(attrs={'rows': 4}),
        }

class CreditCardForm(models.Model):
    card_number = models.CharField(max_length=16)
    expiration_month = models.CharField(max_length=2)
    expiration_year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)
    def __str__(self):
        return self.card_number
class DebitCardForm(models.Model):
    card_number = models.CharField(max_length=16)
    expiration_month = models.CharField(max_length=2)
    expiration_year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)
    def __str__(self):
        return self.card_number
class PaypalForm(models.Model):
    paypal_email = models.CharField(max_length=20)
    paypal_password = models.CharField(max_length=20)
    def __str__(self):
        return self.card_number
