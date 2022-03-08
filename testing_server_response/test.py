from requests import get

# Получение всех работ
print(get('http://localhost:5000/api/jobs').json())
# Корректное получение одной работы
print(get('http://localhost:5000/api/jobs/1').json())
# Ошибочный запрос на получение одной работы — неверный id
print(get('http://localhost:5000/api/jobs/999').json())
# Ошибочный запрос на получение одной работы — строка
print(get('http://localhost:5000/api/jobs/ok').json())
