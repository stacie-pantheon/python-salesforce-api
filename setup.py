#!/usr/bin/env python
from setuptools import setup


if __name__ == '__main__':
    setup(
        name="salesforce-api",
        version="0.1.11",
        author="Felix Lindstrom",
        author_email='felix.lindstrom@gmail.com',
        description="Salesforce API wrapper",
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        keywords=['salesforce', 'salesforce api', 'salesforce bulk api'],
        license='MIT',
        packages=['salesforce_api'],
        install_requires=[],
        zip_safe=True,
        url='https://github.com/felixlindstrom/python-salesforce-api',
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )