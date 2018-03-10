# _*_ coding: utf-8 _*_

import logging

from telebot import TeleBot
from vk_api import VkApi, longpoll as vk_longpoll

__version__ = '0.1.1'

log_format = '%(asctime)s [%(filename)s:%(lineno)d] [%(levelname)s] %(name)s: "%(message)s"'
logging.basicConfig(format=log_format, level=logging.WARNING)
logger = logging.getLogger('Vk2Tg')


class Vk2Tg:
    def __init__(self, tg_token=None, vk_token=None):
        # Init Telegram API
        self.tg = TeleBot(tg_token)

        # Init vk API
        self.vk_session = VkApi(token=vk_token)
        self.vk = self.vk_session.get_api()
        self.longpoll = vk_longpoll.VkLongPoll(self.vk_session)

        # Init listeners
        self.event_listeners = []

    def set_event_listener(self, listener):
        self.event_listeners.append(listener)

    def vk_listen(self):
        return self.longpoll.listen()

    def vk_polling(self):
        logger.info('Started vk_polling')

        while True:
            for event in self.vk_listen():
                for listener in self.event_listeners:
                    listener(event)

    # todo: move to utils
    @staticmethod
    def event_to_dict(event):
        res = dict()
        for attr in vk_longpoll.EVENT_ATTRS_MAPPING[event.type]:
            res[attr] = event.__getattribute__(attr)
        return res

    def send_tg_message(self, chat_id, event=None):
        if event is not None:
            text = '[{}] {}'.format(event.type, self.event_to_dict(event))
            self.tg.send_message(chat_id, text)
