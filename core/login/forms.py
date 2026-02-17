from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    age = forms.IntegerField(label="Ваш вік", min_value=0)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar']

    # Твоя валідація для 10 балів
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if "admin" in username.lower():
            raise forms.ValidationError("Ім'я не може містити 'admin'!")
        return username