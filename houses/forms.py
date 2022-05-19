from django import forms

class HouseFilterForms(forms.Form):
    min_price = forms.IntegerField(label='от', required=False)
    max_price = forms.IntegerField(label='до', required=False)
    query = forms.CharField(label='описание', required=False)
    ordering = forms.ChoiceField(label='сортировка', required=False, choices=[
        ('name', 'по алфавиту'),
        ('price', 'по возрастанию цены'),
        ('-price', 'по убыванию цены')
    ])
