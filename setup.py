#!/usr/bin/env python

from distutils.core import setup

import sys
sys.path.insert(1, 'src/')
from webui.version import __version__


setup(name='tingos-webui',
      version=__version__,
      description='Basic web UI to control a Raspberry Pi running thingOS',
      author='Sven Klomp',
      author_email='mail@klomp.eu',
      url='https://github.com/avanc/thingos-webui',
      packages=['webui'],
      package_dir={'webui': 'src/webui'},
      license="GPLv2",
      platforms=["Linux"],
      long_description=""
     )
