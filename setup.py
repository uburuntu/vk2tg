# -*- coding: utf-8 -*-

import pypandoc
from setuptools import setup

import vk2tg

setup(
    name='vk2tg',
    version=vk2tg.__version__,
    author='uburuntu',
    author_email='bekbulatov.ramzan@ya.ru',
    url='https://github.com/uburuntu/vk2tg',
    description='Integration vk with Telegram',
    long_description=pypandoc.convert_file('readme.md', 'rst', format='markdown_github'),
    download_url='https://github.com/uburuntu/vk2tg/archive/master.zip',
    license='GNU General Public License v3.0, see LICENSE file',

    packages=['vk2tg'],
    install_requires=['vk_api', 'pyTelegramBotAPI']
)
