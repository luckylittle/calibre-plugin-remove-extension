#!/usr/bin/env python2
# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

# Debugging:
# calibre-debug -s; calibre-customize -b /path/to/plugin-remove-extension; ebook-edit

__license__ = 'GPL v3'
__copyright__ = '2018, Lucian Maly'

# Standard libraries
import os
import posixpath

# PyQt libraries
from PyQt5.Qt import QTextEdit, QDockWidget, QApplication, QAction, QFileDialog, QMessageBox, QDialog, QListWidget, QVBoxLayout, QListWidgetItem, QDialogButtonBox, Qt, QTreeWidget
from PyQt5 import QtCore, QtGui

# The base class that all tools must inherit from
from calibre.gui2.tweak_book.plugin import Tool

class FileExtensionRemover(Tool):

    #: Set this to a unique name it will be used as a key
    name = 'file-extension-remover'

    #: If True the user can choose to place this tool in the plugins toolbar
    allowed_in_toolbar = True

    #: If True the user can choose to place this tool in the plugins menu
    allowed_in_menu = True

    def create_action(self, for_toolbar=True):
        # Create an action, this will be added to the plugins toolbar and
        # the plugins menu
        ac = QAction(get_icons('images/icon.png'), 'Remove extension(s)', self.gui)  # noqa
        if not for_toolbar:
            # Register a keyboard shortcut for this toolbar action. We only
            # register it for the action created for the menu, not the toolbar,
            # to avoid a double trigger
            self.register_shortcut(ac, 'file-extension-remover', default_keys=('Ctrl+Shift+Alt+E',))
        # Kick-off the function
        ac.triggered.connect(self.request_remove_ext)
        return ac

    def request_remove_ext(self):
        """
        This function removes extension of the files from the file list. This is extremely useful for raw Safari Online exports.
        """
        # Import calibre/src/calibre/gui2/tweak_book/file_list.py
        from calibre.gui2.tweak_book.file_list import FileList
        # Create a checkpoint before the action
        self.boss.add_savepoint('Before: File Extension Remover')
        # Get list of all selected file names
        names = self.gui.file_list.file_list.selected_names
            # The list looks like this:
            # set([u'9781457191435/02_half_title_xhtml.xhtml', 
            # u'9781457191435/03_full_title_xhtml.xhtml', 
            # u'9781457191435/01_praise_xhtml.xhtml'])
        if names is not None:
            # Remove the extension function
            def change_name(name):
                base = posixpath.splitext(name)[0]
                return base
                    # The base looks like this:
                    # 9781457191435/02_half_title_xhtml
                    # 9781457191435/03_full_title_xhtml
                    # 9781457191435/01_praise_xhtml
            name_map = {n:change_name(n) for n in names}
                # Name map looks like this:
                # {u'9781457191435/02_half_title_xhtml.xhtml': u'9781457191435/02_half_title_xhtml', 
                # u'9781457191435/03_full_title_xhtml.xhtml': u'9781457191435/03_full_title_xhtml', 
                # u'9781457191435/01_praise_xhtml.xhtml': u'9781457191435/01_praise_xhtml'}
            self.boss.bulk_rename_requested(name_map)
