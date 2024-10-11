from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Username alanının widget'ını özelleştir
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        
        
    def confirm_login_allowed(self, user):
        # Kullanıcı devre dışı bırakılmışsa hata fırlat
        if not user.is_active:
            raise forms.ValidationError("This account is inactive")