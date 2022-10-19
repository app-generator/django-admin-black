import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
name='django-admin-black',
version='1.0.0',
zip_safe=False,
packages=find_packages(),
include_package_data=True,
description='Modern template for Django admin interface',
long_description=README,
long_description_content_type="text/markdown",
url='https://github.com/app-generator/django-admin-black',
author='AppSeed.us',
author_email='support@appseed.us',
license='MIT License',
classifiers=[
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Environment :: Web Environment',
    'Topic :: Software Development',
    'Topic :: Software Development :: User Interfaces',
    ],
)
