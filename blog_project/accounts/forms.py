from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Username alanının widget'ını özelleştir
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder' : 'Enter Username'}
                                                         )
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control',
                                                                    'placeholder' : 'Enter Password'}
                                                             )
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
        
    def confirm_login_allowed(self, user):
        # Kullanıcı devre dışı bırakılmışsa hata fırlat
        if not user.is_active:
            raise forms.ValidationError("This account is inactive")
        
    
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['password2'].widget = forms.widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['username'].widget = forms.widgets.TextInput(attrs={'class':'form-control'})
        self.fields['email'].widget = forms.widgets.EmailInput(attrs={'class':'form-control'})
        self.fields['email'].required = True
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email = email).exists():
            self.add_error("email", "this email is already exist")
            raise ValidationError("tis email is already in use")
            
        return email