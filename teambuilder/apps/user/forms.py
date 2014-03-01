from django import forms
from teambuilder.apps.user.models import User


class registerForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Los passwords no coinciden")
        return password2

    def save(self, commit=True):
        user = super(registerForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = False
        if commit:
            user.save()
        return user


class summonerInformation(forms.ModelForm):
    class Meta:
        model = User
        fields = ('in_game_name', 'region')


class personalInformation(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

