import redis
import json

red = redis.Redis(
    host='redis-12084.c1.asia-northeast1-1.gce.cloud.redislabs.com',
    port=12084,
    password='RSRY4TGTHYgqwiR65JiIIZLvCjes1WoK')

dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1'))  # с помощью знакомой нам функции превращаем данные полученные из кэша обратно в словарь
print(type(converted_dict))  # убеждаемся, что получили действительно словарь
print(converted_dict)

red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))
