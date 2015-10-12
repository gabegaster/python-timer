import os
from setuptools import setup

import timer

github_url = 'https://github.com/gabegaster/python-timer'

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.readlines()

# read in the description from README
long_description = "\n".join(read("README.md"))

install_requires = []

setup(
    name="python-timer",
    version=timer.VERSION,
    description=("A wrapper for long-running tasks that iterate over many things, "
                 "printing friendly 'percentage done' messages to standard error."),
    long_description=long_description,
    url=github_url,
    download_url="%s/archives/master" % github_url,
    author='Gabe Gaster',
    author_email='gabe@datascopeanalytics.com',
    license='MIT',
    packages=[
        'timer',
    ],
    install_requires=install_requires,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
