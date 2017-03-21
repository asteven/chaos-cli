from setuptools import setup

name = 'chaos-cli'

setup(
    name=name,
    version='0.1.0',
    author='Steven Armstrong',
    author_email='steven-%s@armstrong.cc' % name,
    description='Chaos cli tools and utilities',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
    ],
    py_modules=['chaos.cli'],
    install_requires=[
        'Click',
        'click-plugins',
    ],
    entry_points={
        'console_scripts': [
            'chaos = chaos.cli:main'
        ],
    },
)
