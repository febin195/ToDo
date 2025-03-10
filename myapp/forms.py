from django import forms

from myapp.models import TaskModel

class Userform(forms.Form):

    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter user name'}))

    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your firstname'}))

    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your lastname'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter your password"}))

    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}))

class Loginform(forms.Form):    

    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))

    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))

class Taskform(forms.ModelForm):

    class Meta:

        model=TaskModel

        fields=["task_name"]



     



