# API backend

Чтобы обратиться к методу API, Вам необходимо выполнить `GET` и `POST` запрос такого вида: ``example.com/tasks`` 

В ответ на такой запрос Вы получите ответ в формате **JSON:** 
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "",
      "description": "",
      "body": "",
      "done": false,
      "data": "09.06.2019",
      "img": [
        "urls",
	"..."
      ],
      "tag": [
        "city",
        "life"
      ]
    }
  ]
}
```
В ответе будут содержаться все статьи на сайте.

Можно обратиться по id конкретной статье: ``example.com/tasks`` 

Запрос ``example.com/tasks/tag`` ответит списком всех тегов на ресурсе.
```json
{
  "tags": [
    "city",
    "life",
    "today"
  ]
}
```

Запрос ``example.com/tasks/tag/city`` выдаст все статьи с этим тагам. 

На неправльно составленный запрос сервер отвит ошибкой:
```json
{
  "error": "Not found"
}
```
