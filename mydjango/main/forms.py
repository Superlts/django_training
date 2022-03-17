from django import forms

class BookForm(forms.Form):
    name = forms.CharField(label='Наименование', max_length=255)
    price = forms.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    pages_number = forms.IntegerField(label='Страницы')
    description = forms.CharField(label="Описание", widget=forms.Textarea)
