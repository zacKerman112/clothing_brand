from django import forms

class RegistrationForm(forms.ModelForm):
    age = forms.IntegerField(label="Your age", min_value=0)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar']

 
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and "admin" in username.lower():
            raise forms.ValidationError("The name can't contain 'admin'.")
        return username

   
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 18:
            raise forms.ValidationError("You're under 18, adults only.")
        return age