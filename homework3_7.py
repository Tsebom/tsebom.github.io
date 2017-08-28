from urllib.parse import urljoin

import requests


TOKEN = 'AQAAAAAB1WWPAASB2PIssCHDckEMl7AhtCft0eM'


class YMBase:
    MANAGMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token),
            'User-Agent': 'netology6 test app',
            'Content - Type': 'application / x - yametrika + json'
        }


class YandexMetrika(YMBase):

    def get_counters(self):
        url = urljoin(self.MANAGMENT_URL, 'counters')
        headers = self.get_headers()

        response = requests.get(url, headers=headers)
        return [Counter(
            self.token,
            counter_id['id'])for counter_id in response.json()['counters']
        ]


class Counter(YMBase):
    def __init__(self, token, counter_id):
        super().__init__(token)
        self.counter_id = counter_id

    def get_info(self):
        url = urljoin(self.MANAGMENT_URL, 'counter/{}'.format(self.counter_id))
        headers = self.get_headers()

        response = requests.get(url, headers=headers)
        return response.json()

    def get_visits(self):
        headers = self.get_headers()
        params = {
            'id': self.counter_id,
            'metrics': str('ym:s:visits, ym:s:pageviews, ym:s:users,'
                           'ym:s:manPercentage, ym:s:womanPercentage,'
                           'ym:s:upTo34AgePercentage')
        }

        response = requests.get(self.STAT_URL, params,  headers=headers)
        return response.json()['totals']


def main():
    ym = YandexMetrika(TOKEN)
    counters = ym.get_counters()

    for counter in counters:
        result = counter.get_visits()

        print('Визитов: {}'.format(result[0]))
        print('Просмотров: {}'.format(result[1]))
        print('Посетителей: {}'.format(result[2]))
        print('Мужчин: {}%'.format(result[3]))
        print('Женщин: {}%'.format(result[4]))
        print('Возраст 25‑34 лет лет: {}%'.format(result[5]))


main()
