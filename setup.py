# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name='santander-cobranca-xml',
    version='1.0.1',
    author='Marcelo Salhab Brogliato',
    author_email='msbrogli@gmail.com',
    url='https://github.com/msbrogli/santander-cobranca-xml',
    packages=find_packages(),
    package_data={
        '': ['LICENSE'],
        'santander_cobranca_xml': ['templates/*.xml', 'santander.py'],
    },
    zip_safe=False,
    provides=[
        'santander_cobranca_xml'
    ],
    license='MIT',
    description='Consumes the API given by Santander in order to register a *boleto bancário*.',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
)
