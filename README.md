# TESTOVOEBLOG

superuser = (admin: 12345)
не забыть префикс /blog при запуске

Работа с API:
'api/list/' - список пользователей;

'api/author_post_list/<int:pk>/' - для GET запроса параметром является id пользователя(результат: список постов указанного автора);

'api/author_post_list/ - для POST запроса (результат: добавление указанного поста). Нужно использовать Postman или подобное. Для теста можно отправить json объект типа:
    {
        "id": 1,
        "title": "sometitle",
        "body": "sometext",
        "user": 2
    }



'api/author_post_list/<int:pk>/' - для DELETE запроса параметром является id поста(результат: удаление указанного поста). Нужно использовать Postman или подобн.
