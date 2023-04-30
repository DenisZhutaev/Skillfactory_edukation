# Работа с API питомника через модуль requests

# Импортируем модуль requests для работы с API

import requests

# Запрос всех доступных питомцев
status = 'available'
res_get = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})
print(f'Статус кода: {res_get.status_code}\n')
print(res_get.text, '\n\n', '-' * 100)


# Создание нового питомца
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {"id": 9223372036854775807, "category": {"id": 0, "name": "string"},
        "name": "BOB", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
        "status": "available"}
res_post = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=data)
print(f'Статус кода: {res_post.status_code}\n')
print(res_post.json(), '\n\n', '-' * 100)


# Изменение данных о питомце
headers_put = {'accept': 'application/json', 'Content-Type': 'application/json'}
data_put = {"id": 9223372036854775807, "category": {"id": 0, "name": "string"}, "name": "PIIIING",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}], "status": "available"}
res_put = requests.put('https://petstore.swagger.io/v2/pet', headers=headers_put, json=data_put)
print(f'Статус кода: {res_put.status_code}\n')
print(res_put.json(), '\n\n', '-' * 100)


# Удаление созданного питомца
res_delete = requests.delete(f'https://petstore.swagger.io/v2/pet/{9223372036854775807}', headers={'accept': 'application/json'})
print(f'Статус кода: {res_delete.status_code}\n')
print(res_delete.json())