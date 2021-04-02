# dataforseoapi


Пользователь:
- выбирает поисковую систему
- выбирает регион поиска (Можете сделать регионы Соединенных Штатов Америки или на ваше усмотрение, не принципиально)
- вводит ключевое слово
- отправляет запрос

Отображается статус поставленных задач и результатов по ним.



#### Как запустить

Installation:

1 Клонируйте репозиторий
```java
git clone https://github.com/bodyahavryshchuk/dataforseoapi

```
2 В директории backend в файле .env.dev присвоить значение переменным
```java
SERP_LOGIN=YOUR_SERP_LOGIN
SERP_PASSWORD=YOUR_SERP_PASSWORD
```

3 Войдите в проект
```java
cd dataforseoapi
```

4 Поднимите проект
```java
docker-compose up --build
```

5 Откройте в браузере страницу
```java
http://localhost:8080
```