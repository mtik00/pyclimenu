#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
climenu setup script
'''
from setuptools import setup


MAIN_NS = {}
VER_PATH = 'climenu.py'


if __name__ == '__main__':
    execfile(VER_PATH, MAIN_NS)
    DESC = open('README.rst').read()

    setup(
        name="climenu",
        py_modules=['climenu'],
        version=MAIN_NS['__version__'],
        description="Command-line menu system",
        url="https://github.com/mtik00/pyclimenu",
        download_url=(
            "https://github.com/mtik00/pyclimenu/releases/download/v{0}"
            "/climenu-{0}.tar.gz").format(MAIN_NS['__version__']),

        keywords='cli command-line menu',

        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
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
