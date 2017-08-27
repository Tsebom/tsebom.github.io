import requests

TOKEN = 'YOUR TOKEN'


class YandexMetrika:

    def __init__(self, token):
        self.token = token

    def get_counters(self):
        url = 'https://api-metrika.yandex.ru/management/v1/counters'
        headers = {
            'Authorization': 'OAuth {}'.format(self.token),
        }

        response = requests.get(url, headers=headers)
        return response.json()


ym = YandexMetrika(TOKEN)
counters = ym.get_counters()
print(counters)
