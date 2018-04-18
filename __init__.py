#!/usr/bin/env python2
# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__ = 'GPL v3'
__copyright__ = '2018, Lucian Maly'

from calibre.customize import EditBookToolPlugin

class FileExtensionRemoverPlugin(EditBookToolPlugin):

    name = 'File Extension Remover'
    version = (0, 0, 2)
    author = 'Lucian Maly'
    supported_platforms = ['windows', 'osx', 'linux']
    description = 'This simple plugin removes file extension(s) of the selected file(s).'
    minimum_calibre_version = (1, 46, 0)
