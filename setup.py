# -*- coding: utf-8 -*-

from os.path import join, dirname

from setuptools import setup, find_packages

setup(
    name='vk2tg',
    version='0.1',
    author='uburuntu',
    author_email='bekbulatov.ramzan@ya.ru',
    url='https://github.com/uburuntu/vk2tg',
    description='Integration vk with Telegram',
    long_description=open(join(dirname(__file__), 'readme.rst')).read(),
    download_url='https://github.com/uburuntu/vk2tg/archive/master.zip',
    license='GNU General Public License v3.0, see LICENSE file',

    packages=find_packages(),
    install_requires=['requests', 'vk_api', 'pyTelegramBotAPI']
)
