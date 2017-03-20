from setuptools import setup, find_packages

import chaos.cli

name = 'chaos-cli'

setup(
    name=name,
    version=chaos.cli.__version__,
    author='Steven Armstrong',
    author_email='steven-%s@armstrong.cc' % name,
    description=chaos.common.__doc__,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'click-plugins',
    ],
    entry_points={
        'console_scripts': [
            'chaos = chaos.cli:main'
        ],
        'chaos.cli.commands': [
            'hello = chaos.cli.commands.hello:main',
        ],
    },
)
