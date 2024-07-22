## Запуск BackEnd

Все консольные команды выполнять в папке BackEnd
Проверить есть ли все зависимости, если нет, то написать 
```cmd
poetry install
```

Скачать и установить postgresql и pgAdmin, там создать сервер

Создать файл .env в самой верхней папке
Записать туда переменные из postgres
```env
DB_HOST=  
DB_PORT=  
DB_NAME=  
DB_USER=  
DB_PASS=
```

прописать в консоль 

```cmd
alembic revision --autogenerate -m "migration_name"

alembic upgrade head
```

Запуск
```cmd
uvicorn main:app --reload
```

И далее переходим по ссылке
http://127.0.0.1:8000/docs
