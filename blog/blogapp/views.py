from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.urls import reverse

from .models import Post
from django.contrib.auth.models import User

from .serializers import UserListSerializer, PostListSerializer
from .forms import *

#Обработчик главной страницы
def user_list(request):
    users = User.objects.all()
    if request.method == "POST":
        addform = AddPostForm(request.POST)
        if addform.is_valid():
            # Автоматическое заполнение поля User текущим пользователем
            response = addform.save(commit=False)
            response.user = request.user
            response.save()

            return redirect(".")

    else:
        addform = AddPostForm()
    return render(request, 'blogapp/user/list.html', {'users':users, 'addform':addform,})


#Обработчик главной страницы с постами конкретного пользователя
def user_selected(request, **kwargs):
    users = User.objects.all()
    addform = AddPostForm()
    user_selected = kwargs['id']

    return render(request, 'blogapp/user/list.html', {'users': users, "user_selected":user_selected, 'addform':addform})

#Удаление поста
def post_delete(request, **kwargs):
    post = Post.objects.get(title=kwargs['slug'])
    post.delete()
    return redirect(reverse('blogapp:user_list'))


#Регистрация пользователя
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "blogapp/user/register.html"
    #success_url = reverse('login')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #При успешной регистрации сразу авторизую пользователя
        user = form.save()
        login(self.request, user)
        return redirect("blogapp:user_list")

#Авторизаия пользователя
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "blogapp/user/login.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('blogapp:user_list')

#Выход пользователя
def loguot_user(request):
    logout(request)
    return redirect('blogapp:login')




#Ниже представлены Обработчики API


#Список пользователей
class UsersApiList(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserListSerializer
    #permission_classes = (permissions.IsAuthenticated,)


#Работа с Постами(Получение, Добавление, Удаление)
class PostsApi(generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer


    def get(self, request, *args, **kwargs):
        queryset = Post.objects.filter(user=kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Содержимое методов скопировал из соответствующих методов дженериков(вместе с вспомогательными методами,
    # чтобы не нарушить консистентность, на всякий случай)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


    #ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ
    def perform_destroy(self, instance):
        instance.delete()



    def perform_create(self, serializer):
        serializer.save()


    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


