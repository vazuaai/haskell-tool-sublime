#!/usr/bin/python27

import sublime
import sublime_plugin
import os
import socket
from threading import Thread
import subprocess
import time

from ..client.ClientManager import ClientManager
from ..client.ClientManager import get_client_manager

# Definition: 
# This class represents the server, that communicate with client.
#
class ServerManager:

	_instance = None

	# Definition:
	# This methods task is to create and start a thread with startserver() method.
	#
	def run(self,path):	
		self.server_path = path	
		thread = Thread(target = self.startserver, args=())
		thread.start()
		print("Server thread started.")
		
	# Definition:
	# Startserver merthod calls a subprocess that run an exe file that contains the server.
	#
	def startserver(self):
		try:
			server_path = get_client_manager().server_path
			subprocess.call([server_path, '4123', 'True']) #, shell=False
		except OSError:
			if (get_client_manager().server_init_error == False):
				sublime.message_dialog("The the servers path not valid! Please give below the servers path.")
				sublime.active_window().run_command("set_server_path")
		
# static method
def get_server_manager():
	
	if ServerManager._instance is None:
		ServerManager._instance = ServerManager()

	return ServerManager._instance