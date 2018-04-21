#!/usr/bin/env python2
# vim:fileencoding=utf-8
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

# Debugging:
# calibre-debug -s; calibre-customize -b /path/to/plugin-remove-extension; ebook-edit

__license__ = 'GPL v3'
__copyright__ = '2018, Lucian Maly'

import os
import posixpath
from PyQt5.Qt import (
    QAction, QIcon, QInputDialog, QLabel, QLineEdit, QListWidget, QListWidgetItem, QMenu, QPainter,
    QPixmap, QRadioButton, QScrollArea, QSize, QSpinBox, QStyle, QStyledItemDelegate,
    Qt, QTimer, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, pyqtSignal
)

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
        ac.triggered.connect(self.request_remove_ext)
        return ac

    def request_remove_ext(self):
        # Import calibre/src/calibre/gui2/tweak_book/file_list.py
        from calibre.gui2.tweak_book.file_list import FileList
        self.boss.add_savepoint('Before: File Extension Remover')
        name = self.gui.file_list.current_name
        name_without_ext = posixpath.splitext(name)[0]
        print(name)
        print(name_without_ext)
        # if names is not None:
        #     def change_name(name):
        #         base = posixpath.splitext(name)[0]
        #         return base
        #     name_map = {n:change_name(n) for n in names}
        self.boss.rename_requested(name,name_without_ext)
        # self.boss.rename_done
        # self.boss.add_savepoint('After: File Extension Remover')
            # self.boss.refresh_file_list()
            # self.boss.apply_container_update_to_gui()
