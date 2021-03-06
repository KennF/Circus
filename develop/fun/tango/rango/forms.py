from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

    name = forms.CharField(max_length=128, help_text="Please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'url', 'views')
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    password = forms.CharField(widget=forms.PasswordInput())

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

