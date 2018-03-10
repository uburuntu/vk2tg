# _*_ coding: utf-8 _*_

import os

# Set your api tokens and keys through environmental variables
# (add lines to your .bashrc and restart terminal):
# export VK2TG_TELEGRAM_BOT_TOKEN="XXXXX:XXXXXXXXXXX"
# export VK2TG_VK_API_TOKEN="XXXXXXXXXXX"
#
# OR
#
# Manually through defaults in this file
# Important: untrack file to prevent accidential private token pushing:
# 'git update-index --assume-unchanged tokens.py'

default_tg_token = ""
tg_token = os.getenv('VK2TG_TELEGRAM_BOT_TOKEN', default_tg_token)

default_vk_token = ""
vk_token = os.getenv('VK2TG_VK_API_TOKEN', default_vk_token)
