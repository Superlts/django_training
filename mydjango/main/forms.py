from django import forms

class BookForm(forms.Form):
    name = forms.CharField(label='Наименование', max_length=255)
    price = forms.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    pages_number = forms.IntegerField(label='Страницы')
    description = forms.CharField(label="Описание", widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class ReviewForm(forms.Form):
    text = forms.CharField(label="Описание", widget=forms.Textarea)


class EditBookDescriptionForm(forms.Form):
   description = forms.CharField(label="Description", widget=forms.Textarea)