from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', initial='undefined', help_text='Введите свое имя')
    age = forms.IntegerField(label='Ваш возраст?', initial=18, help_text='Введите свой возраст')
    reklama = forms.BooleanField(label='Coглacны получать рекламу?', required=False)