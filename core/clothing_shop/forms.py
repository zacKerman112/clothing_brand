from django import forms
from login.models import CustomUser

class RegistrtionForm(forms.ModelForm):
    age = forms.IntegerField(label="Your age" , min_value=0)

    class Meta:
        model = CustomUser
        fields = ['username' , 'email' , 'avatar']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if 'admin' in username.lower():
            raise forms.ValidationError("the username mustn`t contain a word admin!")
        return username
    

    def age_limit(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError('Our apologies but this site is meant only for adults')
        return age