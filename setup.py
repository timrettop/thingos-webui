#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

import sys
from webui.version import __version__


setup(name='thingos-webui',
      version=__version__,
      description='Basic web UI to control a Raspberry Pi running thingOS',
      author='Sven Klomp',
      author_email='mail@klomp.eu',
      url='https://github.com/avanc/thingos-webui',
      packages=find_packages(include=['webui', 'webui.*']),
      package_data={
        "": ["*.html"],
        "webui": ["static/*"],
      },
      license="GPLv2",
      platforms=["Linux"],
      long_description="",

      install_requires=['tornado>=3.1'],

      scripts=['bin/thingos_webui'],

      
     )
