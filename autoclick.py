#!/usr/bin/env python3

import time

import pynput.mouse
import pynput.keyboard
from pynput.mouse import Button

def main():
	mouse = pynput.mouse.Controller()
	click = False

	def on_click(x, y, button, pressed):
		nonlocal click
		if button == Button.x1:
			click = pressed
		return True

	with pynput.mouse.Listener(on_click=on_click):
		while True:
			if click:
				mouse.click(Button.left)
				time.sleep(0.05)
			else:
				time.sleep(0.2)

if __name__ == '__main__':
	main()
