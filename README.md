## API для сервиса YATUBE
Yatube - проект социальной сети. Позволяет публиковать посты, комментировать посты, осуществлять подписку на авторов.
### Технологии:
1. Python 3.9
2. Django
3. DRF
4. JWT + Djoser
### Автор проекта:
[Анна Аржакова](https://github.com/arzhakova)
### Как запустить проект:
1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:arzhakova/api_final_yatube.git
```

```
cd api_final_yatube
```

2. Создать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Выполнить миграции:

```
python3 manage.py migrate
```

5. Запустить проект:

```
python3 manage.py runserver
```

#### После запуска проекта, документация будет доступна по адресу:
http://127.0.0.1:8000/redoc/
