from django import forms
from django.contrib.auth.models import User
from .models import Event,Calendar
from django.core.exceptions import ValidationError


# Kullanıcı Kayıt Formu
class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, label="Şifre")
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label="Şifre Tekrarı")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 'username' alanındaki açıklamaları kaldırıyoruz
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None

    # Şifrelerin birbirine eşit olup olmadığını kontrol etme
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Şifreler birbirine eşleşmiyor.")
        return password2

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_date', 'end_date', 'start_date_bahar', 'end_date_bahar', 'calendar']

    # Tarih alanlarını opsiyonel yapıyoruz
    start_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2020, 2031)),
        required=False,  # Bu alan artık opsiyonel
        label="Güz Yarıyılı Başlangıç Tarihi"
    )
    end_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2020, 2031)),
        required=False,  # Bu alan artık opsiyonel
        label="Güz Yarıyılı Bitiş Tarihi"
    )
    start_date_bahar = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2020, 2031)),
        required=False,  # Bu alan artık opsiyonel
        label="Bahar Yarıyılı Başlangıç Tarihi"
    )
    end_date_bahar = forms.DateField(
        widget=forms.SelectDateWidget(years=range(2020, 2031)),
        required=False,  # Bu alan artık opsiyonel
        label="Bahar Yarıyılı Bitiş Tarihi"
    )

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['name']