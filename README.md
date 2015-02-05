python-pechkin
==============

Интеграция http://voximplant.com/ и вашего приложения

pechkin API: http://voximplant.com/docs/references/httpapi/

Пример кода

    from voximplant.api import API

    api = API('my_username', 'my_password')

    user_id = api.user_add('new_user', 'Новый пользователь', 'new_password')
