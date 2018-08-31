"""setup.py file."""

from setuptools import setup, find_packages

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]
    

__author__ = 'Gabriele Gerbino <gabrielegerbino@gmail.com>'


setup(
    name="napalm-cumulus",
    version="0.2.0",
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
