#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
climenu setup script
'''
# import os
from setuptools import setup


MAIN_NS = {}
VER_PATH = 'climenu.py'  # os.path.join('climenu', 'version.py')


if __name__ == '__main__':
    execfile(VER_PATH, MAIN_NS)
    # with open(VER_PATH) as ver_file:
    #     exec(ver_file.read(), MAIN_NS)  # pylint: disable=W0122

    DESC = open('README.rst').read()

    setup(
        name="climenu",
        version=MAIN_NS['__version__'],
        description="Command-line menu system",
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
        # packages=find_packages(),
        # package_data={"climenu": ['.*']},
        zip_safe=True,
        include_package_data=True,
        long_description=DESC
    )
