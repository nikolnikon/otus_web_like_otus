# Like OTUS

Сайт курсов в IT Like OTUS

## Установка

С использованием git и установкой зависимостей из requirements.txt (для разработки):
```bash
1. Скачать исходный код веб-приложения
$ git clone https://github.com/nikolnikon/otus_web_like_otus.git

2. Установить необходимые зависимости
$ cd otus_web_like_otus
$ pip install -r requirements.txt

3. Создать базу данных
$ docker-compose up -d

4. Выполнить миграции
$ python manage.py migrate

5. Загрузить данные в БД
$ python manage.py loaddata users
$ python manage.py loaddata courses
```

## Запуск приложения
Данная иструкция распространяется на запуск приложения с помощью предоставляемого Django веб-сервера. Такой вариант не 
подходит для развертывания в "боевом" окружении. Подходы к развертыванию в "боевом" окружении описаны в документации.  
```bash
1. Создать в корневой директории (otus_web_like_otus) файл .env

2. Прописать в нем переменные окружения, соответствующие натсройкам веб-приложения. По умолчанию значения настроек 
берутся из файла settings.py

3. Выполнить команду
$ python manage.py runserver --settings=like_otus.settings --configuration=<configuration>
configuration - Dev или Prod (см. like_otus.settings)
```

## Лицензия
Проект распространяентся под лицензией MIT. Подробная информация в файле
[LICENSE](https://github.com/nikolnikon/otus_web_like_otus/blob/master/LICENSE)