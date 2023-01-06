# api_final
api final

Разворачиваем проект:

Клонировать репозиторий и перейти в него в командной строке:

<code>git clone https://github.com/kultmet/api_final_yatube.git</code><br>

<code>cd <ваша_папка></code><br>

Cоздать и активировать виртуальное окружение:<br>

<code>python3 -m venv env</code><br>

<code>source env/bin/activate</code><br>

Установить зависимости из файла requirements.txt:<br>

<code>python3 -m pip install --upgrade pip</code><br>

<code>pip install -r requirements.txt</code><br>

Выполнить миграции:<br>

<code>python3 manage.py migrate</code><br>

Запустить проект:<br>

<code>python3 manage.py runserver</code>

<h1>Описание</h1>
Здесь вы можете совершать определенные действия с обьектами:<br>

| Endpoint | Object | Methods | Description |
| --- | --- | --- | --- |
| /api/v1/posts/ | Post | GET, POST | Получаем список постов и создаем пост. |
| /api/v1/posts/{id}/ | Post | GET, PUT, PATCH, DELETE | Получаем, редактируем, заменяем, отдельный пост. |
| /api/v1/posts/{post_id}/comments/ | Comment | GET, POST | Получаем список комментариев и создаем комментарий к конкретному посту |
| /api/v1/posts/{post_id}/comments/{id}/ | Comment | GET, PUT, PATCH, DELETE | Получаем, редактируем, заменяем, отдельный комментарий и конкретному посту. |
| /api/v1/groups/ | Group | GET | Получаем список групп. Только чтоние |
| /api/v1/groups/{id}/ | Group | GET | Получаем конкретную группу. Только чтоние |
| /api/v1/follow/ | Follow | GET, POST | Получаем все подписки пользователя сделавшего GET запрос. Подписываемся на другого пользователя. Подписыватся на себя безсмысленно |
| /api/v1/jwt/create/ | Token | POST | Получаем токен |
| /api/v1/jwt/refresh/ | Token | POST | Обновляем токен |
| /api/v1/jwt/verify/ | Token | POST | Проверяем токен |
<h2>Примеры ответа</h2><br?
*Используется гибкая пагинация*<br>
 GET запрос<br>
 /api/v1/posts/
<pre><code>
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
</code></pre>

POST запрос<br>
/api/v1/posts/
<pre><code>
{
  "text": "string",
  "image": "string",
  "group": 0
}
</code></pre>
Пример ответа.
<pre><code>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2022-09-21T19:57:45.329Z",
  "image": "string",
  "group": 0
}
</code></pre>
_Остальные примеры запросов и ответов можно посмотреть в файле \api_final_yatube\yatube_api\static\redoc.yaml_ <br>
**Спасибо что пользуетесь нашими сервисами!**
>>>>>>> 8b664a98c17470cdc8217363e17a48deddb29612

Установить зависимости из файла requirements.txt:<br>

<code>python3 -m pip install --upgrade pip</code><br>

<code>pip install -r requirements.txt</code><br>

Выполнить миграции:<br>

<code>python3 manage.py migrate</code><br>

Запустить проект:<br>

<code>python3 manage.py runserver</code>

<h1>Описание</h1>
Здесь вы можете совершать определенные действия с обьектами:<br>

| Endpoint | Object | Methods | Description |
| --- | --- | --- | --- |
| /api/v1/posts/ | Post | GET, POST | Получаем список постов и создаем пост. |
| /api/v1/posts/{id}/ | Post | GET, PUT, PATCH, DELETE | Получаем, редактируем, заменяем, отдельный пост. |
| /api/v1/posts/{post_id}/comments/ | Comment | GET, POST | Получаем список комментариев и создаем комментарий к конкретному посту |
| /api/v1/posts/{post_id}/comments/{id}/ | Comment | GET, PUT, PATCH, DELETE | Получаем, редактируем, заменяем, отдельный комментарий и конкретному посту. |
| /api/v1/groups/ | Group | GET | Получаем список групп. Только чтоние |
| /api/v1/groups/{id}/ | Group | GET | Получаем конкретную группу. Только чтоние |
| /api/v1/follow/ | Follow | GET, POST | Получаем все подписки пользователя сделавшего GET запрос. Подписываемся на другого пользователя. Подписыватся на себя безсмысленно |
| /api/v1/jwt/create/ | Token | POST | Получаем токен |
| /api/v1/jwt/refresh/ | Token | POST | Обновляем токен |
| /api/v1/jwt/verify/ | Token | POST | Проверяем токен |
<h2>Примеры ответа</h2><br?
*Используется гибкая пагинация*<br>
 GET запрос<br>
 /api/v1/posts/
<pre><code>
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
</code></pre>

POST запрос<br>
/api/v1/posts/
<pre><code>
{
  "text": "string",
  "image": "string",
  "group": 0
}
</code></pre>
Пример ответа.
<pre><code>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2022-09-21T19:57:45.329Z",
  "image": "string",
  "group": 0
}
</code></pre>
_Остальные примеры запросов и ответов можно посмотреть в файле \api_final_yatube\yatube_api\static\redoc.yaml_ <br>
**Спасибо что пользуетесь нашими сервисами!**
