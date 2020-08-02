from django import forms
from .models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
                class Meta:
                                model = UserRegistration
                                fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class ViewDatadbForm(forms.Form):
                select_choices =(('TCS','TCS'),
                   ('INFOSYS','INFOSYS'),
                   ('AMAZON','AMAZON'),
                   ('FLIPKART','FLIPKART'),
                   )
                companyname = forms.ChoiceField(choices = select_choices)
                '''select_choices1 =(('1Year','1Year'),
                                  ('2Year','2Year'),
                                  )
                companysales = forms.ChoiceField(choices = select_choices1)'''




