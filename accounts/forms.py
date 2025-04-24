from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django import forms
from .models import CustomUser
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import check_password



SECURITY_QUESTIONS = [
    ("birth_city", "What city were you born in?"),
    ("first_pet", "What was the name of your first pet?"),
    ("mother_maiden", "What is your mother’s maiden name?"),
    ("favorite_teacher", "Who was your favorite teacher in school?"),
]


class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([
            f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))

class CustomUserCreationForm(UserCreationForm):
    security_question_1 = forms.ChoiceField(
        choices=SECURITY_QUESTIONS,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Security Question 1"
    )
    security_answer_1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Answer 1"
    )
    security_question_2 = forms.ChoiceField(
        choices=SECURITY_QUESTIONS,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Security Question 2"
    )
    security_answer_2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Answer 2"
    )
    business = forms.BooleanField(
        required=False,
        label="I am a business account",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


    class Meta:
            model = CustomUser
            fields = (
                'username', 'password1', 'password2',
                'security_question_1', 'security_answer_1',
                'security_question_2', 'security_answer_2',
                'business'
            )


    def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            for fieldname in self.fields:
                self.fields[fieldname].help_text = None
                self.fields[fieldname].widget.attrs.update(
                    {'class': 'form-control'}
                )
                self.fields['business'].widget.attrs.update({'class': 'form-check-input'})


    def save(self, commit=True):
            user = super().save(commit=False)
            user.securityQ1 = self.cleaned_data.get('security_question_1')  # Use get() to prevent KeyError
            user.securityA1 = self.cleaned_data.get('security_answer_1')
            user.securityQ2 = self.cleaned_data.get('security_question_2')
            user.securityA2 = self.cleaned_data.get('security_answer_2')
            user.business = self.cleaned_data.get('business', False)


            if commit:
                user.save()

            return user

    
class ResetPasswordForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Username"
    )
    security_question_1 = forms.ChoiceField(
        choices=SECURITY_QUESTIONS,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Security Question 1"
    )
    security_answer_1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Answer 1"
    )
    security_question_2 = forms.ChoiceField(
        choices=SECURITY_QUESTIONS,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Security Question 2"
    )
    security_answer_2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Answer 2"
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password"
    )
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm New Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise forms.ValidationError("New passwords do not match.")
        return cleaned_data
    
class ChangeUsernameForm(forms.Form):
    new_username = forms.CharField(max_length=150, required=True)

    def clean_new_username(self):
        new_username = self.cleaned_data.get('new_username')

        # Check if the username already exists
        if CustomUser.objects.filter(username=new_username).exists():
            raise forms.ValidationError("This username is already taken.")
        return new_username
    
class CustomPasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old Password"
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password"
    )
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm New Password"
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user


    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not check_password(old_password, self.user.password):
            raise forms.ValidationError("Old password is incorrect.")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise forms.ValidationError("New passwords do not match.")

        return cleaned_data
    