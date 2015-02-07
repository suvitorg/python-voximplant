# -*- coding: utf-8 -
#
# This file is part of python-voximplant released under the MIT license. 
# See the LICENSE for more information.

import os
from setuptools import setup, find_packages

setup(
    name='python-voximplant',
    version=__import__('voximplant').VERSION,
    description='python api client for voximplant.com',
    long_description=file(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    author='SUVIT LLC',
    author_email='mail@suvit.ru',
    license='MIT',
    url='http://github.com/suvitorg/python-voximplant',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=['requests'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Web Environment',
        'Topic :: Software Development',
    ]
)
