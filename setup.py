#!/usr/bin/env python3

from setuptools import setup


setup(name='table_explorer',
      version='0.1',
      description='HTML tables parsing made easy.',
      url='http://github.com/vmarquet/python-table-explorer',
      author='Vincent Marquet',
      author_email='vincent.marquet1@free.fr',
      license='MIT',
      packages=['table_explorer'],
      install_requires=['beautifulsoup4'],
      include_package_data=True,
      platforms='any',
      classifiers = [
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      zip_safe=False)
