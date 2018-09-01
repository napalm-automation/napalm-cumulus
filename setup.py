"""setup.py file."""


<<<<<<< HEAD

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

from setuptools import find_packages, setup
=======
from setuptools import setup, find_packages

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]
>>>>>>> 1993e8da9892b0b13e4f79574d3bc660015710f6
    

__author__ = 'Gabriele Gerbino <gabrielegerbino@gmail.com>'



setup(
    name="napalm-cumulus",
<<<<<<< HEAD
    version="0.3.0",
=======
    version="0.2.0",
>>>>>>> 1993e8da9892b0b13e4f79574d3bc660015710f6
    packages=find_packages(),
    author="Gabriele Gerbino",
    author_email="gabrielegerbino@gmail.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation/napalm-cumulus",
    include_package_data=True,
    install_requires=reqs,
)
