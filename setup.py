#!/usr/bin/env python
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='ConfMerge',
    version='0.1.0',
    author='Andre Lehmann',
    author_email='aisberg@posteo.de',
    url='https://github.com/Aisbergg/python-confmerge',
    license='LGPL',
    description='Configuration file merge utility',
    long_description=long_description,
    keywords=['config', 'ini', 'yamel', 'json', 'command-line', 'CLI'],
    package_dir={ '': 'src' },
    packages=find_packages('src'),
    scripts=[],
    entry_points={
        'console_scripts': [
            'confmerge = confmerge:cli',
        ]
    },
    install_requires=[
        'pyyaml >= 3.10',
    ],
    include_package_data=True,
    zip_safe=True,
    platforms=['POSIX'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: LGPL License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
)
