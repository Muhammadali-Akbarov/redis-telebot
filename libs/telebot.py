import requests

from libs.env import get_env

class TeleBotClient:
    __sendMessage = "/sendMessage"

    def __init__(self, api_host: str, api_token: str, chat_id: str) -> None:
        self.__chat_id = chat_id
        self.__main_url = f'{api_host}{api_token}'

    def send_message(self, text: str) -> dict:
        params = {
            'text': text,
            'chat_id': self.__chat_id,
            'parse_mode': 'HTML'
        }
        resp = requests.post(f'{self.__main_url}{self.__sendMessage}', params)

        return resp


telebot = TeleBotClient(
    **(get_env.get('bot'))
)