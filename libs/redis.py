from redis import StrictRedis

from libs.env import get_env
from libs.telebot import telebot

from utils.to_dict import to_dict


class Redis:
    __MY_CHANNEL = 'mychannel'
    __FIXED_PRICE_DIFFERENCE = 'fixed_price_difference'

    def __init__(self):
        self._redis = StrictRedis(**(get_env.get(('redis'))))

    def publish(self, message: str) -> None:
        context = {
            "channel": self.__MY_CHANNEL,
            "message": message
        }

        self._redis.publish(**context)


    def listen(self) -> str:

        sub = self._redis.pubsub()
        sub.subscribe(self.__MY_CHANNEL)

        for message in sub.listen():
            if message is not None and isinstance(message, dict):
                notify = to_dict(message.get('data'))
                if notify:
                    if notify.get('message_type') == self.__FIXED_PRICE_DIFFERENCE:
                        telebot.send_message(notify.get('message'))


redis = Redis()
