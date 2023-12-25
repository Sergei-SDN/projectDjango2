from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser

        # fields = ('name', 'description', 'image', 'category', 'price',)
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'avatar', 'country']
        # fields = '__all__'
        # exclude = ['price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control'


class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser

        # fields = ('name', 'description', 'image', 'category', 'price',)
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'avatar', 'country']
        # fields = '__all__'
        # exclude = ['price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['password'].widget = forms.HiddenInput()
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control'
