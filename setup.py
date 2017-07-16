#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
climenu setup script
'''
import re
from setuptools import setup


MAIN_NS = {}
VER_PATH = 'climenu.py'


def get_version():
    '''get's the current version from the source file'''
    re_ver = re.compile(
        r'^__version__\s*=\s+[\'"](?P<version>.*?)[\'"]', re.MULTILINE)
    text = open(VER_PATH).read()
    return re_ver.search(text).group('version')


if __name__ == '__main__':
    DESC = open('README.rst').read()
    VERSION = get_version()

    setup(
        name="climenu",
        py_modules=['climenu'],
        version=VERSION,
        description="Command-line menu system",
        url="https://github.com/mtik00/pyclimenu",
        download_url=(
            "https://github.com/mtik00/pyclimenu/releases/download/v{0}"
            "/climenu-{0}.tar.gz").format(VERSION),

        keywords='cli command-line menu',

        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Development Status :: 5 - Production/Stable'
        ],

        author="Timothy McFadden",
        author_email="tim@timandjamie.com",
        license='MIT',
        install_requires=[],
        zip_safe=True,
        include_package_data=True,
        long_description=DESC
    )
