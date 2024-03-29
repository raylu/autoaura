#!/usr/bin/env python3

import time

import pynput.mouse
import pynput.keyboard
from pynput.mouse import Button
from pynput.keyboard import Key
import pystray
from PIL import Image, ImageDraw

def main():
	def stray_click():
		nonlocal icon, keep_going
		icon.stop()
		keep_going = False

	icon = pystray.Icon('autoclick',
		icon=create_image(64, 64, 'black', 'white'),
		menu=pystray.Menu(pystray.MenuItem('close', stray_click, default=True)))
	icon.run_detached()
	mouse = pynput.mouse.Controller()
	click = False
	keep_going = True

	def on_press(key):
		nonlocal click
		if key == Key.f14:
			click = True
		return True

	def on_release(key):
		nonlocal click
		if key == Key.f14:
			click = False
		return True

	try:
		with pynput.keyboard.Listener(on_press=on_press, on_release=on_release):
			while keep_going:
				if click:
					mouse.click(Button.left)
					time.sleep(0.02)
				else:
					time.sleep(0.2)
	except KeyboardInterrupt:
		icon.stop()

def create_image(width, height, color1, color2):
	image = Image.new('RGB', (width, height), color1)
	dc = ImageDraw.Draw(image)
	dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
	dc.rectangle((0, height // 2, width // 2, height), fill=color2)
	return image

if __name__ == '__main__':
	main()
