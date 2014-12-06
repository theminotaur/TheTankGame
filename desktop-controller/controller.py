#!/usr/bin/env python
from Tkinter import *
import bluetooth

def callback_up():
	print 'up'

def callback_down():
	print 'down'

def callback_right():
	print 'right'

def callback_left():
	print 'left'

def main():
	target_name = "Max's Windows P"
	target_address = None

	nearby_devices = bluetooth.discover_devices()

	print "All nearby Devices:"
	for baddr in nearby_devices:
		print bluetooth.lookup_name(baddr)
	
	dev = raw_input("Which device to connect to? ")

	server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

	port = 1
	server_sock.bind(("",port))
	server_sock.listen(1)

	client_sock, address = server_sock.accept()
	print "Accepted connection from ", address
	
	window = Tk()

	topframe = Frame(window)
	topframe.pack()

	bottomframe = Frame(window)
	bottomframe.pack(side=LEFT)

	up = Button(topframe, text="Up", command=callback_up, width=10, height=10);
	right = Button(bottomframe, text="Right", command=callback_right, width=10, height=10);
	down = Button(bottomframe, text="Down", command=callback_down, width=10, height=10);
	left = Button(bottomframe, text="Left", command=callback_left, width=10, height=10);

	up.pack(side=TOP)
	left.pack(side=LEFT)
	down.pack(side=LEFT)
	right.pack(side=LEFT)
	

	window.mainloop()

if(__name__ == "__main__"):
	main()
