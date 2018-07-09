#!/usr/bin python

from .loader import ConfigLoader

import re


class PSXCore:
    _formats = {
        r'.+\.zip': '_zip',
        r'.+\.tar': '_tar',
        r'.+\.psx': '_psx'
    }

    def _zip(self, filename):
        print('Zip file')

    def _tar(self, filename):
        print('TAR file')

    def _psx(self, filename):
        print('PSX file')

    def __init__(self):
        self._config = ConfigLoader()
        print("Core Init")

    def load(self, filename):
        for extension, fnc in iteritems(elf._formats):
            if re.match(extension, filename):
                getattr(self, fnc)(filename)
