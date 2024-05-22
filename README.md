# Скрипт для создания видео бегущей строки (100 на 100, длина 3 секунды)

Клонируйте репозиторий

```
git clone 'репозиторий'
```

Создайте и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполните миграции:
```
python3 manage.py migrate
```

Запустите проект:

```
python3 manage.py runserver
```
