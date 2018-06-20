import setuptools

import vk2tg


def read(filename):
    with open(filename) as file:
        return file.read()


setuptools.setup(
        name='vk2tg',
        version=vk2tg.__version__,
        author='uburuntu',
        author_email='bekbulatov.ramzan@ya.ru',
        url='https://github.com/uburuntu/vk2tg',
        description='Integration vk with Telegram',
        long_description=read('readme.md'),
        long_description_content_type="text/markdown",
        download_url='https://github.com/uburuntu/vk2tg/archive/master.zip',
        license='GNU General Public License v3.0, see LICENSE file',
        packages=['vk2tg'],
        install_requires=['vk_api', 'pyTelegramBotAPI'],
        classifiers=(
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3',
        )
)
