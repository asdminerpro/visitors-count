# visitors-count

Счётчик посещений

```(env)$ python app.py``` 

* Тестовые страницы: /test_page1 и /test_page2
* Проверка количества посещений: /get_count?id=<page_id> - получить число посещений страницы по её идентификатору

<img src="/update_count?id={{ id }}" style="width: 1px; height: 1px" alt="counter">

----

* Считаются только уникальные посещения пользователями страницы. 
* Данные о посещаемости не сохраняются в базу данных.
* Тесты есть только на временный класс PageStatistics
* Есть частичная декомпозиция.



Юрченко Степан ФТ-201
