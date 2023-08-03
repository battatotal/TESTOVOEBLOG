from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blogapp.models import Post

#Форма добавления поста
class AddPostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['title', 'body', ]
        widgets = {'body': forms.Textarea(attrs={'cols':100, 'rows':10})}#'user': forms.HiddenInput()}



#Форма удаления поста
class DelPostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['user','title',]
        widgets = {'body': forms.Textarea(attrs={'cols':100, 'rows':10})}


#Форма регистрации пользователя
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class":"forma"}))
    password1 = forms.CharField(label="Пароль", widget=forms.TextInput(attrs={"class": "forma"}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.TextInput(attrs={"class": "forma"}))


    class Meta:
        model = User
        fields = ("username","password1","password2")