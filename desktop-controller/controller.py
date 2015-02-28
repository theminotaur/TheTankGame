#!/usr/bin/python
from gi.repository import Gtk
import socket
import sys
import base64
import time

try:
	sys.argv[1]
except IndexError:
	print "please supply the host in the arguments"
	exit()

class ControllerWindow(Gtk.Window):
	carsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	turning = 0
	power = 0

	keyrefs = {
		65362: "up",
		65364: "down",
		65361: "left",
		65363: "right"
	}

	def __init__(self):
		Gtk.Window.__init__(self, title="Tank Controller")
		self.connect("delete-event", self.exit)		
		self.connect("key_press_event", self.on_key_press)
		self.connect("key_release_event", self.on_key_up)
		try:
			self.carsocket.connect((sys.argv[1], 6969))
		except:
			print "bad host"
			exit()
		


	def on_key_press(self, widget, event):
		k = event.keyval
		
		try:
			kn = self.keyrefs[k]
		except:
			return;
		if kn == "up":
			if self.power != 100:
				self.power += 5
		if kn == "down":
			if self.power != -100:
				self.power -= 5
		if kn == "left":
			self.turning = 1
		if kn == "right":
			self.turning = -1
		print self.power, self.turning
	
		self.sendControls()	

	def on_key_up(self, widget, event):
		k = event.keyval
		try:
			kn = self.keyrefs[k]
		except:
			return;

		if kn in ["up","down"]:
			self.power = 0
		if kn in ["left", "right"]:
			self.turning = 0	
		
		self.sendControls()			
	
	def sendControls(self):
		message = "%s %s" % (self.power, self.turning)
		self.carsocket.send(message)

	def loop(self):
		print "stuff"
		time.sleep(1)

	def exit(self, widget, event):
		self.carsocket.close()
		Gtk.main_quit(widget, event)

win = ControllerWindow()

win.show_all()
Gtk.main()
