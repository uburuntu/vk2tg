# _*_ coding: utf-8 _*_

import tokens

from vk2tg import Vk2Tg

'''
Duplicates all events in group to specified chat/channel in Telegram
'''

vk2tg = Vk2Tg(tg_token=tokens.tg_token, vk_token=tokens.vk_token)
chat_id = tokens.test_chat_id


def listener(event):
    vk2tg.send_tg_message(chat_id, event)


if __name__ == '__main__':
    vk2tg.set_event_listener(listener)
    vk2tg.vk_polling()
