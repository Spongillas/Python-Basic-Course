"""
Это пример в две строчки работы с модулем requests
для получения ответов от API. Для работы с модулем 
нужно его вначале установить  через pip install.

запрос к API производится через метод get(), полученный
результат можно увидеть, например, через метод json().

В этом примере идет запрос к бесплатному API, которое
выдает случайные интересные факты о кошках. Вы можете обращаться
к любому источнику и обрабатывать полученные результаты так,
как нужно вам.

Ну естественно, потом придется озаботиться обработкой исключений,
написать обработку полученного ответа и передать этот ответ
куда-то дальше, но суть в целом, надеюсь, понятна
"""

import requests

response = requests.get("https://catfact.ninja/fact")
print(response.json()['fact'])