#!/usr/bin/python27 

import sublime
import sublime_plugin
import time 

from .client.ClientManager import ClientManager

class HaskellToolsPlugin(sublime_plugin.EventListener):

    def on_load(self, view):
        print(view.file_name(), "just got loaded")

    def on_pre_save(self, view):
        print(view.file_name(), "is about to be saved")

    def on_post_save(self, view):
        print(view.file_name(), "just got saved")
        if ClientManager._instance.connected is True:
            ClientManager._instance.reload(view.file_name(), "saved")

    def on_new(self, view):
        print("new file")

    def on_modified(self, view):
        print(view.file_name(), "modified")

    def on_activated(self, view):
        print(view.file_name(), "is now the active view")

    def on_close(self, view):
        print(view.file_name(), "is no more")
        if ClientManager._instance.connected is True:
            ClientManager._instance.reload(view.file_name(), "removed")

    def on_clone(self, view):
        print(view.file_name(), "just got cloned")

    def on_window_command(self, view, command_name, args):
        print(command_name, "window_command")

    def on_post_window_command(self, view, command_name, args):
        print(command_name, "window_command")
        
        if command_name == "prompt_add_folder":
            # Ez a rész nem működik jól, előbb kéri le a foldereket mint ahogy berakná az újat
            ClientManager._instance.refresh_packages()
        elif command_name == "remove_folder":
            ClientManager._instance.refresh_packages()

    def on_view_command(self, view, command_name, args):
        print(command_name)

    def on_selection_modified_async(self, view):

        row_begin, col_begin = view.rowcol(view.sel()[0].begin())
        row_end, col_end = view.rowcol(view.sel()[0].end())
        
        row_begin += 1
        col_begin += 1
        row_end += 1
        col_end += 1

        ClientManager._instance.last_selection = str(row_begin) + ":" + str(col_begin) + "-" + str(row_end) + ":" + str(col_end)
        print(ClientManager._instance.last_selection)
        ClientManager._instance.last_selection_file_name = view.file_name()
        