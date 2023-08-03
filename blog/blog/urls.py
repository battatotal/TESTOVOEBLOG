from django.contrib import admin
from django.urls import path, include

from blogapp.views import UsersApiList, PostsApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogapp.urls', namespace='blog')),
    path('api/list/', UsersApiList.as_view()),
    #для get запроса параметром идет id пользователя, для других запросов - id поста
    path('api/author_post_list/<int:pk>/', PostsApi.as_view()),



]
