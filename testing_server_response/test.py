from requests import get

# Получение всех работ
print(get('http://localhost:5000/api/news').json())
# Корректное получение одной работы
print(get('http://localhost:5000/api/news/1').json())
# Ошибочный запрос на получение одной работы — неверный id
print(get('http://localhost:5000/api/news/999').json())
# Ошибочный запрос на получение одной работы — строка
print(get('http://localhost:5000/api/news/ok').json())
