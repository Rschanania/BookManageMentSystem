from django import forms
class NewBookForm(forms.Form):
    title=forms.CharField(label="Title",max_length=100)
    price=forms.FloatField(label="Price")
    author=forms.CharField(label="Author",max_length=200)
    publisher=forms.CharField(label='Publiser',max_length=200)

class SearchForm(forms.Form):
    title=forms.CharField(label="Title")