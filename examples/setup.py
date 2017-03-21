from setuptools import setup, find_packages

name = 'chaos-hello'

setup(
    name=name,
    version='42',
    author='Steven Armstrong',
    author_email='steven-%s@armstrong.cc' % name,
    description='Example to illustrate using chaos-cli',
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
        'chaos-cli',
    ],
    entry_points={
        'chaos.cli.commands': [
            'hello = chaos.hello.cli:main',
        ],
    },
)
