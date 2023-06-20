import os

from setuptools import setup, find_packages

VERSION_NUMBER = '0.6.2'


def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mkdocs-obsidian-support-plugin',
    version=VERSION_NUMBER,
    description='A MkDocs plugin that supports obsidian to mkdocs convert',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs',
    url='https://github.com/ndy2/mkdocs-obsidian-support-plugin',
    author='ndy2',
    author_email='emrdbs12@gmail.com',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'obsidian-support = obsidian_support.plugin:ObsidianSupportPlugin'
        ]
    }
)
