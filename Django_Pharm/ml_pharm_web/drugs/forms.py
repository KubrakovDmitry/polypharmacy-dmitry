import os

from django import forms
from django.conf import settings

from .models import Drug, DrugGroup


class AddDrugGroupForm(forms.ModelForm):
    class Meta:
        model = DrugGroup
        fields = '__all__'


class AddDrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = '__all__'


class AddSideEffect(forms.Form):
    name = forms.CharField(label='Название побочного эффекта', widget=forms.TextInput(attrs={'class': 'form-input'}))


class updateSeideEffectRande(forms.Form):
    # DISPLAY_CHOICES = [ # Нужно получить список побочек
    #     ('1', 'Гипатит'),
    #     ('2', 'Почечная недостаточность'),
    # ]
    DISPLAY_CHOICES = []
    filename = 'side_effects.txt'
    path = os.path.join(settings.TXT_DB_PATH, filename)

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            if line == '\n':
                continue
            line = line.strip()
            print('line =', line)
            DISPLAY_CHOICES.append(
                (line.split('\t')[0],
                 line.split('\t')[1].replace(';', ''))
            )

    display_method = forms.ChoiceField(
        choices=DISPLAY_CHOICES,
        label="Выберете побочный эффект",
        widget=forms.Select
    )

    name = forms.CharField(label='Коэффициент появления', widget=forms.TextInput(attrs={'class': 'form-input'}))


class DisplaySideEffectsForm(forms.Form):

    DISPLAY_CHOICES = []
    DISPLAY_CHOICES.append(('all', 'Показать всё'))

    filename = 'drugs_xcn.txt'
    path = os.path.join(settings.TXT_DB_PATH, filename)

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            drug_name = line.split('\t')[1].replace(';', '')
            drug_id = line.split('\t')[0]
            DISPLAY_CHOICES.append(
                (drug_id,
                 drug_name))

    display_method = forms.ChoiceField(
        choices=DISPLAY_CHOICES,
        label="Выберете способ отображения побочек",
        widget=forms.Select
    )
