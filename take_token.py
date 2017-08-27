from urllib.parse import urlencode

AUTHORIZE_API = 'https://oauth.yandex.ru/authorize'

APP_ID = '448112b027ca4940ba43aab51b97d7cb'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

print('?'.join((AUTHORIZE_API, urlencode(auth_data))))