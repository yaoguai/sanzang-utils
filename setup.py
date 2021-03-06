#!/usr/bin/env python3

""" Sanzang Utils setup script for packaging and installation. """

from distutils.core import setup

with open('README.rst', 'r', encoding='utf-8') as fin:
    LONG_DESCRIPTION = fin.read()

setup(
    #
    # Basic information
    #
    name='sanzang-utils',
    version='1.3.3',
    author='yaoguai',
    author_email='lapislazulitexts@gmail.com',
    url='https://github.com/yaoguai/sanzang-utils',
    license='MIT',
    #
    # Descriptions & classifiers
    #
    description='Machine Translation from Chinese, Japanese, or Korean.',
    long_description=LONG_DESCRIPTION,
    keywords='chinese japanese korean cjk asia language machine translation',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Religion',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities'],
    #
    # Included Python files
    #
    scripts=[
        'szu-ed',
        'szu-r',
        'szu-ss',
        'szu-t'],
    py_modules=[
        'szu_ed',
        'szu_r',
        'szu_ss',
        'szu_t'],
    data_files=[
        ('share/doc/sanzang-utils', [
            'AUTHORS.rst',
            'LICENSE.rst',
            'NEWS.rst',
            'README.rst',
            'TUTORIAL.html']),
        ('share/man/man1', [
            'szu-ed.1',
            'szu-r.1',
            'szu-ss.1',
            'szu-t.1'])]
)
