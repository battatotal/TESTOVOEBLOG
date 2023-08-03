from django.contrib import admin
from django.urls import path, include

from blogapp.views import UsersApiList, PostsApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogapp.urls', namespace='blog')),
    path('api/list/', UsersApiList.as_view()),
    #ниже адрес для двух типов запросов(для get запроса параметром идет id пользователя, для delete - id поста)
    path('api/author_post_list/<int:pk>/', PostsApi.as_view()),

    #post
    path('api/author_post_list/', PostsApi.as_view()),



]
